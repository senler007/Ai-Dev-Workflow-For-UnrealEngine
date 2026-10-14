---
name: implement
description: Implement a piece of work based on a Spec or set of Tickets. Use only when the user explicitly asks to implement scoped work.
---

Implement the work described by the user in the Spec or Tickets. A Spec is
sufficient input — do not require `$to-tickets` first.

Use `$tdd` where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite
once at the end.

Use `$project-documentation` to synchronize confirmed outcomes with existing
module guides and update the daily development record only if configured.
Ask before creating a new module guide.

Once done, use `$code-review` to review the work.

Commit the work to the current branch.

Do not push or close tracker work unless the user also asks.
