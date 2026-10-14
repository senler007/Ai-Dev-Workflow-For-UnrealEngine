# Repository guidance

- Keep skill source in English and generated project documents in the configured project language.
  Exception: preserve the author's Chinese source for `figma-task-steward`.
- Keep `SKILL.md` frontmatter limited to `name` and `description`.
- Preserve Matt Pocock's upstream package layout for derived Skills. Use
  `references/` only for Senler-specific material; do not add per-skill README files.
- Validate every changed skill with the bundled skill validator and run repository tests.
- Preserve the MIT attribution to Matt Pocock and senler007.
- Treat this repository as an independent derivative; do not assume upstream synchronization.

## Upstream behavior

The complete package is installed globally. Project setup reuses existing
project documents and records routing in the project's own AGENTS.md.
New features use `grilling` -> `ask-plan-build` -> approved implementation;
clear small edits and approved plans do not repeat clarification or approval.
Unreal conventions, review, and documentation apply when relevant. Figma
coordination requires the current user's actual activation and permissions.
Keep all existing explicit Spec/Ticket workflows available; they are not
mandatory stages of the default feature workflow. Never export one project's
paths, account links, runtime ledger, schedule, or authorization as defaults.
The upstream-baseline rules below apply to the retained derived workflows.

- Treat Matt Pocock's current Skill as the behavioral baseline for every derived
  workflow Skill.
- Do not add confirmation gates, stop conditions, orchestration, scope tests, or
  publication prompts unless the user explicitly approves that difference.
- The approved Senler differences are: Senler naming and Codex metadata;
  human-readable module guides managed by `$project-documentation`; no standalone
  Architecture document; the lightweight four-part Spec; human-selected workflow
  stages; no sub-agents; `$grill-with-docs` defers all documentation writes until
  the user confirms the final consolidated decisions; and explicit workflow
  invocation as authorization for the publication that workflow describes.

## Senler skills

Before using a Senler workflow Skill, read and follow
`docs/agents/issue-tracker.md` and `docs/agents/project-docs.md`. Use
`$project-documentation` for durable ownership and the configured development
record.
