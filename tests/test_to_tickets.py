from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "skills" / "to-tickets"


class ToTicketsContractTests(unittest.TestCase):
    def test_package_and_explicit_policy(self) -> None:
        self.assertTrue((ROOT / "SKILL.md").is_file())
        metadata = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$to-tickets", metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)

    def test_inline_ticket_template_matches_the_delivery_contract(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        template = skill.split("<issue-template>", 1)[1].split(
            "</issue-template>", 1
        )[0]
        for heading in ("Parent", "What to build", "Acceptance criteria", "Blocked by"):
            self.assertIn(f"## {heading}", template)

    def test_workflow_quizzes_then_publishes_the_approved_breakdown(self) -> None:
        skill = " ".join(
            (ROOT / "SKILL.md").read_text(encoding="utf-8").lower().split()
        )

        self.assertIn("quiz the user", skill)
        self.assertIn("until the user approves the breakdown", skill)
        self.assertIn("do not ask for another publication confirmation", skill)
        self.assertIn("do not close, relabel, change the status of", skill)
        self.assertIn("native parent/sub-issue relationship", skill)

    def test_local_ticket_contract_uses_configured_parent_and_state(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        template = skill.split("<local-ticket-template>", 1)[1].split(
            "</local-ticket-template>", 1
        )[0]

        self.assertIn("**Parent:**", template)
        self.assertIn("configured ready state", template)
        self.assertIn("does not start implementing", skill)

    def test_skill_does_not_decide_that_tickets_are_unnecessary(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()

        self.assertNotIn("small cohesive change", skill)
        self.assertNotIn("can run the spec directly and stop", skill)
        self.assertNotIn("tickets only to satisfy ceremony", skill)


if __name__ == "__main__":
    unittest.main()
