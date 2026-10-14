# Repository guidance

- Preserve the copied local skills' source language and rules; do not translate or
  rewrite them just to generalize project identifiers.
- Limit `SKILL.md` frontmatter to `name` and `description`.
- Keep only instructions that add Senler-specific decisions or prevent a concrete
  workflow failure. Do not duplicate general coding advice or require upstream
  structure; this is an independently maintained derivative.
- Validate changed skills with the bundled skill validator and run
  `python -m unittest discover -s tests -v`.
- Preserve the MIT attribution to Matt Pocock and senler007.

The current local skill packages are the source of truth. The initializer is
a new local implementation of the fixed document structure, not a restored
remote workflow. Do not restore
removed packages, document maps, tests, or daily development records from remote
history. Maintain the package catalog and usage in README.md / README.zh-CN.md;
skill behavior belongs in skills/<name>/SKILL.md and its linked resources.
Consumer projects must use the fixed document structure defined by
skills/project-documentation/SKILL.md; do not add alternative-layout discovery.
This package repository is not a consumer-project initialization target.
