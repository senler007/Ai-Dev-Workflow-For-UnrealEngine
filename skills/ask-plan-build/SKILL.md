---
name: ask-plan-build
description: Turn clarified feature requirements into a concrete implementation plan and carry it out after approval. Use after grilling or when the user requests a plan; reuse existing answers and approvals.
---

## Ask

Use the outcome from `$grilling` as the Ask input. If a new feature or behavior
change reaches this skill without clarification, run `$grilling` first. Reuse
the conversation's settled effects, boundaries, acceptance criteria, and
delegated choices; do not start a second interview. Already approved plans go
directly to Build. Ask only about a newly discovered material gap, limited to
the affected scope, and continue independent investigation while awaiting it.

## Propose

Synthesize the answers into your own recommended solution: intended behavior,
key choices, implementation steps, and verification. State assumptions for
delegated choices. Inspect the relevant implementation before proposing changes
so the user can review a concrete change list, not just broad goals such as
"refactor the weapon" or "adjust animations."

Include the following detail where it applies:

- **Files and assets:** List the specific paths to create, modify, move, rename,
  or delete. For each, explain what changes, why it is needed, and the resulting
  behavior. Related files may be grouped only if each path and its role remain
  clear. Include configuration, references, and documentation affected by the
  change, not only source code.
- **Implementation:** Identify the relevant classes, functions, components, or
  data fields and explain how their responsibilities or interactions change.
  Describe meaningful before/after behavior and the order of dependent steps.
- **Animations and other content:** Name the actual assets and paths involved,
  including assets whose use changes without editing the asset itself. For
  animation work, explain which motions change and how: reuse or replacement,
  playback triggers, sequencing, blending, timing, notifies, slots, or bindings,
  as relevant. Distinguish editing animation content from changing the code or
  Blueprint that plays it. For example, a weapon refactor should identify the
  affected equip, fire, or reload animations and their planned changes when
  those motions are in scope.
- **Verification:** Connect checks to the proposed behavior, including visible
  or interactive outcomes for animation and UI changes. Identify any required
  manual verification or unavailable validation.

Use enough detail for the user to understand what they are agreeing to without
reading the implementation. Scale the explanation to the task; do not add
unrelated changes or boilerplate categories. Do not invent asset names, paths,
or parameter values. Mark unresolved details explicitly, explain how they will
be determined, and distinguish confirmed targets from conditional changes.

Present the plan and wait for the user's response before implementing.

## Build

After approval, incorporate actionable corrections and implement the plan
without another confirmation. If the user instead rejects the plan, asks a
question or requests a rewritten proposal, or postpones implementation, address
that request and remain at the proposal stage until they respond again.

Complete the implementation and relevant validation. Use `$code-review` on the
task's changes, correct findings within the approved scope, and verify affected
behavior. Use `$project-documentation` when stable behavior or maintenance
entry points changed. Report actual results and remaining checks. Do not commit,
push, or publish unless requested or explicitly required by the invoked workflow.
