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
    "fix-bug": True,
    "grilling": True,
    "project-documentation": True,
    "tdd": True,
    "code-review": True,
}


def frontmatter(skill_file: Path) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}

    parsed: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return parsed
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            parsed[key] = value.strip().strip('"')
    return {}


def readme_skill_names(path: Path) -> set[str]:
    pattern = re.compile(r"^\| `([a-z0-9-]+)` \|", re.MULTILINE)
    return set(pattern.findall(path.read_text(encoding="utf-8")))


class ReleaseContractTests(unittest.TestCase):
    def test_release_contains_exactly_ten_valid_packages(self) -> None:
        self.assertEqual(set(EXPECTED_POLICIES), {path.name for path in SKILLS.iterdir()})
        for name, implicit in EXPECTED_POLICIES.items():
            with self.subTest(skill=name):
                root = SKILLS / name
                skill_file = root / "SKILL.md"
                self.assertTrue(skill_file.is_file())
                skill_frontmatter = frontmatter(skill_file)
                self.assertEqual({"name", "description"}, set(skill_frontmatter))
                self.assertEqual(name, skill_frontmatter["name"])
                self.assertTrue(skill_frontmatter["description"])

                metadata = parse_simple_metadata(root / "agents" / "openai.yaml")
                self.assertLessEqual({"interface", "policy"}, set(metadata))
                self.assertLessEqual(
                    {"display_name", "short_description", "default_prompt"},
                    set(metadata["interface"]),
                )
                self.assertLessEqual(
                    {"allow_implicit_invocation"}, set(metadata["policy"])
                )
                self.assertIn(f"${name}", metadata["interface"]["default_prompt"])
                self.assertIsInstance(metadata["interface"]["display_name"], str)
                self.assertIsInstance(metadata["interface"]["short_description"], str)
                self.assertIsInstance(metadata["interface"]["default_prompt"], str)
                self.assertGreaterEqual(
                    len(metadata["interface"]["short_description"]), 25
                )
                self.assertLessEqual(
                    len(metadata["interface"]["short_description"]), 64
                )
                self.assertIs(
                    implicit, metadata["policy"]["allow_implicit_invocation"]
                )

    def test_all_repository_markdown_links_resolve(self) -> None:
        link_pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
        for markdown_file in ROOT.rglob("*.md"):
            with self.subTest(markdown=str(markdown_file.relative_to(ROOT))):
                for target in link_pattern.findall(
                    markdown_file.read_text(encoding="utf-8")
                ):
                    if "://" not in target and not target.startswith("#"):
                        path = target.split("#", 1)[0]
                        self.assertTrue((markdown_file.parent / path).is_file(), target)

    def test_skill_instructions_are_project_neutral(self) -> None:
        forbidden = ("TableGame", "InputDesign", "EventDesign", "CardDesign")
        for skill_source in SKILLS.rglob("*.md"):
            text = skill_source.read_text(encoding="utf-8")
            with self.subTest(source=str(skill_source.relative_to(SKILLS))):
                for term in forbidden:
                    self.assertNotIn(term, text)
                self.assertIsNone(re.search(r"[\u3400-\u9fff]", text))

    def test_cross_skill_references_resolve_to_bundled_skills(self) -> None:
        reference_pattern = re.compile(r"\$([a-z][a-z0-9-]*)")
        references: set[str] = set()

        for skill_source in SKILLS.rglob("*.md"):
            references.update(
                reference_pattern.findall(skill_source.read_text(encoding="utf-8"))
            )

        self.assertLessEqual(references, set(EXPECTED_POLICIES))

    def test_consumers_do_not_auto_run_explicit_setup(self) -> None:
        for name in (
            "code-review",
            "grill-with-docs",
            "project-documentation",
            "to-spec",
            "to-tickets",
        ):
            with self.subTest(skill=name):
                instructions = " ".join(
                    (SKILLS / name / "SKILL.md")
                    .read_text(encoding="utf-8")
                    .lower()
                    .split()
                )
                self.assertIn("explicitly run `$setup-senler-skills`", instructions)
                self.assertIn("do not run", instructions)

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

    def test_readme_skill_tables_match_the_release(self) -> None:
        expected = set(EXPECTED_POLICIES)

        self.assertEqual(expected, readme_skill_names(ROOT / "README.md"))
        self.assertEqual(expected, readme_skill_names(ROOT / "README.zh-CN.md"))


if __name__ == "__main__":
    unittest.main()
