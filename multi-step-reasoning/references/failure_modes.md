# Failure Modes — Full Reference

---

## FM-1: Overthinking

**What happens:** Agent generates 6+ sub-problems for a task that needs 2.
Token cost balloons. User gets confused by unnecessary complexity.

**Detection signals:**
- More than 5 sub-problems generated
- Sub-problems are nested more than 2 levels deep
- Time spent reasoning > 3x what the output justifies

**Mitigation:**
- Hard cap: Maximum 4 sub-problems per decomposition
- If the problem naturally has more, group related ones
- Ask: "Could this sub-problem be a note at the end instead of a step?" If yes → move it.

---

## FM-2: Wrong Premise / Bad Assumption at Step 1

**What happens:** Agent misreads a constraint or goal. All subsequent steps are
technically correct but answer the wrong question.

**Detection signals:**
- Final answer doesn't feel responsive to the original ask
- User says "that's not what I meant"
- A stated constraint appears to be violated in the answer

**Mitigation:**
- Always restate the goal in one sentence at Step 1 (Parse)
- Explicit assumption logging: "I'm assuming X. If wrong, the answer changes."
- On retry: re-read the original problem before Step 1, not the restatement

---

## FM-3: Branch Explosion in ToT

**What happens:** ToT generates too many paths. Evaluation becomes shallow.
Agent picks a winner based on surface-level scoring, not real reasoning.

**Detection signals:**
- 5+ branches per sub-problem
- Evaluation scores are all within 1 point of each other
- Agent can't articulate why the winner beat the runner-up

**Mitigation:**
- Prune before evaluating: Eliminate any branch that violates a hard constraint immediately
- Diversity check: If two branches are 80%+ similar, merge them into one
- ToT max branches per node: 3. Non-negotiable.

---

## FM-4: Circular Reasoning

**What happens:** A later step uses the conclusion of an earlier step as evidence
for that same conclusion. The reasoning is internally consistent but proves nothing.

**Detection signals:**
- "As established in Step 2..." — and Step 2 itself relied on what Step 4 is proving
- Agent says "this is clearly true" without external evidence
- Confidence is High but the answer is non-falsifiable

**Mitigation:**
- Each claim in a step must cite either: (a) the original problem, (b) a prior step's
  output, or (c) external knowledge — never the current step's conclusion
- Invoke REFLECT_RETRY and specifically ask: "Is this step self-referential?"

---

## FM-5: Confidence Inflation

**What happens:** Agent assigns High confidence to speculative or assumption-heavy
answers. User treats it as fact. Bad outcome follows.

**Detection signals:**
- Answer contains "probably", "I believe", "likely" — but confidence is High
- Answer is based on 2+ unverified assumptions
- The domain is one where the agent's training data is sparse or outdated

**Mitigation:**
- Confidence rules (enforce strictly):
  - **High**: Every claim is grounded in explicit problem data or verifiable knowledge
  - **Medium**: 1–2 assumptions made; answer directionally correct but details uncertain
  - **Low**: Multiple unknowns; answer is a starting point, not a recommendation
- When in doubt: downgrade one level

---

## FM-6: Premature Convergence

**What happens:** Agent picks a winner in ToT too early — before exploring alternatives
properly. The "tree" is really just a single chain with discarded branches that were never
genuinely developed.

**Detection signals:**
- Winning branch is 5x longer than alternatives (alternatives were sketched, not thought through)
- Agent says "obviously Path A is best" at the generation phase, before scoring

**Mitigation:**
- All branches must be developed to roughly equal depth before scoring
- "Devil's advocate" rule: Before selecting a winner, make the strongest possible case
  for the runner-up. Only then confirm the winner.
