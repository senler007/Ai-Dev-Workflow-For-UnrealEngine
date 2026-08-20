---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, then write the final confirmed decisions into human-readable project documentation in one pass. Use when the user explicitly asks to grill a feature, system, lifecycle, or design with project docs.
---

Run a `$grilling` session, using the `$project-documentation` skill.

Locate the project-documentation map through the repository's agent instructions
and read the relevant existing authorities before interviewing. Use them to
resolve facts and avoid reopening decisions the project already owns. If the map
is missing, tell the user to explicitly run `$setup-senler-skills`; do not run
setup on their behalf.

Do not edit project documentation while the interview is in progress. Treat each answer as input to the evolving design, not as permission to persist that answer.

Once every decision branch is resolved, present one concise consolidated summary
of the proposed durable decisions and ask the user to confirm that final summary.
Only after explicit final confirmation, write those decisions into the appropriate
existing module guides in one documentation pass and update the configured daily
development record once. If the user revises the summary, continue the interview
and do not write yet.

Ask before creating a new module guide.
