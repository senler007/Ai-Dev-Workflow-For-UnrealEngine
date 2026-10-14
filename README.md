English | [简体中文](README.zh-CN.md)

# Senler Skills

A complete, globally installed workflow for project setup, requirements,
implementation, Unreal development, review, documentation, and Figma task
coordination. Install all 12 skills once, then initialize each project with one
prompt. Project facts stay in the project; reusable instructions stay global.

## Set and Use

With Node.js/npm and Git installed, run:

```bash
npx --yes skills add senler007/skills --skill '*' --agent codex --global --copy --yes
```

This uses the [Skills CLI](https://github.com/vercel-labs/skills) to install every
skill in this repository for Codex, globally, including references and scripts.
`--copy` avoids symlinks. The command updates same-name installed packages; keep
personal edits separately. It does not modify a project or connect accounts.
If skills are not listed, restart Codex. See the [Chinese setup guide](docs/INSTALL.zh-CN.md).

Open a new or existing project in Codex and send:

```text
Use $setup-senler-skills to initialize this project with all globally installed
Senler skills. Reuse existing documents and conventions, and configure the
project's workflow and document map.
```

Setup inspects the project, asks only for missing facts, and merges the required
rules into its AGENTS.md. It does not copy skills into each project. It preserves
local customizations and identifies same-name local/global conflicts. Re-running
setup updates existing sections instead of resetting them.

The document map covers AGENTS.md, README.md, Docs/ProjectOverview.md, CONTEXT.md,
Docs/Worldbuilding.md and established module guides. Only create documents with
real confirmed content; worldbuilding is optional. Keep existing paths when the
project uses another layout. No mandatory empty files, daily journal, or tracker.

## Workflow

For new features and behavior changes:

```text
Read project facts -> grilling -> ask-plan-build -> approve the plan
                   -> implement and verify -> code-review -> update stable docs
```

`grilling` resolves consequential decisions; `ask-plan-build` consumes those
answers without a second interview. Clear requirements need only a brief
consolidation. Small explicit changes and already approved plans proceed
directly. Unreal work also applies `unreal-project`.

Example:

```text
Use $grilling to add saved character appearance presets to this project.
```

After clarification, Codex presents a concrete plan through `ask-plan-build`.
After your approval it implements, verifies, reviews, and updates changed facts.
A design-only discussion does not automatically become implementation.

All older Spec/Ticket skills are also installed. Use only the stages your change needs when you explicitly choose that workflow: `grill-with-docs` records
confirmed design, `to-spec` creates change scope, `to-tickets` provides optional
slicing, and `implement` works directly with a Spec or Tickets. Their explicit
invocation governs their documented publication/commit behavior; the default
feature workflow does not silently create issues or commits.

## What Each Skill Does

| Skill | Role |
| --- | --- |
| [setup-senler-skills](skills/setup-senler-skills/SKILL.md) | Initialize or adapt a project's document map and workflow. |
| [grilling](skills/grilling/SKILL.md) | Clarify requirements in decision dependency order. |
| [ask-plan-build](skills/ask-plan-build/SKILL.md) | Turn those answers into a plan and implement after approval. |
| [unreal-project](skills/unreal-project/SKILL.md) | Apply Unreal code, Blueprint, UI, asset, and verification conventions. |
| [code-review](skills/code-review/SKILL.md) | Review Standards, Spec, and Documentation, including uncommitted work. |
| [project-documentation](skills/project-documentation/SKILL.md) | Maintain confirmed project facts and module guides. |
| [figma-task-steward](skills/figma-task-steward/SKILL.md) | Dispatch task chats, coordinate shared writes, and preserve handovers. |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Clarify a design, then persist its confirmed decisions. |
| [to-spec](skills/to-spec/SKILL.md) | Create a compact specification for one change. |
| [to-tickets](skills/to-tickets/SKILL.md) | Split a specification into deliverable slices. |
| [implement](skills/implement/SKILL.md) | Execute an explicitly selected Spec/Ticket workflow. |
| [tdd](skills/tdd/SKILL.md) | Develop through behavioral tests at public seams. |

Installation includes all of them. Invocation follows the task and project
rules; installing a skill does not force every task through every skill.

Figma coordination additionally uses a connected Figma plugin, Codex desktop
project/chat tools, and Python 3.8+ for its bundled ledger. Configure your own
Figma link and explicitly enable coordination. Automatic daily handover needs a
user-requested schedule. Unreal asset work needs the project's working editor
integration. Setup reports missing capabilities without blocking unrelated work.
No personal project data, credentials, ledger, or account authorization is bundled.

Run the same install command to update all skills. It updates global instructions;
it does not rewrite existing project documents. Run setup in a project to adapt
its rules when needed. Preserve the Figma runtime ledger outside the package.

## Credit

Inspired by Matt Pocock's AIHero Skills workflow. MIT licensed and independently
maintained by senler007; no automatic upstream synchronization. See [LICENSE](LICENSE).
