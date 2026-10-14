English | [简体中文](README.zh-CN.md)

# Senler Skills

This is an AI collaboration workflow I put together during game development, and I plan to keep using it in future projects.
As a project grows, if requirements and documentation don't have clearly defined responsibilities, AI tends to ask the same questions over and over and shit out documentation all over the place. These skills standardize where documents go, how requirements are clarified, how plans are made, and how finished work is checked, covering a complete UE project development pipeline.

## Installation and initialization

First, run this command:

```sh
npx --yes skills add senler007/Ai-Dev-Workflow --skill '*' --agent codex --global --copy --yes
```

Then open a new project in Codex and send this:

```text
Use $setup-senler-skills to initialize this project.
```

A project needs clear documentation conventions, or things get painful later. AI will dump shit everywhere, so I use a common structure for organizing documents here.

## Essential project documents for game development

Use the following document structure with this skill set. All paths are relative to your own project root.

- `Docs/ProjectOverview.md`: Project introduction, core experience, document navigation, and other important references, such as Figma.
- `AGENTS.md`: Team working rules, development workflow, and skill entry points.
- `README.md`: Repository overview, resource directories, naming, and asset management conventions.
- `CONTEXT.md`: Project terminology and its meanings.
- `Docs/Worldbuilding.md`: Worldbuilding (optional; generally for lore and other narrative material).
- `Docs/Modules/<feature>.md`: Design, responsibilities, implementation, and maintenance entry points for actual modules, created as features need them.

## From requirements to implementation

**Whatever the requirement, you only need to invoke one skill: use $grilling when you describe what you want. It will keep asking about the unclear parts of your requirements. Use it for anything a bit bigger to avoid rework.** The other skills are invoked automatically; you don't need to invoke them yourself.

| Skill | What it does |
| --- | --- |
| `setup-senler-skills` | Initialize project documents and the development workflow. |
| `grilling` | Clarify requirements, boundaries, and acceptance criteria. |
| `ask-plan-build` | Take the clarification results, make a plan, and implement after confirmation. |
| `unreal-project` | Set UE project rules for C++ and Blueprint responsibilities, resource organization, asset operations, and verification. |
| `code-review` | Check whether changes meet requirements and project rules. |
| `project-documentation` | Maintain project documents and keep them consistent with the implementation. |
| `figma-task-steward` | Manage Figma tasks, assign dedicated chats, run implementation tasks one at a time, and handle handoffs to reduce repeated coordination. |

**And finally, go be a badass, bro!**
