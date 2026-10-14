English | [简体中文](README.zh-CN.md)

# Senler Skills

An AI collaboration workflow I put together while developing a game, and intend to reuse in future projects.
As a project grows, unclear requirements and scattered documents lead to repeated questions and rework. These skills give documentation, clarification, planning, implementation, and review a shared structure.

## Install and initialize

With Node.js 22.20+ and Git installed, one command installs all seven skills:

```sh
npx --yes skills add senler007/Ai-Dev-Workflow --skill '*' --agent codex --global --copy --yes
```

Install globally once and share the skills across projects, without project-local copies. Updates replace matching skills, so preserve your own edits first.

Open a new project in Codex and send this, together with its name, purpose, and core experience:

```text
Use $setup-senler-skills to initialize this project.
```

It creates project documents and workflow rules, preserving and completing existing content. When joining a project that already uses this workflow, install the skills, sync the latest project files, and start a new Codex conversation. No reinitialization is needed.

## Project documents

This skill set uses the following fixed structure. All paths are relative to your project root.

- `Docs/ProjectOverview.md`: Project introduction, core experience, document navigation, and references such as Figma.
- `AGENTS.md`: Team rules, workflow, skill entry points, and project-specific commands.
- `README.md`: How to run the project, resource directories, naming, and asset management.
- `CONTEXT.md`: Project terminology and definitions.
- `Docs/Worldbuilding.md`: World and character information, when needed.
- `Docs/Modules/<feature>.md`: Design, responsibilities, implementation, and maintenance for actual modules, created as needed.

Maintain each fact in one place. See [project-documentation](skills/project-documentation/SKILL.md) for the detailed rules.

## Working on a feature

**Start a new feature with `$grilling` to clarify the requirements.** It asks about real uncertainties to reduce rework. When the requirements are already clear, it summarizes them without inventing more questions.

`ask-plan-build` then uses those answers to propose concrete changes and implements them after approval. Review the changes and update affected documentation before finishing. Reuse existing answers and approvals; clear small edits proceed directly.

| Skill | What it does |
| --- | --- |
| `setup-senler-skills` | Initialize project documents and workflow rules. |
| `grilling` | Clarify requirements, boundaries, and acceptance criteria. |
| `ask-plan-build` | Turn clarified requirements into a plan and implement after approval. |
| `unreal-project` | Apply UE rules for C++/Blueprint responsibilities, resources, asset operations, and verification. |
| `code-review` | Check changes against requirements and project rules. |
| `project-documentation` | Keep project documentation consistent with implementation. |
| `figma-task-steward` | Coordinate Figma tasks through dedicated chats, serialized implementation, and handoffs. |

You do not need to name every skill each time; use them according to project rules and task needs. UE rules apply only to UE projects. To use the Figma steward, connect Figma tools, have Python 3 available, and record the file in Docs/ProjectOverview.md. Then ask:

```text
Use $figma-task-steward to manage this project's Figma daily tasks, create dedicated task chats, and coordinate execution.
```

Installation does not start a steward or create a schedule. Keep project coordination authorization and handoff arrangements in AGENTS.md.

---

Inspired by Matt Pocock's AIHero Skills and independently maintained by senler007 under the [MIT license](LICENSE).
