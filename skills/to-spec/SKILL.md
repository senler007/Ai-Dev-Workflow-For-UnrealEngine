---
name: to-spec
description: Turn the current conversation into a lightweight Spec and publish it to the configured project tracker — no interview, just synthesis of what has already been discussed. Use when the user explicitly asks to create a Spec or PRD.
---

This skill takes the current conversation context and codebase understanding and
produces a Spec. Do NOT interview the user — just synthesize what is already
known.

Read the tracker and documentation map in AGENTS.md or its referenced files.
A separate issue-tracker.md or project-docs.md is not required. If no publication
destination is configured, use `$setup-senler-skills` to resolve that missing
tracker choice for this requested Spec; reuse all other project setup. Do not
assume that a Git remote alone authorizes choosing its issue tracker.

## Process

1. Explore the repo to understand the current state of the codebase, if you have
   not already. Use the project's terminology throughout the Spec, respect ADRs,
   and link relevant module guides instead of copying their durable content.

2. Sketch the seams at which the change will be tested. Prefer existing seams to
   new ones and use the highest seam possible. The fewer seams across the change,
   the better; one is ideal.

   Check with the user that these seams match their expectations.

3. Write the Spec using the template below, then publish it to the configured
   project tracker. Apply the configured ready label or state; no additional
   triage is needed.

Invoking `$to-spec` explicitly authorizes this one Spec publication and its
configured ready label. Do not ask for a second confirmation before publishing.
In GitHub mode, create the Issue directly and do not write a temporary Spec file
inside the repository.

<spec-template>

## Goal

The problem the user is facing and the observable result this change should
produce.

## Change

The confirmed behavioral and maintenance delta. Include implementation decisions
only when they were already settled and are needed to prevent ambiguity. Link
module guides or ADRs instead of copying long-lived project knowledge.

## Scope

What this change includes and explicitly excludes.

## Acceptance & Testing

Objective completion criteria, the agreed testing seams, observable cases, and
required project-documentation synchronization.

</spec-template>

Report the published identifier or URL. Do not automatically start
`$to-tickets` or `$implement`; the user chooses the next workflow.
