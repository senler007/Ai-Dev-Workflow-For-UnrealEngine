---
name: grilling
description: Clarify new features and behavior changes before planning, or stress-test a design when requested. Reuse prior decisions; small explicit edits and approved implementation do not need another interview.
---

Model the unresolved design as a decision tree. In each round, ask a small group
of questions whose prerequisites are settled, with a recommendation and its
tradeoff for each. Let the answers determine the next round; do not ask dependent
questions together or reopen decisions without conflicting evidence.

Resolve discoverable facts from the project before asking the user. Focus on
choices that change the outcome, scope, or costly commitments. Finish when the
material decisions are resolved, not when every hypothetical branch is explored.

When the request already resolves those decisions, briefly consolidate the
intended effect, scope, acceptance criteria, and remaining dependencies without
inventing questions. For a request to build a feature, pass that summary directly
to `$ask-plan-build` in the same conversation. Its Ask input is already complete;
do not interview the user again. A discussion-only request ends with the summary.
When called by another explicitly selected workflow such as `$grill-with-docs`,
return the clarification to that workflow instead of starting implementation
planning.

If the user asks to preserve the design in project docs, read the relevant
existing authorities first. Keep the interview out of those files until the user
confirms a consolidated decision summary, then use `$project-documentation` to
write the confirmed decisions once. A revised summary needs confirmation of the
changed decisions.
