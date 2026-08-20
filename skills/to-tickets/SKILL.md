---
name: to-tickets
description: Break a plan, Spec, or the current conversation into a set of tracer-bullet Tickets, each declaring its blocking edges, published to the configured tracker. Use when the user explicitly asks to split understood work into implementation Tickets.
---

# To Tickets

Break a plan, Spec, or conversation into a set of **Tickets** — tracer-bullet vertical slices, each declaring the Tickets that **block** it.

Locate the issue-tracker map through the repository's agent instructions. If it
is missing, tell the user to explicitly run `$setup-senler-skills`; do not run
that explicit-only workflow on their behalf.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a Spec path, an Issue number or URL) as an argument, fetch it and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's terminology, module guides, and ADRs.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft vertical slices

Break the work into **tracer bullet** Tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests) — vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

Give each Ticket its **blocking edges** — the other Tickets that must complete before it can start. A Ticket with no blockers can start immediately.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change — rename a column, retype a shared symbol — whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own Ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a Ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify Ticket — green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each Ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other Tickets (if any) must complete first
- **What it delivers**: the end-to-end behavior this Ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct — does each Ticket only depend on Tickets that genuinely gate it?
- Should any Tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Publish the Tickets to the configured tracker

Publish the approved Tickets. **How** depends on the tracker `$setup-senler-skills` configured — the Tickets are the same either way, only the shape of the blocking edges changes:

- **Local files** → write one file per Ticket at the configured Ticket path,
  numbered from `01` in dependency order (blockers first). Each file records the
  configured ready state, its parent Spec when one exists, and the numbers/titles
  that block it. Use the per-Ticket file template below — one Ticket per file,
  never a single combined file.
- **A real issue tracker** → publish one Issue per Ticket in dependency order (blockers first) so each Ticket's blocking edges can reference real identifiers. Use native blocking and sub-issue relationships where available; otherwise record the relationships in the Issue body. Apply the configured ready label or state.
- **A custom tracker** → follow its configured identifiers, relationships, and state rules.

Explicit invocation of `$to-tickets` authorizes publication of the approved Ticket set and its configured relationships or labels. After the user approves the breakdown, do not ask for another publication confirmation. When the configured tracker is external, publish directly and do not create temporary Ticket files inside the repository.

For later implementation, the eligible set is the **frontier**: any Ticket whose
blockers are all done. For a purely linear chain that means top to bottom. This
workflow defines that set; it does not start implementing it.

Do not close, relabel, change the status of, or rewrite any parent Spec. The only
allowed parent-side mutation is the native parent/sub-issue relationship already
authorized by this publication workflow.

<local-ticket-template>

# <NN> — <Ticket title>

**Parent:** the configured relative path to the parent Spec, or omit this field
when the source was not a Spec.

**What to build:** the end-to-end behavior this Ticket makes work, from the user's perspective — not a layer-by-layer implementation list.

**Blocked by:** the numbers/titles of the Tickets that gate this one, or "None — can start immediately".

**Status:** the configured ready state

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

A reference to the parent Spec on the tracker (if the source was an existing Spec, otherwise omit this section).

## What to build

The end-to-end behavior this Ticket makes work, from the user's perspective — not a layer-by-layer implementation list.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking Ticket, or "None — can start immediately".

</issue-template>

In either form, avoid specific file paths or code snippets — they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

Do not automatically invoke `$implement`; the user chooses the next workflow.
