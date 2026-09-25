# Sovinity human-and-AI product workflow

GitHub Issues are the authoritative record of planned work for Sovinity. The organization project [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1) provides the cross-repository view; it is not a second backlog.

Sovinity is one product with one backlog. Repositories identify where implementation happens; they do not define separate products, roadmaps, or prioritization queues.

This contract is tool-neutral. It applies equally to Mario, Ludwig, Codex, another AI agent, and future contributors. Sovinity uses a pull system: product work is made ready and ordered, while contributors claim work only when they have capacity. A fast AI implementation does not skip lifecycle states: status describes the current truth, not the expected duration.

## Where an issue belongs

- `sovinityAI/cloud`: hosted/private-workspace application, services, AI, storage, connectors, operations, and recovery
- `sovinityAI/SovinityDesktop`: desktop application, local runtime, packaging, and stores
- `sovinityAI/website`: public website, domains, legal pages, and launch work
- `sovinityAI/product`: cross-product vision, strategy, roadmap, decisions, and discovery
- `sovinityAI/.github`: organization-wide process, shared templates, and cross-repository governance

Cross-repository initiatives use a parent issue with repository-specific sub-issues. Dependencies must be recorded as GitHub issue relationships rather than only described in prose.

## Portable human-and-AI interface

Sovinity uses existing open formats instead of a vendor-specific agent or memory protocol:

- [`AGENTS.md`](https://agents.md/) contains repository-level working instructions for humans and compatible AI coding agents.
- If a tool cannot load `AGENTS.md` directly, its smallest possible adapter may import or point to that file. Shared rules must not be copied into a competing tool-specific source of truth.
- [Agent Skills](https://agentskills.io/) (`SKILL.md`) may package reusable procedures, scripts, references, and templates. They must not contain the current product strategy, roadmap, decisions, credentials, or personal data.
- The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) may connect an agent to external tools and data. It is an integration interface, not a replacement for durable project records.
- GitHub Issues, pull requests, and version-controlled repository documents hold durable task and product state. Chat history, local notes, profiles, memory, and sessions from any tool may help an individual contributor but are non-canonical and disposable.

## Product milestones and views

The Project field **Product milestone** groups Issues by product outcome across repositories. It is the shared milestone model; repository milestones remain local metadata and must not replace it.

The Project maintains these working views:

- **Product Board**: all product work grouped by Status, with Repository, Product milestone, Priority, Work type, and Benötigter Input visible where useful
- **Product Milestones**: product work grouped by Product milestone, independent of implementation repository
- **Ready Queue**: unassigned work in Ready, ordered by Priority and dependency order
- **Product Operations**: organization process and governance work from `sovinityAI/.github`

An Issue appears once in the shared Project. Its repository tells contributors where to implement it. A cross-repository outcome has one coordinating parent Issue and linked implementation sub-issues in the repositories that own the resulting changes.

## Issue intake

- Prefer creating an Issue from the Project when the implementation repository is already known.
- Otherwise use the shared **Product task** or **Bug report** form. The forms add the new Issue to **Sovinity Product** through `projects: ["sovinityAI/1"]`.
- Blank Issues are disabled for normal intake so that outcome, acceptance criteria, dependencies, verification, and Work type are not skipped.
- The creator must have permission to add items to the organization Project. If an Issue is created through another route, add it to the Project during triage.
- Native repository-specific auto-add workflows may remain temporarily as safety nets. They are not required for every repository and do not replace the shared forms or Project-first creation.

## Ready criteria

An issue is ready when it has:

- a concrete outcome,
- acceptance criteria that can be checked,
- the correct repository and priority,
- known dependencies or an explicit statement that none are known,
- enough context to begin without inventing product decisions,
- no unresolved blocker that requires external authority or sensitive input,
- no assignee or existing claim.

## Project status

- **Backlog**: valid work, not yet ready or selected
- **Ready**: sufficiently specified, prioritized, unblocked, unassigned, and available to pull
- **In progress**: pulled and actively claimed by a human or AI contributor, even if execution takes only minutes
- **Needs input**: paused for a named decision, dependency, sensitive input, or external authority
- **In review**: output exists and human, legal, visual, or technical evidence is being reviewed
- **Done**: acceptance criteria are verified and the issue is closed

Every Issue in **Needs input** must have a short **Benötigter Input** value that states the missing decision, information, dependency, or external result. Clear or update that value when the Issue leaves Needs input.

## Work type

The Project field **Work type** helps contributors decide whether an issue is suitable to pull. It is classification, never assignment:

- **Any contributor**: no special execution constraint
- **AI-suitable**: sufficiently bounded work that an AI agent may execute; humans may also pull it
- **Human judgment**: a product, legal, financial, ethical, or other decision must be made by a human
- **Pairing**: the work should be performed collaboratively by two humans or by a human with an AI agent
- **External**: completion depends on a customer, lawyer, tax adviser, security reviewer, or another party outside the active team

An issue in **Ready** stays unassigned regardless of its Work type. The type does not reserve work for anyone or create an obligation.

## Priority

- **P0**: required before the next pilot, release, or externally committed gate
- **P1**: important product or operational work after current P0 items
- **P2**: useful improvement without a near-term gate

Priority expresses consequence, not size. Dependencies and readiness determine the executable order within a priority.

## Pull policy and work-in-progress limit

- Mario and Ludwig curate outcomes, readiness, priority, dependencies, and top-to-bottom order in the shared **Ready** queue.
- A contributor with capacity pulls the highest-priority suitable issue. Skipping a higher item requires a short Issue comment explaining the dependency, access, or capability reason.
- Before claiming, re-read the Issue and confirm that it remains **Ready**, unassigned, and without a newer claim comment.
- Claim atomically: assign the accountable GitHub user, add an AI claim comment if the AI has no separate GitHub identity, and move the item to **In progress** before editing.
- Each contributor or AI session normally has at most one implementation issue in **In progress**. An exception must be explained in both affected Issues.
- Review is also pulled. Moving output to **In review** does not push it to a named reviewer; an available qualified reviewer claims it.

Pull is not an unprioritized free choice. Product responsibility determines what is Ready and in which order; contributor capacity determines when the next suitable item starts.

## Implementation lifecycle

1. Start from an open issue; create one first if implementation work has no issue.
2. Add the issue to the organization Project and confirm scope, acceptance criteria, priority, dependencies, and **Work type**.
3. Product preparation ends in an unassigned **Ready** issue. Do not nominate a person or AI agent to perform it.
4. When capacity is available, pull the highest-priority suitable issue: confirm it is unclaimed, assign the accountable GitHub user, add an AI claim comment where needed, and move it to **In progress**.
5. Work on a branch named `<actor>/<issue-number>-<short-slug>`.
6. Keep durable state in GitHub. Chat, local notes, and agent memory may support the work but never replace Issue comments or pull-request evidence.
7. If work pauses, comment with what is complete and the exact missing input or dependency; clear the active assignment and move to **Needs input**. Naming somebody who can provide input is a dependency signal, not an assigned obligation.
8. Link the pull request with `Closes #<number>` or the full cross-repository reference.
9. Record tests, checks, screenshots, decisions, and remaining uncertainty in the pull request.
10. When implementation is ready, clear the implementation assignment and move the item to **In review**. A qualified reviewer pulls the review when capacity is available.
11. Merge and close only when acceptance criteria are satisfied; then move the item to **Done**.

An AI agent must reconcile the Project before ending its work: no stopped task may remain **In progress**, and every pause must record the exact next action or missing input. AI agents do not pull work silently; they use the same claim protocol as humans.

Newly discovered scope becomes a separate linked issue. It must not be hidden in a pull request or silently added to the current task.

## Issue as the durable handoff

The Issue or linked pull request must make it possible for a different human or AI agent to continue without reconstructing a private conversation. Record:

- the current outcome and checked acceptance criteria,
- decisions made and by whom,
- relevant evidence and verification results,
- unresolved risks or blockers,
- the exact next action or missing input.

## Asking Codex for the next task

Use this request:

> Read the open GitHub Issues and the Sovinity Product project across all Sovinity repositories. Reconcile stale status, assignments, and Work type values before selecting work. Pull the highest-priority suitable, unassigned issue from Ready; within a priority, respect dependencies and the Project's top-to-bottom order. Confirm it is still unclaimed, claim it, move it to In progress, and keep the Issue and Project synchronized. If only recommending rather than starting, recommend exactly one issue and list up to three follow-ups without assigning them.
