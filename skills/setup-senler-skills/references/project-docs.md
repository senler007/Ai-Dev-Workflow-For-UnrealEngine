# Project document templates

These are structures to adapt, not files to copy blindly. Use the project's
language, paths, real facts, and existing authorities. Omit unknown or unused
sections; do not leave placeholders in generated output.

| Document role | Default for a new project | Content |
| --- | --- | --- |
| Work rules and map | AGENTS.md | Workflow triggers, authorities, project constraints, tool access |
| Repository guide | README.md | Actual startup/use, directories, naming and resource conventions |
| Project overview | Docs/ProjectOverview.md | Purpose, audience, experience, navigation and supplied links |
| Glossary | CONTEXT.md | Confirmed vocabulary and short meanings |
| World and characters | Docs/Worldbuilding.md | Supplied narrative facts, when applicable |
| Module guide | Docs/Modules/ModuleName.md | Confirmed behavior, responsibilities, maintenance and validation |

## Agent instructions

Suggested sections: project rules, workflow, document map, and actual tools.
Reference globally installed skills by name; do not copy them into the project.
Keep the process in the skill and project facts in the project. The workflow is
grilling -> ask-plan-build -> approved implementation -> verification/review ->
documentation when durable facts change. Existing answers and approvals carry
forward. State the actual source when project-local skills share a global name.

## Overview

Write a short factual introduction, intended experience or use, and navigation
to existing documents. Include real reference URLs only when supplied or found.
For Figma-enabled projects, identify the real file and task-page name; no borrowed
file IDs. Product goals, unfinished plans, and current behavior stay distinguishable.

## Module guide

For an authorized real module, describe its purpose and boundaries, confirmed
user-facing behavior, state/rule/presentation ownership, relevant code/assets,
common edit locations, and repeatable verification. Keep Architecture within the
same guide. Do not create a module guide before there is a real module to explain.

## Existing separate documentation map

When the repository already uses a map, preserve it instead of creating a second
authority in AGENTS.md. Relevant fields are:

- Language: the actual project language.
- Project overview: its real path.
- Glossary: its real path, or not maintained.
- Module documentation: the established directory or naming convention.
- Worldbuilding: its real path, when applicable.
- Development records: the explicitly configured path, or disabled.
- Tracker: the existing source, or the current user request and approvals.

One fact has one authoritative owner; other documents link to it. Do not add
daily records or ADR directories by default. Preserve explicit existing policies.
