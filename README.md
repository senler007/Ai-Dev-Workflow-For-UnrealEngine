English | [简体中文](README.zh-CN.md)

# Senler Skills

If you want to control your own project instead of letting AI turn it into a mess,
use this workflow. It makes AI ask about what it does not understand and work with
you until each feature or solution is clear. Finally, it preserves every design
decision and code structure in human-readable project documentation.

This workflow is largely inspired by AIHero, with three key changes:

- **Human-readable project docs.** Each major module keeps its durable design,
  current code structure, and maintenance map in one document people can read.
- **You control the workflow.** You decide which stage runs and when. AI does not orchestrate the project for you.
- **Create a Spec whenever you want to build or change something.** Each Spec is a small AI-written record you can read later, not a giant document trying to own the whole project.

## Set and Use

Paste this into Codex to install all ten Skills:

```text
Use $skill-installer to install all ten Skills from https://github.com/senler007/skills.
```

After installation, start a new Codex turn, open your project, and run:

```text
Use $setup-senler-skills to configure this project so every Skill knows where its docs and tracker live.
```

This initializes the Skills for that project and only needs to run once.

## Workflow

Use only the stages your change needs. You decide which Skill runs and when:

1. **Talk the design through** - run `$grill-with-docs` when the design is still unclear. It asks dependency-ready decisions in focused rounds, then writes the consolidated decisions to project docs only after you confirm the final summary.
   - **Examples:** "Help me define the full turn lifecycle." "Walk me through the item-card system and clarify its design."
2. **Create a change record** - run `$to-spec` whenever a feature or change is clear enough to build.
3. **Break it into real work (optional)** - run `$to-tickets` when the Spec needs independent slices, dependency ordering, or staged delivery, then approve the breakdown.
4. **Build exactly that scope** - run `$implement` directly with a Spec or a set of Tickets. It tests, updates docs, reviews the result, and commits.

Nothing silently starts the next stage. You stay in control.

**A small change:**

```text
You Say     :[$grill-with-docs] I need to flesh out the duel system
Communicate :Talk it through with AI...
You Say     :[$to-spec]
You Say     :[$implement]
Finally     :Finish with a complete feature ready for human acceptance testing
```

For larger work, run `[$to-tickets]` between `$to-spec` and `$implement` so you
can approve the slices and dependencies first.

## What Each Skill Does

### Explicit Workflows

These run only when you ask for them.

| Skill | What it does |
| --- | --- |
| `setup-senler-skills` | Configures GitHub, GitLab, local, or custom tracking plus project-doc paths without creating empty junk. |
| `grill-with-docs` | Runs dependency-safe design rounds, gets final confirmation, then writes the consolidated decisions to the right project document in one pass. |
| `to-spec` | Creates a small record of one change instead of copying the whole project design. |
| `to-tickets` | Optionally splits larger work into complete vertical slices and waits for you to approve the plan. |
| `implement` | Implements a Spec or Ticket scope, tests and reviews the complete task delta, updates durable docs, and commits only after verifying that user changes are not mixed in. |

### Supporting Skills

These provide discipline when the task needs it.

| Skill | What it does |
| --- | --- |
| `grilling` | Maps a design tree and asks only the dependency-ready decision frontier in each focused round. |
| `project-documentation` | Keeps each module's design, code structure, and maintenance map in one human-readable guide, then records completed project changes in the daily development record. |
| `fix-bug` | Repairs defects from evidence: reproduces the symptom, traces the first wrong state, fixes the earliest confirmed source, and leaves regression evidence. It can activate implicitly when you ask for a bug to be fixed. |
| `tdd` | Tests behavior through stable public seams instead of testing implementation details. |
| `code-review` | Reviews committed, staged, unstaged, and untracked changes across Standards, Spec, and Documentation without changing files. |

## Credit

Largely inspired by Matt Pocock's AIHero Skills workflow. This repository is MIT
licensed, independently maintained, and does not automatically sync upstream.
See [`LICENSE`](LICENSE).
