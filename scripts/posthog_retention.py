#!/usr/bin/env python3
"""Sicherer PostHog-EU-Loeschlauf fuer Sovinity-Analytics-Ereignisse."""

from __future__ import annotations

import argparse
import calendar
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Callable


API_HOST = "https://eu.posthog.com"
DEFAULT_PROJECT_ID = 289846
DEFAULT_SAFETY_DAYS = 14

EVENTS_BY_SURFACE = {
    "website": (
        "$autocapture",
        "website_beta_interest_submitted",
        "website_download_clicked",
        "website_error",
        "website_home_viewed",
        "website_offer_viewed",
    ),
    "docs": (
        "docs_answer_completed",
        "docs_app_started",
        "docs_citation_opened",
        "docs_index_ready",
        "docs_measurement_started",
        "docs_source_added",
    ),
}

ACTIVE_STATUSES = {"draft", "pending", "approved", "in_progress", "queued"}
FAILED_STATUSES = {"failed"}
COMPLETED_STATUSES = {"completed"}


class RetentionError(RuntimeError):
    pass


def subtract_calendar_months(value: datetime, months: int) -> datetime:
    if value.tzinfo is None:
        raise ValueError("UTC-Zeitpunkt mit Zeitzone erforderlich")
    total_months = value.year * 12 + value.month - 1 - months
    year, month_index = divmod(total_months, 12)
    month = month_index + 1
    day = min(value.day, calendar.monthrange(year, month)[1])
    return value.replace(year=year, month=month, day=day)


def deletion_cutoff(now: datetime, safety_days: int = DEFAULT_SAFETY_DAYS) -> datetime:
    """Waehlt Ereignisse, deren Sechsmonatsfrist im Sicherheitsfenster endet."""
    return subtract_calendar_months(now.astimezone(timezone.utc) + timedelta(days=safety_days), 6)


def _quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _common_predicate(cutoff: datetime) -> str:
    cutoff_text = cutoff.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return "\n".join(
        (
            f"timestamp <= toDateTime({_quote(cutoff_text)}, 'UTC')",
            "properties.environment = 'production'",
            "properties.synthetic = false",
            "properties.surface IN ('website', 'docs')",
        )
    )


def build_query(cutoff: datetime, *, known_events: bool) -> str:
    all_events = sorted(event for events in EVENTS_BY_SURFACE.values() for event in events)
    operator = "IN" if known_events else "NOT IN"
    event_list = ", ".join(_quote(event) for event in all_events)
    predicate = _common_predicate(cutoff).replace("\n", "\n  AND ")
    return (
        "SELECT uuid\n"
        "FROM events\n"
        f"WHERE {predicate}\n"
        f"  AND event {operator} ({event_list})"
    )


def query_fingerprint(query: str) -> str:
    return hashlib.sha256(query.encode("utf-8")).hexdigest()[:12]


def submission_id(now: datetime, query: str) -> str:
    name = f"sovinity-retention:{now.astimezone(timezone.utc).date()}:{query_fingerprint(query)}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, name))


@dataclass(frozen=True)
class ApiResponse:
    status: int
    data: dict[str, Any]


Transport = Callable[[str, str, dict[str, Any] | None], ApiResponse]


class PostHogClient:
    def __init__(
        self,
        read_api_key: str,
        write_api_key: str,
        project_id: int,
        transport: Transport | None = None,
    ) -> None:
        if not read_api_key:
            raise RetentionError("POSTHOG_RETENTION_READ_API_KEY fehlt")
        if not write_api_key:
            raise RetentionError("POSTHOG_RETENTION_WRITE_API_KEY fehlt")
        self.project_id = project_id
        self._read_api_key = read_api_key
        self._write_api_key = write_api_key
        self._transport = transport or self._request

    @property
    def base_path(self) -> str:
        return f"/api/projects/{self.project_id}/data_deletion_requests"

    def _request(self, method: str, path: str, payload: dict[str, Any] | None) -> ApiResponse:
        body = None if payload is None else json.dumps(payload, separators=(",", ":")).encode("utf-8")
        api_key = self._read_api_key if method == "GET" else self._write_api_key
        request = urllib.request.Request(
            API_HOST + path,
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "sovinity-posthog-retention/1",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                data = json.loads(raw) if raw else {}
                return ApiResponse(response.status, data)
        except urllib.error.HTTPError as error:
            error.read()
            raise RetentionError(f"PostHog API antwortet mit HTTP {error.code}") from error
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            raise RetentionError("PostHog API ist nicht belastbar erreichbar") from error

    def list_requests(self) -> list[dict[str, Any]]:
        response = self._transport("GET", self.base_path + "/?limit=100", None)
        if response.status != 200 or not isinstance(response.data.get("results"), list):
            raise RetentionError("Loeschauftraege konnten nicht gelesen werden")
        return response.data["results"]

    def preview(self, query: str) -> int:
        response = self._transport("POST", self.base_path + "/preview/", {"query": query, "variables": {}})
        count = response.data.get("count")
        if response.status != 200 or isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise RetentionError("Loeschvorschau lieferte keinen belastbaren Zaehler")
        return count

    def submit(self, query: str, request_id: str) -> dict[str, Any]:
        response = self._transport(
            "POST",
            self.base_path + "/",
            {"query": query, "variables": {}, "submission_id": request_id},
        )
        if response.status not in {200, 201, 202} or not response.data.get("id"):
            raise RetentionError("Loeschauftrag wurde nicht bestaetigt")
        return response.data


def _parse_created_at(request: dict[str, Any]) -> datetime | None:
    value = request.get("created_at")
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def assess_requests(requests: list[dict[str, Any]], now: datetime) -> dict[str, Any]:
    active: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    unknown: list[dict[str, Any]] = []
    completed = 0
    for request in requests:
        status = str(request.get("status", "")).lower()
        summary = {
            "request_id": request.get("id"),
            "status": status or "missing",
            "age_days": None,
        }
        created_at = _parse_created_at(request)
        if created_at is not None:
            summary["age_days"] = max(0, (now - created_at).days)
        if status in ACTIVE_STATUSES:
            active.append(summary)
        elif status in FAILED_STATUSES:
            failed.append(summary)
        elif status in COMPLETED_STATUSES:
            completed += 1
        else:
            unknown.append(summary)
    return {"active": active, "failed": failed, "unknown": unknown, "completed": completed}


def run(client: PostHogClient, mode: str, now: datetime, safety_days: int) -> dict[str, Any]:
    state = assess_requests(client.list_requests(), now)
    if state["failed"]:
        raise RetentionError("Mindestens ein frueherer Loeschauftrag ist fehlgeschlagen")
    if state["unknown"]:
        raise RetentionError("Unbekannter PostHog-Loeschstatus; kein neuer Auftrag")
    if state["active"]:
        if any(item["age_days"] is None for item in state["active"]):
            raise RetentionError("Offener Loeschauftrag ohne belastbaren Erstellzeitpunkt")
        oldest = max(item["age_days"] or 0 for item in state["active"])
        if oldest > 9:
            raise RetentionError("Loeschauftrag ist laenger als neun Tage offen")
        return {"result": "pending", "active": state["active"], "completed": state["completed"]}

    cutoff = deletion_cutoff(now, safety_days)
    known_query = build_query(cutoff, known_events=True)
    unknown_query = build_query(cutoff, known_events=False)
    unknown_count = client.preview(unknown_query)
    if unknown_count:
        raise RetentionError("Unbekannte Sovinity-Ereignisse liegen vor; Positivliste zuerst pruefen")
    count = client.preview(known_query)
    result: dict[str, Any] = {
        "result": "preview",
        "cutoff_utc": cutoff.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "safety_days": safety_days,
        "event_count": count,
        "query_fingerprint": query_fingerprint(known_query),
        "completed_requests": state["completed"],
    }
    if mode == "dry-run" or count == 0:
        return result

    request = client.submit(known_query, submission_id(now, known_query))
    result.update(
        {
            "result": "submitted",
            "request_id": request.get("id"),
            "request_status": request.get("status"),
        }
    )
    return result


def _arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("dry-run", "reconcile-submit"), default="dry-run")
    parser.add_argument("--project-id", type=int, default=DEFAULT_PROJECT_ID)
    parser.add_argument("--safety-days", type=int, default=DEFAULT_SAFETY_DAYS)
    return parser.parse_args()


def main() -> int:
    args = _arguments()
    if not 0 <= args.safety_days <= 31:
        print(json.dumps({"result": "error", "message": "safety-days ausserhalb 0..31"}))
        return 2
    try:
        client = PostHogClient(
            os.environ.get("POSTHOG_RETENTION_READ_API_KEY", ""),
            os.environ.get("POSTHOG_RETENTION_WRITE_API_KEY", ""),
            args.project_id,
        )
        result = run(client, args.mode, datetime.now(timezone.utc), args.safety_days)
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0
    except RetentionError as error:
        print(json.dumps({"result": "error", "message": str(error)}, sort_keys=True, separators=(",", ":")))
        return 1


if __name__ == "__main__":
    sys.exit(main())
