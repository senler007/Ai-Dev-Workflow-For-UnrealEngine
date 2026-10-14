---
name: unreal-project
description: Apply Unreal Engine project conventions to C++, Blueprint, gameplay, UI, audio, architecture, and asset work. Use asset-safety guidance for asset edits or Git writes affecting assets; ordinary documents and read-only Git queries do not need it.
---

# Unreal project conventions

Read applicable project instructions and only relevant module documents. Resolve
the actual engine version, content roots, resource conventions, and available
editor tools from this project; never reuse another project's machine paths,
custom commands, or permissions. Project-specific rules win.

## Requirements and reuse

New features and gameplay changes follow `$grilling`, then `$ask-plan-build`.
Reuse existing answers and approvals. Small explicit configuration/resource
changes and approved implementation proceed without another interview.

Inspect a comparable production implementation and its whole lifecycle: input,
state, interaction, presentation, audio, completion, interruption, death, and
departure cleanup. Reuse the complete public flow. Explain intentional
differences; extract only what the request needs. Verify the existing feature
as well as the new caller.

## Ownership and implementation

Identify public entry -> state owner -> rules/flow owner -> presentation owner
when adding state or changing cross-module responsibilities. Keep authoritative
state and rules separate from local visuals and sound. Public facades validate
and route rather than accumulating unrelated lifecycles. Use Unreal Subsystems,
Components, UObjects, and Actors according to real responsibilities.

Behavior belongs in C++ by default; Blueprint owns replaceable presentation and
design configuration. Keep model, material, animation, sound, transform, and
static visibility defaults in production Blueprint assets. C++ changes only the
fields required by runtime behavior; it must not overwrite art defaults during
initialization. Asset-axis or pivot corrections belong in the source/mesh asset.

Use serialized typed asset references, project data assets, and the project's
cooking/Asset Manager conventions. Do not hardcode or construct runtime resource
paths. Expose only properties with a concrete design purpose; keep internal
components/state private. Preserve an independent scene root when designers
need to adjust a presentation component's relative transform.

UI follows Designer Widget Blueprint -> feature controller -> gameplay API.
Widgets own layout, styling, animation, navigation, and displayed state;
controllers bind/unbind once and translate intent and view state; gameplay owns
network authority, travel, validation, and results. The local player/HUD assembles
these pieces and cleans them up. Do not rebuild designer UI in native code unless
the project explicitly uses that approach.

## Editor and assets

Use the project's approved Unreal MCP/editor integration for asset inspection,
creation, compilation, saving, and verification. Do not directly rewrite .uasset
or .umap binaries. If the required integration is unavailable, finish independent
text work and identify the exact editor operations still unverified.

Inspect actual object paths, classes, and properties before writing. Configure
Blueprint defaults on the generated-class CDO. Treat create/duplicate, compile,
verify, and save as separate outcomes; do not hide failed steps in a successful
batch. On generated-class/skeleton internal errors, stop retrying the damaged
object and recover through a normal editor restart after preserving valid work.

Coordinate only actual shared-workspace or editor conflicts. Static reads do not
need exclusive access. Never kill the user's editor or discard unsaved assets to
make a build pass. Use the project's verified graceful-close procedure if a
restart/build requires it; do not invent a project-specific command.

For asset edits and Git writes affecting assets, read
[asset safety](references/asset-safety.md). Normal text edits do not require
closing the editor or creating asset backups.

## Verification and documentation

Use risk-matched verification of real interaction paths, cleanup, and necessary
host/client perspectives. For UI/input work, include clicking, focus, and restored
game input. Reproduce a bug before fixing it, then rerun that scenario and the
affected original behavior. Stop expanding checks after sufficient verification
unless new changes, failures, or unresolved risks justify it.

Use `$code-review` for logic changes and `$project-documentation` for changed
stable behavior or maintenance entry points. Keep responsibilities and edit
locations together in module guides. Report what was actually checked and which
editor or manual checks remain; compilation alone is not feature acceptance.
