from pathlib import Path
import unittest

try:
    from tests.metadata_support import parse_simple_metadata
except ModuleNotFoundError:
    from metadata_support import parse_simple_metadata


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "fix-bug"


class FixBugContractTests(unittest.TestCase):
    def test_fix_bug_is_available_for_implicit_repairs(self) -> None:
        metadata = parse_simple_metadata(SKILL_ROOT / "agents" / "openai.yaml")

        self.assertTrue(metadata["policy"]["allow_implicit_invocation"])
        self.assertIn("$fix-bug", metadata["interface"]["default_prompt"])

    def test_fix_bug_builds_a_red_capable_evidence_loop(self) -> None:
        instructions = " ".join(
            (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8").lower().split()
        )

        for invariant in (
            "red-capable",
            "three to five ranked",
            "falsifiable hypotheses",
            "change one variable at a time",
            "first divergence",
            "earliest checkpoint",
            "undo only that experiment's edits",
        ):
            with self.subTest(invariant=invariant):
                self.assertIn(invariant, instructions)

    def test_fix_bug_requires_regression_evidence_and_cleanup(self) -> None:
        instructions = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        for integration in ("$tdd", "$project-documentation", "$code-review"):
            with self.subTest(integration=integration):
                self.assertIn(integration, instructions)

        self.assertIn("remove temporary logs", instructions.lower())
        self.assertIn("do not claim the bug is fixed", instructions.lower())
        self.assertIn("redact credentials", instructions.lower())
        self.assertIn("captured baseline", instructions.lower())


if __name__ == "__main__":
    unittest.main()
