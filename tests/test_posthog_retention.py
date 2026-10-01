import json
import unittest
from datetime import datetime, timezone

from scripts.posthog_retention import (
    ApiResponse,
    PostHogClient,
    RetentionError,
    assess_requests,
    build_query,
    deletion_cutoff,
    run,
    subtract_calendar_months,
    submission_id,
)


UTC = timezone.utc
NOW = datetime(2026, 10, 1, 12, 0, tzinfo=UTC)


class FakeTransport:
    def __init__(self, requests=None, previews=None, submit_status=201):
        self.requests = requests or []
        self.previews = list(previews or [0, 0])
        self.submit_status = submit_status
        self.calls = []

    def __call__(self, method, path, payload):
        self.calls.append((method, path, payload))
        if method == "GET":
            return ApiResponse(200, {"results": self.requests})
        if path.endswith("/preview/"):
            return ApiResponse(200, {"count": self.previews.pop(0)})
        return ApiResponse(self.submit_status, {"id": "request-1", "status": "pending"})


class CalendarTests(unittest.TestCase):
    def test_month_end_is_bounded(self):
        value = datetime(2026, 8, 31, 9, 30, tzinfo=UTC)
        self.assertEqual(subtract_calendar_months(value, 6), datetime(2026, 2, 28, 9, 30, tzinfo=UTC))

    def test_leap_day_is_bounded(self):
        value = datetime(2024, 8, 31, 9, 30, tzinfo=UTC)
        self.assertEqual(subtract_calendar_months(value, 6), datetime(2024, 2, 29, 9, 30, tzinfo=UTC))

    def test_safety_window_moves_cutoff_forward(self):
        self.assertEqual(deletion_cutoff(NOW, 14), datetime(2026, 4, 15, 12, 0, tzinfo=UTC))


class QueryTests(unittest.TestCase):
    def test_known_query_has_strict_scope(self):
        query = build_query(datetime(2026, 4, 15, tzinfo=UTC), known_events=True)
        self.assertIn("SELECT uuid", query)
        self.assertIn("properties.environment = 'production'", query)
        self.assertIn("properties.synthetic = false", query)
        self.assertIn("properties.surface IN ('website', 'docs')", query)
        self.assertIn("website_beta_interest_submitted", query)
        self.assertIn("event IN", query)
        self.assertNotIn("distinct_id", query)

    def test_unknown_query_inverts_only_event_allowlist(self):
        known = build_query(datetime(2026, 4, 15, tzinfo=UTC), known_events=True)
        unknown = build_query(datetime(2026, 4, 15, tzinfo=UTC), known_events=False)
        self.assertEqual(known.replace("event IN", "event NOT IN"), unknown)

    def test_submission_id_is_stable_per_day_and_query(self):
        query = build_query(datetime(2026, 4, 15, tzinfo=UTC), known_events=True)
        self.assertEqual(submission_id(NOW, query), submission_id(NOW, query))
        self.assertNotEqual(submission_id(NOW, query), submission_id(datetime(2026, 10, 2, tzinfo=UTC), query))


class RequestStateTests(unittest.TestCase):
    def test_request_states_are_minimized(self):
        state = assess_requests(
            [
                {"id": "a", "status": "pending", "created_at": "2026-09-30T12:00:00Z", "query": "secret"},
                {"id": "b", "status": "completed", "created_at": "2026-09-29T12:00:00Z"},
            ],
            NOW,
        )
        self.assertEqual(state["completed"], 1)
        self.assertEqual(state["active"], [{"request_id": "a", "status": "pending", "age_days": 1}])
        self.assertNotIn("secret", json.dumps(state))

    def test_unknown_status_blocks(self):
        transport = FakeTransport(requests=[{"id": "x", "status": "mystery"}])
        with self.assertRaisesRegex(RetentionError, "Unbekannter"):
            run(PostHogClient("test", 289846, transport), "dry-run", NOW, 14)

    def test_failed_request_blocks(self):
        transport = FakeTransport(requests=[{"id": "x", "status": "failed"}])
        with self.assertRaisesRegex(RetentionError, "fehlgeschlagen"):
            run(PostHogClient("test", 289846, transport), "dry-run", NOW, 14)

    def test_recent_pending_request_prevents_duplicate(self):
        transport = FakeTransport(requests=[{"id": "x", "status": "queued", "created_at": "2026-09-29T12:00:00Z"}])
        result = run(PostHogClient("test", 289846, transport), "reconcile-submit", NOW, 14)
        self.assertEqual(result["result"], "pending")
        self.assertEqual(len(transport.calls), 1)

    def test_stale_pending_request_fails_visibly(self):
        transport = FakeTransport(requests=[{"id": "x", "status": "queued", "created_at": "2026-09-20T12:00:00Z"}])
        with self.assertRaisesRegex(RetentionError, "neun Tage"):
            run(PostHogClient("test", 289846, transport), "reconcile-submit", NOW, 14)

    def test_pending_request_without_timestamp_fails_visibly(self):
        transport = FakeTransport(requests=[{"id": "x", "status": "queued"}])
        with self.assertRaisesRegex(RetentionError, "Erstellzeitpunkt"):
            run(PostHogClient("test", 289846, transport), "reconcile-submit", NOW, 14)


class RunTests(unittest.TestCase):
    def test_dry_run_never_submits(self):
        transport = FakeTransport(previews=[0, 4])
        result = run(PostHogClient("test", 289846, transport), "dry-run", NOW, 14)
        self.assertEqual(result["result"], "preview")
        self.assertEqual(result["event_count"], 4)
        self.assertEqual([call[0] for call in transport.calls], ["GET", "POST", "POST"])

    def test_unknown_events_block_before_known_preview(self):
        transport = FakeTransport(previews=[2])
        with self.assertRaisesRegex(RetentionError, "Positivliste"):
            run(PostHogClient("test", 289846, transport), "reconcile-submit", NOW, 14)
        self.assertEqual(len(transport.calls), 2)

    def test_zero_events_do_not_create_empty_request(self):
        transport = FakeTransport(previews=[0, 0])
        result = run(PostHogClient("test", 289846, transport), "reconcile-submit", NOW, 14)
        self.assertEqual(result["result"], "preview")
        self.assertEqual(len(transport.calls), 3)

    def test_submit_uses_only_query_and_id(self):
        transport = FakeTransport(previews=[0, 3])
        result = run(PostHogClient("test", 289846, transport), "reconcile-submit", NOW, 14)
        self.assertEqual(result["result"], "submitted")
        payload = transport.calls[-1][2]
        self.assertEqual(set(payload), {"query", "variables", "submission_id"})
        self.assertNotIn("test", json.dumps(payload))

    def test_missing_key_is_rejected(self):
        with self.assertRaisesRegex(RetentionError, "fehlt"):
            PostHogClient("", 289846)


if __name__ == "__main__":
    unittest.main()
