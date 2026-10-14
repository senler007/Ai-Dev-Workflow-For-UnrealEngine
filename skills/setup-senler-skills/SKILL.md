---
name: setup-senler-skills
description: Initialize or adapt a project to the globally installed Senler workflow, including project docs, grilling-to-plan routing, Unreal conventions, and Figma task coordination. Use when the user asks to set up this workflow in a new or existing project.
---

# Set up the whole workflow

This explicit setup request authorizes the project documentation and instruction
changes needed to adopt the workflow. Inspect first, preserve existing work,
then complete setup. Do not ask for approval again for the requested setup.
Ask only for missing product facts or an actual conflicting convention. This
skill does not implement a product feature, publish tracker work, activate
unrequested automations, or enroll unrelated chats.

## Discover the current project

Locate the real project root, applicable agent instructions, existing documents,
Git remote, language, engine/toolchain, and available tool connections. Reuse
existing names, directory casing, authorities, and user decisions. A blank
project may need its purpose and intended audience from the user; ask together
for the few unknowns that affect the initial documents. Do not infer a game's
world or features from its folder name.

All skills remain in the user's global installation. Resolve the installed
skill paths instead of copying skills into the project or hardcoding a machine
path. If a project already has same-name skills, inspect them and explicitly
select the intended source in its rules; preserve local customizations. Do not
silently delete them or assume that duplicate names are merged.

## Prepare project documents

Use [the document templates](references/project-docs.md). Existing owners take
precedence. Create only documents for which confirmed content exists:

- AGENTS.md: the workflow entry, document map, conventions, tool boundaries.
- README.md: actual project setup/use and resource or repository conventions.
- Docs/ProjectOverview.md: confirmed project purpose, experience, navigation,
  and supplied reference links, including Figma when available.
- CONTEXT.md: actual terms when a glossary is useful.
- Docs/Worldbuilding.md: supplied world and character facts for narrative projects.
- Docs/Modules/: the module-guide convention; create a guide only for a real
  established module, with explicit human confirmation of a new guide boundary.

Merge changed sections rather than replacing existing files. Do not create empty
files/directories, invented capabilities, or a standalone Architecture document.
Do not resurrect deliberately deleted documents or add a daily record unless
this project already requires one or the user requests it.

Keep the role map directly in AGENTS.md unless a separate map already exists.
Reuse an established tracker. Without one, current requests and approvals are
the scope authority; no issue service or local tracker needs to be created.
For explicitly requested tracked work without a destination, ask which tracker
and repository or local directory to use, then record the answer in the existing
map before returning to that workflow. Do not skip this choice by merely leaving
the tracker unconfigured. The existing references support
[GitHub](references/issue-tracker-github.md),
[local files](references/issue-tracker-local.md), and
[another service](references/issue-tracker-custom.md).

## Connect all installed skills

Merge these routing rules into the project's agent instructions:

1. New features and behavior changes start with `$grilling`. Inspect existing
   implementation first. Reuse existing answers; if clear, summarize without
   manufacturing questions.
2. `$ask-plan-build` consumes that summary, proposes concrete changes and
   validation, then implements the approved scope. Do not repeat Ask or approval.
   Small explicit edits and already approved implementation proceed directly.
3. Apply `$unreal-project` to Unreal work. Follow real engine versions, content
   ownership, and connected editor tools. Non-Unreal tasks do not activate it.
4. Review logic changes with `$code-review`, fix authorized findings, and verify
   affected behavior. Update stable facts with `$project-documentation`.
5. Use `$figma-task-steward` when the user enables Figma task management. Keep
   static reading and clarification parallel; coordinate shared writes, builds,
   tests, and editor actions serially. Do not enroll ordinary independent chats.
6. Preserve the installed `$grill-with-docs`, `$to-spec`, `$to-tickets`,
   `$implement`, and `$tdd` workflows for explicit use; publishing and committing
   remain governed by the selected workflow and the user's request.

## Resolve environment-dependent capabilities

Installation of the whole package is complete even when an external connector
has not been configured. Check only the capabilities the project will use and
report specific missing connections. Do not claim connected or enabled without
tool evidence, and do not stop unrelated setup for a missing connector.

For Unreal, record the actual engine and approved editor access. Shared defaults
live in `$unreal-project`; project-specific commands and asset roots stay here.
Do not import another project's custom close command, asset paths, or grants.

For Figma coordination, retain the real Figma link, task-page name, user timezone,
and any requested handover schedule in the project overview or existing config.
Confirm Figma access and Codex project/chat/message tools when activation is
requested. Register actual authorization for participating chats and board
updates. Do not copy another user's consent, ledger, thread IDs, or schedule.
An unavailable connection remains an explicit setup item; the rest proceeds.

## Verify and finish

Check generated paths and links, unresolved placeholders, duplicate authorities,
and the actual discoverability of each installed skill. Re-running setup must
reuse existing files and configuration rather than duplicate sections or reset
decisions. Report the actual files changed, chosen skill sources, working
capabilities, and concrete remaining setup. A subsequent new-feature request
should start with grilling and reach a concrete plan without a second interview.
