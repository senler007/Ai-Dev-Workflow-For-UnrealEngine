English | [简体中文](README.zh-CN.md)

# Ai-Dev-Workflow-For-UnrealEngine

This is a streamlined AI collaboration workflow I put together during game development, and I plan to keep using it in future projects.
It mainly addresses two things:

1. Making document locations and responsibilities clear.
2. Keeping the development workflow consistent and reducing errors.

As a project grows, unclear documentation and an unclear process for turning requirements into features make it easy for AI to dump shit everywhere. These skills standardize where documents go, how requirements are clarified, how plans are made, and how finished work is checked, covering a simple UE project development pipeline.

## Installation and initialization

First, run this command:

```sh
npx --yes skills add senler007/Ai-Dev-Workflow-For-UnrealEngine --skill '*' --agent codex --global --copy --yes
```

Then open a new project in Codex and send this:

```text
Use $setup-senler-skills to initialize this project.
```

## Essential project documents for game development

A project needs clear documentation conventions, or things get painful later.
Use the following shared document structure with my skill set. All paths are relative to your own project root.

- `Docs/ProjectOverview.md`: Project introduction, core experience, document navigation, and other important references, such as Figma.
- `AGENTS.md`: Team working rules, development workflow, and rules for using skills.
- `README.md`: Repository overview, resource directories, naming, and asset management conventions.
- `CONTEXT.md`: Project terminology and its meanings.
- `Docs/Worldbuilding.md`: Worldbuilding (optional; generally for lore and other narrative material).
- `Docs/Modules/<feature>.md`: Design, responsibilities, implementation, and maintenance entry points for actual modules, created as features need them.

## From requirements to implementation

**Whatever the requirement, you only need to invoke one skill: use $grilling when you describe what you want. It will keep asking about the unclear parts of your requirements. You can use it for any feature to avoid rework or results you're unhappy with.** The other skills are invoked automatically; you don't need to invoke them yourself. If you're curious, here's what they do.

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
