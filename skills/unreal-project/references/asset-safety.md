# Unreal asset and Git safety

Read for asset edits or Git operations that can overwrite .uasset, .umap, or
external actor/object packages. Ordinary text work and read-only Git queries do
not need an editor shutdown or an asset audit.

- Check only affected assets and real unsaved/uncommitted work. Editing in the
  approved scope proceeds normally; do not create whole-project backups or
  backup branches unless requested or required by an explicit project policy.
- Before external Git writes, reconcile editor save conflicts for those assets.
  Preserve user work; obtain a choice when an actual overwrite would discard it.
  Do not treat a dirty repository as blanket permission to reset.
- Resolve binary conflicts through the approved editor/version workflow, not
  line merges or blanket ours/theirs choices. Prefer existing Git versions as
  recovery sources; never assume a commit includes unsaved editor changes.
- Avoid broad reset/restore/clean operations and deletion of LFS recovery data.
  On failed recovery or merge, preserve the state and explain the actual failure
  instead of chaining destructive retries.
- Verify touched assets and expected behavior, including relevant external
  packages. Git success or an unchanged main map alone does not prove integrity.
