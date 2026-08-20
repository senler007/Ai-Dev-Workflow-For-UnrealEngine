from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"


def read_skill(name: str) -> str:
    return (SKILLS_ROOT / name / "SKILL.md").read_text(encoding="utf-8")


def read_metadata(name: str) -> str:
    return (SKILLS_ROOT / name / "agents" / "openai.yaml").read_text(
        encoding="utf-8"
    )


class GrillingWorkflowContractTests(unittest.TestCase):
    def test_both_grilling_skills_are_discoverable(self) -> None:
        for name in ("grilling", "grill-with-docs"):
            with self.subTest(skill=name):
                skill_root = SKILLS_ROOT / name
                self.assertTrue((skill_root / "SKILL.md").is_file())
                self.assertTrue((skill_root / "agents" / "openai.yaml").is_file())

    def test_invocation_policies_match_matt(self) -> None:
        self.assertIn("allow_implicit_invocation: true", read_metadata("grilling"))
        self.assertIn(
            "allow_implicit_invocation: false", read_metadata("grill-with-docs")
        )

    def test_grilling_uses_dependency_safe_frontier_rounds(self) -> None:
        grilling = read_skill("grilling")

        self.assertIn("Interview the user relentlessly", grilling)
        self.assertIn("design tree", grilling)
        self.assertIn("frontier rounds", grilling)
        self.assertIn("prerequisites", grilling)
        self.assertIn("If a fact can be found", grilling)
        self.assertIn("The decisions, though, are the user's", grilling)
        self.assertIn("Do not act on the design", grilling)
        self.assertNotIn("sub-agent", grilling)

    def test_grill_with_docs_is_only_the_approved_composition(self) -> None:
        workflow = read_skill("grill-with-docs")

        self.assertIn("$grilling", workflow)
        self.assertIn("$project-documentation", workflow)
        self.assertIn("existing module guides", workflow)
        self.assertIn("Ask before creating a new module guide", workflow)

    def test_grill_with_docs_defers_writes_until_final_confirmation(self) -> None:
        workflow = read_skill("grill-with-docs")

        self.assertIn(
            "Do not edit project documentation while the interview is in progress",
            workflow,
        )
        self.assertIn("consolidated summary", workflow)
        self.assertIn("explicit final confirmation", workflow)
        self.assertIn("in one documentation pass", workflow)
        self.assertNotIn("as the session proceeds", workflow)


if __name__ == "__main__":
    unittest.main()
