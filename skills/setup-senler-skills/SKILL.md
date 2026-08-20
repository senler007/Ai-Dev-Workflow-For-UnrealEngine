---
name: setup-senler-skills
description: Configure a repository for the Senler workflow, including GitHub, GitLab, local, or custom tracking and project-documentation paths. Use only when the user explicitly asks for setup or reconfiguration.
---

# Setup Senler Skills

Configure the repository once without replacing conventions that already work.
This skill is explicit-only: never run it merely because another workflow skill
is being used.

## Inspect the repository

Read only enough context to locate:

- the repository root and Git remote;
- existing agent instruction files such as `AGENTS.md` or `CLAUDE.md`;
- existing project overview, glossary, module guides, ADR, and tracker documentation;
- any existing daily development-record convention;
- the established documentation directory casing and project language.

Existing paths, casing, terminology, and language take precedence over the
defaults in this skill. Do not create parallel files for roles that already have
an authoritative owner.

## Confirm the configuration

Summarize what was found, then confirm choices that cannot be inferred safely:

1. **Tracker mode.** Recommend GitHub or GitLab when the Git remote identifies
   that host; otherwise recommend local. Also support a custom tracker.
2. **Agent instruction file.** Update an existing instruction file. If none
   exists, ask before creating one and recommend `AGENTS.md` for Codex-first use.
3. **Project-document locations.** Reuse existing owners. For missing roles,
   propose a project overview, glossary, module-guide directory or naming
   convention, and ADR directory, adapting names and casing to the repository.
   Module guides co-locate Design, Architecture, and Maintenance Map sections;
   do not propose a standalone Architecture document.
4. **Development record.** Reuse an existing dated task journal. When none exists,
   propose `docs/DevelopmentRecord/YYYY-MM-DD.md`, adapting directory casing to
   the repository.
5. **Document language.** Infer it from durable project documentation and ask
   only when mixed usage leaves the answer ambiguous.

Show the exact files and substantive configuration before writing, then wait for
the user's explicit approval. Do not create empty project, glossary, module-guide,
or ADR documents during setup.

## Write the configuration

Use the applicable tracker reference:

- GitHub: [references/issue-tracker-github.md](references/issue-tracker-github.md)
- GitLab: [references/issue-tracker-gitlab.md](references/issue-tracker-gitlab.md)
- Local: [references/issue-tracker-local.md](references/issue-tracker-local.md)
- Custom: [references/issue-tracker-custom.md](references/issue-tracker-custom.md)

Create or update two small agent-facing configuration files in the repository's
existing agent-documentation directory. Prefer `docs/agents/` only when the
repository has no established location:

- `issue-tracker.md`, based on the selected tracker reference;
- `project-docs.md`, based on
  [references/project-docs.md](references/project-docs.md).

Add a concise `## Senler skills` section to the confirmed agent instruction file.
It should tell future agents where those two configurations live and to follow
them, including the configured daily development record. Merge with an existing
section instead of duplicating it.

Record actual repository-specific values, not unresolved placeholders. Avoid
copying the detailed document-role rules into multiple files; the configuration
should map roles to paths and defer maintenance behavior to
`$project-documentation`.

Re-read the written maps and agent-instruction section. Confirm that every path
is discoverable from the agent instructions, no unresolved repository-specific
placeholder remains, the chosen tracker has explicit ready/done states, and
rerunning setup would update the same blocks rather than create duplicates.
Documented runtime variables such as `<feature>` and `<ticket>` may remain when
the downstream workflow supplies them for each piece of work.

## Finish

Use `$project-documentation` to record the completed setup in the configured
development record.

Report the tracker mode, configuration files, instruction file, document
language, development-record path, reused authorities, and proposed-but-uncreated
module-guide convention. Call out any ambiguity left for the user. Do not start
a Spec or create tracker work as a side effect of setup.
