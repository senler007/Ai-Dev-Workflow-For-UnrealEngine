---
name: code-review
description: Review the changes since a fixed point (commit, branch, tag, or merge-base) along three axes — Standards, Spec, and Documentation — and report them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
---

Three-axis review of one fixed change set, including uncommitted work when that is the requested scope:

- **Standards** — does the code conform to this repo's documented coding standards?
- **Spec** — does the code faithfully implement the originating issue / PRD / spec?
- **Documentation** — do the changed behavior and code structure match their authoritative human-readable project documentation?

Run all three axes in the current conversation. Do not create sub-agents.

Read applicable AGENTS.md instructions and their documentation/tracker map. Use existing `docs/agents/issue-tracker.md` and `docs/agents/project-docs.md` when configured; their absence does not require setup or block review. The current user request and accepted plan can be the specification.

## Process

### 1. Pin the fixed change set

Honor the requested branch, PR, commit, or worktree scope. For delivery review,
review the current task's actual edits without asking the user to provide a ref.

- For committed branch work, resolve the supplied/default target branch, then
  capture `git diff <fixed-point>...HEAD` and
  `git log <fixed-point>..HEAD --oneline`.
- For worktree changes, capture `git diff HEAD` for staged and unstaged tracked
  changes, plus `git ls-files --others --exclude-standard` and the relevant
  untracked files. With no HEAD yet, inspect the initial index and new files.
- For a since-commit request, resolve that commit and compare its tree to the
  requested endpoint; do not silently change this into a merge-base comparison.

Record the resolved baseline, selected paths, and current file hashes or a
snapshot. Keep the same contents for every pass. Separate pre-existing unrelated
edits from this task. An invalid ref needs correction; an empty committed diff
must not hide worktree changes. Report no changes only after checking the full
requested scope. If files change during review, refresh affected findings.

### 2. Identify the spec source

Use the user's current request, accepted clarification/plan, and any supplied
Spec/Ticket or PR as the scope authority. Follow linked issues through the
project's actual tracker configuration; inspect matching local specifications
when useful. Ask only about material missing requirements. A separate issue or
specification file is not required. If no requirement evidence exists, report
that limitation on the Spec axis and continue the other passes.

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below — a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation — and, like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name** — a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code** — the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy** — a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps** — the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession** — a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches** — the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery** — one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change** — one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality** — abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains** — long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man** — a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest** — a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Identify the documentation sources

Read the configured map (AGENTS.md or an existing `docs/agents/project-docs.md`), `$project-documentation`, and the module guides or other authorities affected by the diff.

### 5. Run the three review passes

Use the same captured change set and requirement evidence for every pass.

**Standards pass:**

- Report — per file/hunk where relevant — (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk.
- Distinguish hard violations from judgement calls — documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline.
- Skip anything tooling enforces.

**Spec pass:**

- Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong.
- Cite the requirement or accepted user decision for each finding.

If the spec is missing, skip the Spec pass and note this in the final report.

**Documentation pass:**

- Report missing, incorrect, duplicated, or unapproved documentation changes.
- Cite the applicable project-documentation rule and file for each finding.

### 6. Aggregate

Present the three reports under `## Standards`, `## Spec`, and `## Documentation` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings — the three axes are deliberately separate (see _Why three axes_).

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes — that's the reranking the separation exists to prevent.

## Why three axes

A change can pass one axis and fail another:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**
- Code and behavior can both be correct while the human-readable project documentation is stale → **Standards and Spec pass, Documentation fail.**

Reporting them separately stops one axis from masking another.
