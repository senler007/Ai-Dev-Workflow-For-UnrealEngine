# GitLab issue tracker configuration

Use this seed for the repository's agent-facing `issue-tracker.md`. Replace every
placeholder with the confirmed project value and omit unused guidance.

```markdown
# Issue tracker

- Mode: GitLab
- Project: `{group}/{project}`
- Host: `{gitlab.com or self-hosted URL}`
- Specs: GitLab issues labeled `{spec label, if used}`
- Tickets: GitLab issues linked to their parent Spec
- Ready state: `{label or workflow state}`
- Done state: closed issue

Use `glab` against the project and host above for Issue reads and authorized
writes. Read the full parent Spec and selected Ticket before implementation.
Create blocking links with the configured GitLab relationship mechanism when
available; otherwise keep `Blocked by` references in each Issue body. Preserve
the parent relation through native linked work items when the configured GitLab
tier supports it, otherwise keep the `Parent` reference in the body.

Explicit invocation of `$to-spec` or `$to-tickets` authorizes the publication,
labels, and relationships that workflow describes after its own required
approval. Do not ask for duplicate publication confirmation. Publish directly
to GitLab and do not create temporary tracker files in the repository.
```
