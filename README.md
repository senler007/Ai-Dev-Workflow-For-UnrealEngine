English | [简体中文](README.zh-CN.md)

# Senler Skills

Six skills based on the current local versions. New features and behavior
changes follow `grilling` -> `ask-plan-build` -> approved implementation,
verification, review, and updates to changed durable documentation. Reuse settled
answers and approvals; clear small edits proceed directly.

| Skill | Purpose |
| --- | --- |
| `setup-senler-skills` | Initialize a project with the fixed document structure and current local skills. |
| `grilling` | Clarify consequential decisions and consolidate outcomes, boundaries, and acceptance. |
| `ask-plan-build` | Consume the clarified requirements, propose concrete changes, and implement after approval. |
| `unreal-project` | Apply Unreal ownership, C++/Blueprint, UI, asset, and verification rules. |
| `code-review` | Review one complete change set against conventions, requirements, and documentation. |
| `project-documentation` | Maintain confirmed facts under the mandatory document structure. |

## Install everything with one command

Install Node.js 22.20 or newer and Git, then run:

```sh
npx --yes skills add senler007/skills --skill '*' --agent codex --global --copy --yes
```

This installs all six current packages globally for Codex, shared across projects.
GitHub is the distribution source; Codex reads the installed local files. Projects
do not need their own copies. The command updates matching global skills, so
preserve unpublished local edits first. It does not uninstall previously installed
packages that have since been removed from this repository; remove obsolete skills
you no longer use separately.

## Initialize a new project

After the global installation above, open the target project in Codex
and send:

```text
Use $setup-senler-skills to initialize this project.
```

Provide its name, purpose, and core experience in the same message when known.
The initializer creates AGENTS.md, README.md, CONTEXT.md, and
Docs/ProjectOverview.md at the fixed locations, using confirmed project facts.
It configures grilling -> ask-plan-build -> approved implementation. It asks
only for necessary missing facts, preserves existing documents, and avoids
duplicate rules on repeat runs. Worldbuilding and module guides follow the
conditions below. It uses the currently installed local skills without fetching
an older remote version. It does not create an engine project or connect Figma.
Reopen the project conversation, or restart Codex if needed, to refresh a newly
installed entry point.

## Required project documents

These paths and responsibilities are part of the workflow contract. Do not
search for or adapt to alternative document layouts. Paths are relative to the
working project's root, never to the global skill installation directory.

| Document | Responsibility |
| --- | --- |
| `AGENTS.md` | Team rules, workflow, skill entry points, project constraints, and actual tool commands |
| `README.md` | Startup, resource directories, naming, and asset version/temporary backup rules |
| `CONTEXT.md` | Project terms and meanings |
| `Docs/ProjectOverview.md` | Project identity, core experience, document navigation, and reference links |
| `Docs/Worldbuilding.md` | World and character facts; optional |
| `Docs/Modules/<feature>.md` | Module behavior, design, ownership, implementation, maintenance, and stable validation |

The first four files are required. Create module guides for real modules and
worldbuilding when needed. Populate missing required documents with confirmed
facts at these locations; ask for unknown facts without inventing content or
creating empty placeholders. Read-only tasks report missing documents without
writing them. Do not generate daily journals, standalone architecture documents,
or restore deleted configuration. The maintenance authority is
[project-documentation](skills/project-documentation/SKILL.md).

## Use

Install all six complete directories under `skills/` into your agent's skill
directory; they can be shared globally. Include their existing references and
metadata. Keep consumer-project documents in each project. This repository's
root AGENTS.md governs skill maintenance, not the consumer project's workflow.

Examples:

- `Use $grilling to clarify this feature and pass the outcome to ask-plan-build.`
- `Use $ask-plan-build to propose changes from our confirmed requirements.`
- `Use $code-review to inspect this task's uncommitted changes.`
- `Use $project-documentation to update the confirmed feature documentation.`

Use `unreal-project` only for Unreal work. Record actual content roots and
resource-table names in the project's README.md. Record the engine version,
normal editor-close command, and verification commands in its AGENTS.md. Never
assume a project includes a particular asset, script, or custom tool. Preserve
version-specific failure guidance and apply it under its stated conditions.

The workflow does not automatically commit or push. Publication, cross-chat
messages, and task coordination require the user's applicable authorization.

## Credit

Derived from Matt Pocock's AIHero skills and independently maintained by senler007
under the [MIT license](LICENSE).
