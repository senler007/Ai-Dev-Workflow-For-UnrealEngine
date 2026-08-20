---
name: project-documentation
description: Maintain authoritative human-readable module guides and the configured daily development record. Use when confirmed behavior, terminology, code ownership, data flow, assets, configuration, ADRs, or tracker outcomes need routing or updating; when code and documentation disagree; or after a task changes the project.
---

# Project Documentation

Keep durable project knowledge readable by people and useful to maintainers. A
module guide explains both what a module does and where its implementation can be
changed. The development record remains a concise dated account of completed
work, not another source of project truth.

## Load the project's map

Find the project-documentation configuration named by the repository's agent
instructions. It must map the project's authorities and development-record path.
If either is missing, tell the user to explicitly run `$setup-senler-skills`;
do not run that explicit-only workflow on their behalf or silently impose
default paths.

Read only the configuration and candidate authorities needed for the current
fact. Follow established casing, language, terminology, and style. Read
[references/document-roles.md](references/document-roles.md) when ownership is
unclear. Read
[references/module-guide-structure.md](references/module-guide-structure.md)
whenever creating or materially updating a module guide.

## Decide whether the fact is durable

Write durable documentation only when information is confirmed and will help a
future human understand or maintain the project. Typical durable facts include
accepted behavior, canonical terminology, stable code or runtime responsibility,
asset and configuration wiring, and architectural decisions with meaningful
tradeoffs.

Do not persist:

- tentative ideas or unresolved alternatives;
- ticket progress, current test output, commit or release status in module guides;
- information already owned authoritatively elsewhere;
- documentation changes during a read-only request.

When confirmation is unclear, summarize the candidate fact and ask before
writing it.

## Keep module knowledge together

Use one module guide as the human-readable front door for each large or
independently understandable module. When applicable, the same guide contains:

- an overview and the module's product boundaries;
- a **Design section** for confirmed user-visible flows and rules;
- an **Architecture section** for current code responsibilities, state ownership,
  data flow, assets, configuration, and integration seams;
- a Maintenance Map, common change recipes, and stable validation procedures.

Architecture is a section of the module guide, not a standalone document. A
small related rule belongs in an existing guide rather than a new file. Do not
add empty headings merely to match a template.

Update an existing module guide in the same task when implementation or confirmed
design materially changes it. Creating a new module guide establishes a new
long-lived module boundary and therefore always requires explicit human
confirmation before writing the file. Do not create placeholders.

## Keep one authority per fact

Route each durable fact to one owner:

- project identity and navigation -> project overview;
- canonical term and terse meaning -> glossary;
- confirmed module behavior and current implementation -> the applicable Design
  or Architecture section of its module guide;
- consequential rationale and tradeoffs -> ADR;
- goals, acceptance criteria, dependencies, progress, current validation results,
  and remaining work -> tracker.

Other documents link to the authority and add only enough context to explain the
link. The development record briefly reports completed work and links outward; it
does not own rules, architecture, delivery scope, or status.

## Check implementation health

When documenting changed code, verify that each stable source unit has one
coherent responsibility that can be described in one sentence. Treat a class
that owns unrelated UI, input, persistence, validation, presentation, and
integration concerns as a structural warning. Document current ownership
honestly and name a sensible extraction seam, but do not expand the authorized
task into an unapproved refactor.

Derive maintenance details from current source, assets, and configuration. Never
guess a path, binding, reader, material slot, or validation procedure.

## Reconcile inconsistencies

When implementation and durable documentation differ:

1. Check the active Spec and Tickets.
2. If they describe an in-progress transition, keep progress in the tracker.
3. Otherwise, surface the exact conflict and ask which behavior is authoritative
   unless the conversation already settled it.
4. Update only the confirmed authority and authorized implementation scope.

Never quietly rewrite documentation to match unexplained code or rewrite code to
match unexplained documentation.

## Maintain the daily development record

After a task actually changes code, documentation, configuration, assets,
Git/Editor state, or settles a durable decision, update the configured record
once before reporting completion. Never create or update it for a read-only task.

Use the configured language, path, and local date. Reuse the day's file and append
without overwriting earlier work. Preserve user-written goal text and merge one
conversation task into one concise actual-implementation section. When the file
is absent, create only the minimal date, goal, and actual-implementation structure
used by the project.

Record actual results, key configuration, and direct validation. Include a small
diagram only when it materially clarifies changed flow. Do not record plans,
brainstorming, secrets, per-message chronology, or tracker status already owned
by the tracker.

## Report the maintenance result

State which module guide or other authority changed, what it now owns, and which
daily development record was updated. Report implementation, validation, Git,
and release state separately. Keep generated documentation in the project's
configured language even though this Skill source is English.
