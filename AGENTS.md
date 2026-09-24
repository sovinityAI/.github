# Sovinity organization human-and-AI working agreement

## GitHub task contract

- GitHub Issues are the source of truth for planned work. The organization project is [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1).
- Implementation work requires an open issue in the repository that owns the result. Organization-wide process and template work belongs in `sovinityAI/.github`.
- Before editing, read the complete issue, comments, labels, dependencies, linked pull requests, and acceptance criteria.
- Keep the change within the issue scope. Record newly discovered work as a separate linked issue instead of silently expanding scope.
- Do not mark an issue complete until every acceptance criterion has been checked against concrete evidence.
- Chat messages, local notes, and an agent's memory are not durable task state. Record decisions, blockers, handoffs, and completion evidence in the GitHub Issue or linked pull request.

## Mandatory Project synchronization

Humans and AI agents follow the same lifecycle in [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1):

- **Backlog**: valid work that is not yet ready or selected.
- **Ready**: specified, unblocked, and startable without inventing a product decision.
- **In progress**: a named human or AI agent is actively working on the issue, even when the work may take only minutes.
- **Needs input**: work is paused for a named decision, dependency, sensitive input, or external authority.
- **In review**: output exists and is waiting for human, legal, visual, or technical verification.
- **Done**: the acceptance criteria are verified and the issue is closed.

Keep the Project's **Next actor** field current: `AI agent`, `Mario`, `Ludwig`, `Both founders`, `External reviewer`, or `None`.

- On start: move the issue to **In progress** and set **Next actor** to the active owner.
- On pause or handoff: add a concise Issue comment stating what is complete, what is needed next, and who must act; then move to **Needs input** and update **Next actor**.
- On implementation completion: record verification evidence, move to **In review**, and select the reviewer as **Next actor**.
- On verified completion: close the issue, move it to **Done**, and set **Next actor** to `None`.
- Never leave an issue **In progress** when work has stopped or an agent turn ends without an active continuation.

## Selecting the next task

- When asked what to do next, inspect open issues across `sovinityAI/cloud`, `sovinityAI/SovinityDesktop`, `sovinityAI/website`, and `sovinityAI/.github`.
- Exclude epics, **Needs input** work, and issues already covered by an open pull request.
- Prefer `priority:p0`, then `priority:p1`, then `priority:p2`. Within a priority, recommend the smallest ready item that removes uncertainty or unblocks other work.
- Recommend exactly one next issue and identify up to three follow-ups separately.

## Git and pull requests

- Use a branch named `<actor>/<issue-number>-<short-slug>` for implementation work, for example `codex/12-fix-import` or `ludwig/12-fix-import`.
- Reference the issue in commits and pull requests. Use `Closes #<number>` for same-repository issues or `Closes owner/repository#<number>` for cross-repository issues.
- Pull requests must summarize the change, list verification performed, and disclose remaining risks or unfinished acceptance criteria.
- Do not merge or close an issue merely because files were changed; verification decides completion.

## Organization repository scope

- Keep shared issue forms, pull-request templates, workflow documentation, and the public organization profile factual and reusable.
- Do not place repository-specific product requirements in shared templates.
- Never add secrets, personal data, internal-only operational details, or unverified public claims.
