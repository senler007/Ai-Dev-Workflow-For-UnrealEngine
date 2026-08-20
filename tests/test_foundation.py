from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"


def frontmatter_keys(skill_file: Path) -> set[str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return set()

    keys: set[str] = set()
    for line in lines[1:]:
        if line == "---":
            break
        if line and not line[0].isspace() and ":" in line:
            keys.add(line.split(":", 1)[0])
    return keys


class FoundationContractTests(unittest.TestCase):
    def test_repository_preserves_upstream_and_original_mit_attribution(self) -> None:
        license_text = (REPOSITORY_ROOT / "LICENSE").read_text(encoding="utf-8")

        self.assertIn("MIT License", license_text)
        self.assertIn("Copyright (c) 2026 Matt Pocock", license_text)
        self.assertIn("Copyright (c) 2026 senler007", license_text)

    def test_foundation_skills_use_the_standard_package_shape(self) -> None:
        for skill_name in ("setup-senler-skills", "project-documentation"):
            with self.subTest(skill=skill_name):
                skill_root = SKILLS_ROOT / skill_name
                skill_file = skill_root / "SKILL.md"
                self.assertTrue(skill_file.is_file())
                self.assertEqual({"name", "description"}, frontmatter_keys(skill_file))
                self.assertTrue((skill_root / "agents" / "openai.yaml").is_file())

    def test_invocation_policies_match_the_public_workflow(self) -> None:
        setup_metadata = (
            SKILLS_ROOT / "setup-senler-skills" / "agents" / "openai.yaml"
        ).read_text(encoding="utf-8")
        documentation_metadata = (
            SKILLS_ROOT / "project-documentation" / "agents" / "openai.yaml"
        ).read_text(encoding="utf-8")

        self.assertIn('allow_implicit_invocation: false', setup_metadata)
        self.assertIn('allow_implicit_invocation: true', documentation_metadata)
        self.assertIn('$setup-senler-skills', setup_metadata)
        self.assertIn('$project-documentation', documentation_metadata)
        self.assertIn('module docs', setup_metadata)
        self.assertIn('module guides', documentation_metadata)

    def test_setup_bundles_every_supported_tracker_and_document_layout_contract(self) -> None:
        references = SKILLS_ROOT / "setup-senler-skills" / "references"

        for filename in (
            "issue-tracker-github.md",
            "issue-tracker-gitlab.md",
            "issue-tracker-local.md",
            "issue-tracker-custom.md",
            "project-docs.md",
        ):
            with self.subTest(reference=filename):
                self.assertTrue((references / filename).is_file())

    def test_documentation_reference_defines_the_module_guide_authority(self) -> None:
        roles = (
            SKILLS_ROOT
            / "project-documentation"
            / "references"
            / "document-roles.md"
        ).read_text(encoding="utf-8")

        for role in (
            "Project overview",
            "Glossary",
            "Module guide",
            "Design section",
            "Architecture section",
            "ADRs",
            "Tracker work",
            "Development record",
        ):
            with self.subTest(role=role):
                self.assertIn(role, roles)

    def test_module_guide_reference_defines_the_human_readable_contract(self) -> None:
        guide = (
            SKILLS_ROOT
            / "project-documentation"
            / "references"
            / "module-guide-structure.md"
        ).read_text(encoding="utf-8")

        for required_section in (
            "Module at a glance",
            "Design",
            "Architecture",
            "Maintenance map",
            "Common change recipes",
            "Stable validation",
        ):
            with self.subTest(section=required_section):
                self.assertIn(required_section, guide)

        self.assertFalse(
            (
                SKILLS_ROOT
                / "project-documentation"
                / "references"
                / "architecture.md"
            ).exists()
        )

    def test_new_module_document_boundaries_require_human_confirmation(self) -> None:
        instructions = " ".join((
            SKILLS_ROOT / "project-documentation" / "SKILL.md"
        ).read_text(encoding="utf-8").lower().split())

        self.assertIn("new module guide", instructions)
        self.assertIn("explicit human confirmation", instructions)

    def test_setup_does_not_configure_a_standalone_architecture_document(self) -> None:
        setup = (SKILLS_ROOT / "setup-senler-skills" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        template = (
            SKILLS_ROOT
            / "setup-senler-skills"
            / "references"
            / "project-docs.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("docs/Architecture.md", setup)
        self.assertNotIn("- Architecture:", template)
        self.assertIn("Module documentation:", template)

    def test_documentation_skill_requires_one_daily_record_for_modifying_tasks(self) -> None:
        instructions = (
            SKILLS_ROOT / "project-documentation" / "SKILL.md"
        ).read_text(encoding="utf-8")
        setup_template = (
            SKILLS_ROOT
            / "setup-senler-skills"
            / "references"
            / "project-docs.md"
        ).read_text(encoding="utf-8")

        self.assertIn("daily development record", instructions)
        self.assertIn("Never create or update it for a read-only task", instructions)
        self.assertIn("Development records:", setup_template)


if __name__ == "__main__":
    unittest.main()
