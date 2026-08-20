---
name: implement
description: Implement a scoped Spec or set of Tickets through testing, documentation, review, and a focused commit. Use only when the user explicitly asks to implement the work.
---

Implement the work described by the user in the Spec or Tickets. A Spec is
sufficient input — do not require `$to-tickets` first.

## Resolve the complete scope

- **Spec:** implement every approved associated Ticket in dependency order. The
  frontier only identifies the next executable Ticket; completing one frontier
  Ticket is not a stopping condition. Continue until every associated Ticket
  meets its acceptance criteria or a genuine unresolved blocker prevents any
  further in-scope progress.
- **Ticket set:** implement every supplied Ticket in dependency order.
- **Single Ticket:** stop after one Ticket only when the user explicitly scopes
  the request to that single Ticket.

The user's explicit scope overrides an inferred tracker frontier. Never silently
reduce a Spec or Ticket set to only its first ready Ticket.

Read the complete source work and its comments, dependencies, acceptance
criteria, and configured project guidance. Before editing, capture the starting
`HEAD` as the review baseline, the initial tracked patch, and a comparable
content snapshot of each existing untracked text file. For sensitive, binary, or
large untracked files that cannot be snapshotted safely, record metadata and a
hash and treat any task modification as blocking automatic commit. Keep a record
of the task's own delta over that snapshot so pre-existing user work stays
outside later review and commit.

Before editing, read and follow the repository's applicable coding standards and
preserve its documented conventions throughout implementation.

Use `$tdd` where possible at seams already agreed in the Spec, Tickets, or
conversation. If no seam was agreed and adding tests requires a new public
boundary, confirm that boundary before writing the test.

Run typechecking regularly, single test files regularly, and the full test suite
once at the end.

Use `$project-documentation` to synchronize confirmed outcomes with existing
module guides and update the configured daily development record. Ask before
creating a new module guide.

Once implementation, tests, and documentation are current, use `$code-review`
with the captured baseline and source work. Include the in-scope staged,
unstaged, and untracked changes in the review set. Resolve review findings that
are within scope, rerun affected checks, and review again until no in-scope
blocking finding remains. Report out-of-scope findings instead of expanding the
implementation.

Stage and inspect only the task delta, then verify the staged diff before
committing it to the current branch. If pre-existing and task changes overlap in
the same hunk and cannot be separated safely, do not commit; report the exact
overlap and leave the working tree intact for the user.

Do not push or close tracker work unless the user also asks.

Report the delivered behavior, tests and checks run, documentation updated,
review outcome, commit identifier, and anything that still needs human
verification.
