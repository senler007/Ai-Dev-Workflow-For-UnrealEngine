---
name: fix-bug
description: Fix software defects through a reproducible signal, falsifiable diagnosis, and a minimal verified patch. Use when the user asks to fix or correct a bug; do not use for feature work, broad refactoring, code review, or diagnosis-only requests.
---

# Fix Bugs from Evidence

Restore the expected behavior instead of hiding the symptom. A request to fix a
bug authorizes changes within that defect's scope; it does not authorize feature
work, broad cleanup, or unrelated refactoring.

## Establish the target and baseline

- State one observable acceptance result: what should happen, what happens now,
  and how the result will be checked.
- Read the relevant project guidance and inspect the current worktree before
  editing. Preserve unrelated and pre-existing user changes.
- Capture the starting `HEAD`, initial tracked patch, and untracked-file snapshot
  for the later `$code-review`. A bug-fix request does not itself authorize a Git
  commit; commit only when separately requested or when another invoked workflow
  explicitly includes it.
- Redact credentials, tokens, personal data, and authentication headers before
  showing or persisting commands, logs, traces, screenshots, or fixtures.

## Build a red-capable feedback loop

Reproduce the exact reported symptom before patching. Prefer, in order, a failing
test at the real seam, a deterministic command or request, a headless interaction,
a trace replay, or a small throwaway harness. Tighten the loop until it is fast,
repeatable, and specific enough to distinguish this defect from nearby failures.

Minimize the reproduction one input, caller, configuration value, or step at a
time. Keep a removal only when the same symptom still occurs. The loop is ready
when every remaining element is load-bearing and one already-run command can
show the red result.

If no red-capable loop can be built, report what was tried and request the
smallest missing access or redacted artifact. Do not turn source inspection alone
into a claimed root cause or speculative production patch.

## Rank and test hypotheses

Generate three to five ranked, falsifiable hypotheses. Each must predict an
observation that would distinguish it from the others. Show the list briefly;
continue with the strongest evidence-backed ranking unless the user supplies
domain information that changes it.

Treat each diagnostic edit as one experiment. Change one variable at a time and
tie every probe to a prediction. When evidence disproves a hypothesis, undo only
that experiment's edits, update the ranking, and collect distinguishing evidence
before editing the same point again. Never stack delays, retries, fallback
writes, or resets onto an unproven theory.

## Find the first divergence

Trace the value, event, or state across the complete path that produces the
symptom. Add narrow, temporary instrumentation at the relevant boundaries, such
as:

1. input or trigger receipt;
2. state before and after mutation;
3. selection, routing, or ownership changes;
4. confirmation, commit, or persistence;
5. object creation, I/O, or external handoff;
6. lifecycle callbacks and final observable output.

Include stable identifiers and ordering information when concurrent actors or
rapid recreation could make separate events look like one. At each checkpoint,
compare expected and actual values. Locate the earliest checkpoint where they
diverge; later wrong values are consequences until evidence proves otherwise.

Use the trace to say which hypotheses were eliminated and why. Prefer a short
evidence chain over large volumes of undirected logging. Tag temporary probes so
they can be found and removed deterministically.

## Fix the earliest wrong source

- Correct the control flow, state transition, ownership, or data source at the
  first confirmed divergence.
- Prefer the smallest change that removes the root cause and preserves intended
  behavior around it.
- Do not use a delay, retry, duplicate write, reset, guard, or broad fallback as
  the final fix unless evidence shows that mechanism is the intended behavior.
- Keep diagnostic changes separate from the production fix so temporary
  instrumentation can be removed cleanly.

## Lock in and verify the repair

Use `$tdd` when available to turn the minimized reproduction into a regression
test at an agreed stable public seam. The test must fail for the observed defect
before the repair and pass afterward without encoding implementation details. If
no correct seam can reproduce the real pattern, report that architectural gap
instead of adding a misleading shallow test.

Verify in proportion to the defect:

- rerun the original reproduction path;
- run the focused regression test and nearby tests;
- run relevant typechecking, linting, or build validation;
- run the full test suite once when practical;
- remove temporary logs, probes, and disproved edits.

Do not claim the bug is fixed unless the acceptance result was observed. If the
environment prevents the final check, report exactly what was verified and what
still needs human reproduction.

When the project has configured human-readable documentation, use
`$project-documentation` to synchronize confirmed behavior and the development
record. Then use `$code-review` against the captured baseline and the complete
in-scope worktree change set. Resolve in-scope blocking findings and rerun the
affected checks, then review the resulting change set again until no in-scope
blocking finding remains. Report out-of-scope findings separately.

Report the observable symptom, confirmed root cause, first bad checkpoint,
minimal repair, regression coverage, validation performed, and any remaining
uncertainty.
