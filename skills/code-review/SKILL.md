---
name: code-review
description: Review committed or work-in-progress changes from a fixed baseline along three independent axes — Standards, Spec, and Documentation. Use for branches, PRs, uncommitted work, or requests to "review since X".
---

Three-axis review of one shared change set between a fixed baseline and the
current repository snapshot:

- **Standards** — does the code conform to this repo's documented coding standards?
- **Spec** — does the code faithfully implement the originating issue / PRD / spec?
- **Documentation** — do the changed behavior and code structure match their authoritative human-readable project documentation?

Run all three axes in the current conversation. Do not create sub-agents. This
skill is read-only: report findings, but do not edit files.

Locate the issue-tracker and project-documentation maps through the repository's
agent instructions. Do not assume they live under `docs/agents/`. If the maps
are missing, tell the user to explicitly run `$setup-senler-skills`; do not run
that explicit-only workflow on their behalf.

## Process

### 1. Pin the baseline

Use the fixed point supplied by the user or calling workflow: a commit SHA,
branch, tag, `main`, `HEAD~5`, or a captured starting `HEAD`. If neither supplied
one, ask for it.

Confirm it resolves with `git rev-parse <fixed-point>`. Also capture the commit
list with `git log <fixed-point>..HEAD --oneline`.

### 2. Freeze the shared change set

Capture every in-scope state source before any review pass:

- committed branch changes: `git diff <fixed-point>...HEAD`;
- staged and unstaged tracked changes over `HEAD`: `git diff HEAD`;
- untracked paths: `git ls-files --others --exclude-standard`, followed by the
  relevant contents or binary metadata for each in-scope path.

Treat the worktree diff as an overlay on the committed diff. When a calling
workflow captured an initial dirty-state patch or untracked-file snapshot,
compare against it and review only the task delta — do not exclude an entire path
merely because it already had changes. If same-hunk overlap cannot be separated
reliably, flag the overlap as blocking. Record the commands, commit list, and
untracked-path list once; all three axes must review this same frozen change set.
Only report "empty diff" when every source above is empty.

### 3. Identify the spec source

Look for the originating spec, in this order:

1. Source work supplied by the calling workflow or user: paths, URLs,
   identifiers, or inline bodies. For multiple Tickets, include their parent Spec;
   for `$fix-bug`, use the stated acceptance result as the behavior contract.
2. Issue references in commit messages (`#123`, `Closes #45`, GitLab `!67`, etc.)
   — fetch via the configured issue-tracker map.
3. A PRD/spec file under `docs/`, `specs/`, or `.scratch/` matching the branch name or feature.
4. If nothing is found, ask the user where the spec is. If they say there isn't one, skip the **Spec** axis and report "no spec available".

### 4. Identify the standards sources

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

### 5. Identify the documentation sources

Read the configured project-documentation map, `$project-documentation`, and the
module guides or other documentation authorities affected by the change set.

### 6. Run the three review passes

Use the same frozen change set and commit list for every pass.

**Standards pass:**

- Report — per file/hunk where relevant — (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk.
- Distinguish hard violations from judgement calls — documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline.
- Skip anything tooling enforces.

**Spec pass:**

- Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong.
- Quote the spec line for each finding.

If the spec is missing, skip the Spec pass and note this in the final report.

**Documentation pass:**

- Report missing, incorrect, duplicated, or unapproved documentation changes.
- Cite the applicable project-documentation rule and file for each finding.

Label every finding **blocking** or **advisory** within its own axis. Documented
standards breaches, Spec mismatches or omissions, unsafe change-set overlap, and
missing synchronization with an authoritative project document are blocking by
default. Fowler smell heuristics are advisory by default. Use evidence to justify
exceptions; classification does not merge or rank findings across axes.

### 7. Aggregate

Present the three reports under `## Standards`, `## Spec`, and `## Documentation` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings — the three axes are deliberately separate (see _Why three axes_).

End with a one-line summary: blocking and advisory totals per axis, and the worst
issue _within each axis_ (if any). Don't pick a single winner across axes — that's
the reranking the separation exists to prevent.

## Why three axes

A change can pass one axis and fail another:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**
- Code and behavior can both be correct while the human-readable project documentation is stale → **Standards and Spec pass, Documentation fail.**

Reporting them separately stops one axis from masking another.
