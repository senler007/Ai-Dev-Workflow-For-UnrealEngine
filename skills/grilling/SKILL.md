---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any grill trigger phrase.
---

Interview the user relentlessly until you reach a shared understanding. Map the
topic as a **design tree**: every decision branches into the decisions that
depend on it.

Work in **frontier rounds**. The frontier is every unresolved decision whose
prerequisites are already settled. Ask that whole frontier in one numbered round,
give a recommended answer for each question, then wait for the user's answers.
Never ask a question whose answer still depends on another open decision in the
same round.

If a fact can be found by exploring the environment (filesystem, tools, etc.),
look it up directly instead of asking the user or delegating it. A missing fact
keeps only its dependent branch off the frontier; independent questions can
still proceed. The decisions, though, are the user's — put each one to them and
wait for their answer.

After every round, update the tree from the answers and recompute the frontier.
The session ends only when the frontier is empty and the user confirms the
consolidated understanding. Do not act on the design before that confirmation.
