---
name: to-spec
description: Turn the current conversation into a lightweight Spec and publish it to the configured project tracker — no interview, just synthesis of what has already been discussed. Use when the user explicitly asks to create a Spec or PRD.
---

This skill takes the current conversation context and codebase understanding and
produces a Spec. Do NOT interview the user — just synthesize what is already
known.

Locate the issue-tracker and project-documentation maps through the repository's
agent instructions. If either is missing, tell the user to explicitly run
`$setup-senler-skills`; do not run that explicit-only workflow on their behalf.

## Process

1. Explore the repo to understand the current state of the codebase, if you have
   not already. Use the project's terminology throughout the Spec, respect ADRs,
   and link relevant module guides instead of copying their durable content.

2. Sketch the seams at which the change will be tested. Prefer existing seams to
   new ones and use the highest seam possible. The fewer seams across the change,
   the better; one is ideal.

   Check with the user that these seams match their expectations.

3. Write the Spec using the template below, then publish it exactly where the
   configured tracker map specifies. For a local tracker, create the configured
   Spec file and Status field. For an external tracker, publish directly without
   a temporary repository copy. Apply the configured ready label or state; no
   additional triage is needed.

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

Read back the published Spec to verify its title, body, state, and identifier.
Report its path, identifier, or URL. Do not automatically start
`$to-tickets` or `$implement`; the user chooses the next workflow.
