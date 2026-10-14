from pathlib import Path
import re
import unittest

try:
    from tests.metadata_support import parse_simple_metadata
except ModuleNotFoundError:
    from metadata_support import parse_simple_metadata


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_POLICIES = {
    "setup-senler-skills": False,
    "grill-with-docs": False,
    "to-spec": False,
    "to-tickets": False,
    "implement": False,
    "grilling": True,
    "ask-plan-build": True,
    "figma-task-steward": True,
    "project-documentation": True,
    "tdd": True,
    "code-review": True,
    "unreal-project": True,
}


class ReleaseContractTests(unittest.TestCase):
    def test_release_contains_the_expected_valid_packages(self) -> None:
        self.assertEqual(set(EXPECTED_POLICIES), {path.name for path in SKILLS.iterdir()})
        for name, implicit in EXPECTED_POLICIES.items():
            with self.subTest(skill=name):
                root = SKILLS / name
                self.assertTrue((root / "SKILL.md").is_file())
                metadata = parse_simple_metadata(root / "agents" / "openai.yaml")
                self.assertIn(f"${name}", metadata["interface"]["default_prompt"])
                self.assertIs(
                    implicit, metadata.get("policy", {}).get("allow_implicit_invocation", True)
                )

    def test_all_bundled_reference_links_resolve(self) -> None:
        link_pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
        for skill_file in SKILLS.glob("*/SKILL.md"):
            with self.subTest(skill=skill_file.parent.name):
                for target in link_pattern.findall(
                    skill_file.read_text(encoding="utf-8")
                ):
                    if "://" not in target and not target.startswith("#"):
                        self.assertTrue((skill_file.parent / target).is_file(), target)

    def test_skill_instructions_are_project_neutral(self) -> None:
        forbidden = ("TableGame", "InputDesign", "EventDesign", "CardDesign")
        for skill_file in SKILLS.glob("*/SKILL.md"):
            text = skill_file.read_text(encoding="utf-8")
            with self.subTest(skill=skill_file.parent.name):
                for term in forbidden:
                    self.assertNotIn(term, text)

    def test_readme_explains_the_public_release(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for heading in (
            "## Set and Use",
            "## Workflow",
            "## What Each Skill Does",
            "## Credit",
        ):
            self.assertIn(heading, readme)

        self.assertIn("Use only the stages your change needs", readme)
        self.assertIn("optional", readme.lower())
        self.assertNotIn("Every feature or solution goes through", readme)

    def test_readmes_offer_bilingual_navigation(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("[简体中文](README.zh-CN.md)", english)
        self.assertIn("[English](README.md)", chinese)
        self.assertIn("Use only the stages your change needs", english)
        self.assertIn("只运行这次变更真正需要的阶段", chinese)
        self.assertIn("directly with a Spec", english)
        self.assertIn("把 Spec 或一组 Tickets 直接交给", chinese)


if __name__ == "__main__":
    unittest.main()
