from pathlib import Path
import re
import unittest

from tests.metadata_support import parse_simple_metadata


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_POLICIES = {
    "setup-senler-skills": True,
    "figma-task-steward": True,
    "ask-plan-build": True,
    "grilling": True,
    "unreal-project": True,
    "project-documentation": True,
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
        key, value = line.split(":", 1)
        if key in parsed:
            raise ValueError(f"duplicate frontmatter field: {key}")
        parsed[key] = value.strip()
    return {}


class ReleaseContractTests(unittest.TestCase):
    def test_packages_and_invocation_metadata(self) -> None:
        self.assertEqual(set(EXPECTED_POLICIES), {path.name for path in SKILLS.iterdir()})
        for name, implicit in EXPECTED_POLICIES.items():
            with self.subTest(skill=name):
                root = SKILLS / name
                header = frontmatter(root / "SKILL.md")
                self.assertEqual({"name", "description"}, set(header))
                self.assertEqual(name, header["name"])
                self.assertTrue(header["description"])

                metadata_path = root / "agents" / "openai.yaml"
                if not metadata_path.exists():
                    # Metadata is optional; the default invocation policy is implicit.
                    self.assertIs(implicit, True)
                    continue
                metadata = parse_simple_metadata(metadata_path)
                interface = metadata["interface"]
                for field in ("display_name", "short_description", "default_prompt"):
                    self.assertIsInstance(interface[field], str)
                    self.assertTrue(interface[field])
                self.assertIn(f"${name}", interface["default_prompt"])
                self.assertGreaterEqual(len(interface["short_description"]), 25)
                self.assertLessEqual(len(interface["short_description"]), 64)
                self.assertIs(implicit, metadata.get("policy", {}).get("allow_implicit_invocation", True))

    def test_repository_markdown_links_resolve(self) -> None:
        link_pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
        for markdown_file in ROOT.rglob("*.md"):
            with self.subTest(markdown=str(markdown_file.relative_to(ROOT))):
                for target in link_pattern.findall(
                    markdown_file.read_text(encoding="utf-8")
                ):
                    if "://" not in target and not target.startswith("#"):
                        path = target.split("#", 1)[0]
                        self.assertTrue((markdown_file.parent / path).exists(), target)

    def test_active_skill_references_resolve(self) -> None:
        sources = [
            ROOT / "AGENTS.md",
            ROOT / "README.md",
            ROOT / "README.zh-CN.md",
            *SKILLS.rglob("*.md"),
            *SKILLS.rglob("*.yaml"),
            *(ROOT / "docs" / "agents").glob("*.md"),
        ]
        for source in sources:
            with self.subTest(source=str(source.relative_to(ROOT))):
                references = set(
                    re.findall(r"\$([a-z][a-z0-9-]*)", source.read_text(encoding="utf-8"))
                )
                self.assertLessEqual(references, set(EXPECTED_POLICIES))

    def test_readme_catalogs_match_installed_packages(self) -> None:
        for filename in ("README.md", "README.zh-CN.md"):
            with self.subTest(readme=filename):
                catalog = re.findall(
                    r"^\| `([a-z0-9-]+)` \|",
                    (ROOT / filename).read_text(encoding="utf-8"),
                    re.MULTILINE,
                )
                self.assertCountEqual(EXPECTED_POLICIES, catalog)

    def test_skill_sources_remain_project_neutral(self) -> None:
        for source in SKILLS.rglob("*.md"):
            with self.subTest(source=str(source.relative_to(SKILLS))):
                text = source.read_text(encoding="utf-8")
                self.assertNotIn("TableGame", text)
                self.assertNotIn("senler007/skills", text)
                self.assertNotIn("C:/Users/Administrator", text)

    def test_mit_attributions_are_preserved(self) -> None:
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        for required in (
            "MIT License",
            "Copyright (c) 2026 Matt Pocock",
            "Copyright (c) 2026 senler007",
        ):
            self.assertIn(required, license_text)


if __name__ == "__main__":
    unittest.main()
