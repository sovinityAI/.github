# Sovinity human-and-AI product workflow

GitHub Issues are the authoritative record of planned work for Sovinity. The organization project [Sovinity Product](https://github.com/orgs/sovinityAI/projects/1) provides the cross-repository view; it is not a second backlog.

This contract is tool-neutral. It applies equally to Mario, Ludwig, Codex, another AI agent, and future contributors. A fast AI implementation does not skip lifecycle states: status describes the current truth, not the expected duration.

## Where an issue belongs

- `sovinityAI/cloud`: hosted/private-workspace application, services, AI, storage, connectors, operations, and recovery
- `sovinityAI/SovinityDesktop`: desktop application, local runtime, packaging, and stores
- `sovinityAI/website`: public website, domains, legal pages, and launch work
- `sovinityAI/.github`: organization-wide process, shared templates, and cross-repository governance

Cross-repository initiatives use a parent issue with repository-specific sub-issues. Dependencies must be recorded as GitHub issue relationships rather than only described in prose.

## Ready criteria

An issue is ready when it has:

- a concrete outcome,
- acceptance criteria that can be checked,
- the correct repository and priority,
- known dependencies or an explicit statement that none are known,
- enough context to begin without inventing product decisions,
- no unresolved blocker that requires external authority or sensitive input.

## Project status

- **Backlog**: valid work, not yet ready or selected
- **Ready**: sufficiently specified and unblocked
- **In progress**: actively owned by a named human or AI agent, even if execution takes only minutes
- **Needs input**: paused for a named decision, dependency, sensitive input, or external authority
- **In review**: output exists and human, legal, visual, or technical evidence is being reviewed
- **Done**: acceptance criteria are verified and the issue is closed

## Next actor

The Project field **Next actor** answers one question: who can move this issue forward now?

- **AI agent**: specified work can continue autonomously within the Issue contract
- **Mario** or **Ludwig**: that founder owns the next decision or action
- **Both founders**: a joint product, legal, financial, or ownership decision is required
- **External reviewer**: legal, tax, security, customer, or other professional review is required
- **None**: no action is expected until a linked dependency changes, or the issue is complete

`Next actor` is routing information, not ownership history. Change it whenever the work is handed off.

## Priority

- **P0**: required before the next pilot, release, or externally committed gate
- **P1**: important product or operational work after current P0 items
- **P2**: useful improvement without a near-term gate

Priority expresses consequence, not size. Dependencies and readiness determine the executable order within a priority.

## Implementation lifecycle

1. Start from an open issue; create one first if implementation work has no issue.
2. Add the issue to the organization Project and confirm scope, acceptance criteria, priority, dependencies, and **Next actor**.
3. Move the issue to **In progress** when work actually starts, and set **Next actor** to the active human or `AI agent`.
4. Work on a branch named `<actor>/<issue-number>-<short-slug>`.
5. Keep durable state in GitHub. Chat, local notes, and agent memory may support the work but never replace Issue comments or pull-request evidence.
6. If work pauses, comment with what is complete, the exact missing input, and the responsible actor; move to **Needs input** and update **Next actor**.
7. Link the pull request with `Closes #<number>` or the full cross-repository reference.
8. Record tests, checks, screenshots, decisions, and remaining uncertainty in the pull request.
9. Move to **In review** and set **Next actor** to the human or external reviewer who must verify the result.
10. Merge and close only when acceptance criteria are satisfied; then move the item to **Done** and set **Next actor** to `None`.

An AI agent must reconcile the Project before ending its work: no stopped task may remain **In progress**, and every handoff must name the next actor and missing input.

Newly discovered scope becomes a separate linked issue. It must not be hidden in a pull request or silently added to the current task.

## Issue as the durable handoff

The Issue or linked pull request must make it possible for a different human or AI agent to continue without reconstructing a private conversation. Record:

- the current outcome and checked acceptance criteria,
- decisions made and by whom,
- relevant evidence and verification results,
- unresolved risks or blockers,
- the exact next action and **Next actor**.

## Asking Codex for the next task

Use this request:

> Read the open GitHub Issues and the Sovinity Product project across all Sovinity repositories. Reconcile stale status or Next actor values before recommending work. Exclude epics, Needs input issues, and work already covered by an open pull request. Order Ready work by P0, P1, then P2, taking dependencies and uncertainty reduction into account. Recommend exactly one next issue and list up to three follow-ups.
