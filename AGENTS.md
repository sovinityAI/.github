# Sovinity organization human-and-AI working agreement

## GitHub task contract

- GitHub Issues are the source of truth for planned work. The organization project is [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1).
- Sovinity has one product backlog across all repositories. The repository identifies the technical implementation home; it does not create a separate product or backlog.
- Implementation work requires an open issue in the repository that owns the result. Organization-wide process and template work belongs in `sovinityAI/.github`.
- Before editing, read the complete issue, comments, labels, dependencies, linked pull requests, and acceptance criteria.
- Keep the change within the issue scope. Record newly discovered work as a separate linked issue instead of silently expanding scope.
- Do not mark an issue complete until every acceptance criterion has been checked against concrete evidence.
- Chat messages, local notes, and an agent's memory are not durable task state. Record decisions, blockers, handoffs, and completion evidence in the GitHub Issue or linked pull request.

## Mandatory Project synchronization

Humans and AI agents follow the same lifecycle in [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1):

- **Backlog**: valid work that is not yet ready or selected.
- **Ready**: specified, unblocked, prioritized, unassigned, and available for a suitable contributor to pull.
- **In progress**: a human or AI contributor has pulled and claimed the issue and is actively working on it, even when the work may take only minutes.
- **Needs input**: work is paused for a named decision, dependency, sensitive input, or external authority.
- **In review**: output exists and is waiting for human, legal, visual, or technical verification.
- **Done**: the acceptance criteria are verified and the issue is closed.

Keep the Project's **Work type** field current: `Any contributor`, `AI-suitable`, `Human judgment`, `Pairing`, or `External`. It describes the work and never assigns it.

Keep the Project's **Product milestone** field current for product work. Product milestones describe cross-repository outcomes. Repository milestones remain repository-local and must not be used as the shared product roadmap.

- Create new work from the Project or through the organization's shared issue forms. Both paths must add the Issue to **Sovinity Product**.
- Do not create blank Issues for normal product work. If an exceptional maintenance Issue is created without a form, add it to the Project immediately.
- Native Project auto-add workflows are optional safety nets, not the source of truth for intake.

- Product work is prepared and ordered in **Ready**; it is not pushed to a person or AI agent.
- On pull: confirm that the Issue is still unassigned and unclaimed, assign yourself or the accountable GitHub user, add a short claim comment when an AI has no separate GitHub identity, and move the issue to **In progress**.
- Limit work in progress to one implementation issue per contributor or AI session unless a documented exception is necessary.
- On pause: add a concise Issue comment stating what is complete and the exact missing input or dependency; clear the active assignment and move to **Needs input**.
- On implementation completion: record verification evidence, clear the implementation assignment, and move to **In review** so an available reviewer can pull it.
- On verified completion: close the issue and move it to **Done**.
- Never leave an issue **In progress** when work has stopped or an agent turn ends without an active continuation.

## Selecting the next task

- When asked what to do next, inspect open issues across `sovinityAI/cloud`, `sovinityAI/SovinityDesktop`, `sovinityAI/website`, `sovinityAI/product`, and `sovinityAI/.github`.
- Exclude epics, **Needs input** work, and issues already covered by an open pull request.
- Pull from **Ready**, not from another contributor's assigned work. Prefer `priority:p0`, then `priority:p1`, then `priority:p2`; within a priority, follow dependency order and then the Project's top-to-bottom order.
- Skip work whose **Work type** is unsuitable for the available contributor. `AI-suitable` means AI may perform it; it does not exclude a human contributor.
- Recommend exactly one next issue and identify up to three follow-ups separately.

## Git and pull requests

- Use a branch named `<actor>/<issue-number>-<short-slug>` for implementation work, for example `codex/12-fix-import` or `ludwig/12-fix-import`.
- Reference the issue in commits and pull requests. Use `Closes #<number>` for same-repository issues or `Closes owner/repository#<number>` for cross-repository issues.
- Pull requests must summarize the change, list verification performed, and disclose remaining risks or unfinished acceptance criteria.
- Do not merge or close an issue merely because files were changed; verification decides completion.

## Tool-neutral agent guidance

- Use the repository's `AGENTS.md` as the shared, tool-neutral instruction file. A tool-specific adapter may import or point to it when necessary, but must not maintain a divergent copy of the shared rules.
- Keep durable task and product state in GitHub and version-controlled repository documents. Chat history, local notes, profiles, memory, and sessions from any AI tool are temporary aids, never shared infrastructure or a source of truth.
- Use Agent Skills (`SKILL.md`) only for reusable procedures, scripts, references, and templates. Do not place the current product strategy, roadmap, decisions, credentials, or personal data in a skill.
- Use the Model Context Protocol (MCP) only when a standard interface to external tools or data is needed. MCP connections do not replace Issues, pull requests, or repository documents as the durable record.

## Organization repository scope

- Keep shared issue forms, pull-request templates, workflow documentation, and the public organization profile factual and reusable.
- Do not place repository-specific product requirements in shared templates.
- Never add secrets, personal data, internal-only operational details, or unverified public claims.
