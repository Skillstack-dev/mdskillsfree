---
name: multi-step-reasoning
description: >
  Enables structured, multi-step reasoning using Chain-of-Thought (CoT) and Tree-of-Thought (ToT)
  frameworks. Use this skill whenever a problem is complex, ambiguous, or multi-layered — including
  debugging, product decisions, UX flow design, business strategy, AI agent planning, math, logic
  puzzles, or any task where a single-shot answer risks being wrong or shallow. Trigger this skill
  when the user says things like "help me think through", "what should I do about", "how do I
  decide", "analyze this problem", "walk me through", "I'm stuck on", or asks for a structured
  breakdown of any non-trivial challenge. Also trigger for any multi-variable trade-off analysis,
  root cause investigations, scenario planning, or when you sense the user needs a decision framework
  rather than a quick answer. Do NOT use for simple factual lookups, single-step tasks, or casual
  conversation.
---

# Multi-Step Reasoning Skill
## Chain-of-Thought + Tree-of-Thought Reasoning Framework

---

## 1. SKILL OVERVIEW

**Purpose**: Give any AI agent the ability to reason carefully through hard problems — breaking
them down, exploring alternatives, evaluating paths, and producing a clear, confident answer.

**When to USE this skill:**
- Multi-variable decisions with trade-offs
- Root cause analysis / debugging
- Planning (product, strategy, UX, engineering)
- Problems where a wrong first assumption cascades into a wrong answer
- Any task explicitly requesting "step by step", "think through", or "analyze"
- When the agent's first-pass answer feels uncertain or shallow

**When NOT to use:**
- Simple factual lookups ("What year was X founded?")
- Single-step transformations ("Translate this to French")
- Casual small talk or emotional support conversations
- Tasks already fully scoped with a clear single correct answer

---

## 2. REASONING MODES

Read `references/modes.md` for the full breakdown. Quick reference:

| Mode | Use When | Style |
|------|----------|-------|
| **Chain-of-Thought (CoT)** | Linear, sequential problems | One path, step by step |
| **Tree-of-Thought (ToT)** | Multiple valid strategies exist | Branch → evaluate → prune |
| **Self-Consistency** | High-stakes, one correct answer | N parallel CoT chains → vote |
| **Reflection + Retry** | Agent catches its own error | Pause → critique → redo |

**Quick selection heuristic:**
- Is there one clearly correct approach? → **CoT**
- Are there 2–4 meaningfully different strategies worth comparing? → **ToT**
- Is correctness critical and verifiable? → **Self-Consistency**
- Did the previous step produce something suspicious? → **Reflection + Retry**

---

## 3. EXECUTION FLOW

Follow this sequence for every reasoning task:

```
STEP 1 — PARSE
  Read the problem. Extract: goal, constraints, unknowns, success criteria.
  If ambiguous → state your assumption explicitly before proceeding.

STEP 2 — DECOMPOSE
  Break the problem into 2–5 sub-problems.
  Each sub-problem should be independently solvable.
  Label them: [SP-1], [SP-2], ...

STEP 3 — SELECT MODE
  Apply the heuristic above to choose CoT or ToT.
  State the selected mode briefly.

STEP 4 — GENERATE PATHS
  CoT: Solve each sub-problem sequentially.
  ToT: For each sub-problem, generate 2–3 candidate approaches.

STEP 5 — EVALUATE
  Score each path on: feasibility, risk, alignment with goal.
  Prune weak branches. Keep the best 1–2 per sub-problem.

STEP 6 — SYNTHESIZE
  Combine the best path across all sub-problems into a unified answer.

STEP 7 — CONFIDENCE CHECK
  Assign confidence (High / Medium / Low) with one-line justification.
  If Low → trigger Reflection + Retry before presenting the answer.

STEP 8 — OUTPUT
  Use the standard output schema (see Section 5).
```

---

## 4. PROMPT TEMPLATES

See `references/prompts.md` for the full library. Quick index:

- `BASIC_COT` — Linear step-by-step for clear problems
- `TOT_EXPLORE` — Branch and prune for strategic problems
- `SELF_CONSISTENCY` — Parallel paths + voting for high-stakes decisions
- `REFLECT_RETRY` — Catch and correct intermediate errors
- `AGENT_PLAN` — For autonomous agent task planning
- `UX_DECISION` — Specialized for UX/product trade-off analysis

Load and use the relevant template from `references/prompts.md`.

---

## 5. OUTPUT SCHEMA

Every response from this skill MUST follow this structure (adapt verbosity to context):

```json
{
  "reasoning_steps": [
    { "step": 1, "label": "Parse", "content": "..." },
    { "step": 2, "label": "Decompose", "content": "..." },
    { "step": 3, "label": "Reason", "content": "..." }
  ],
  "alternatives": [
    { "path": "A", "summary": "...", "score": 7 },
    { "path": "B", "summary": "...", "score": 4 }
  ],
  "evaluation": "Path A wins because...",
  "final_answer": "Clear, direct recommendation or solution.",
  "confidence_score": "High | Medium | Low",
  "confidence_reason": "One sentence justifying confidence level."
}
```

In **conversational** contexts, render this as readable prose with clear section breaks —
not raw JSON. Reserve JSON output for tool/API contexts.

---

## 6. OPTIMIZATION RULES

**Skip reasoning when:**
- Problem has a single, unambiguous correct answer
- Answer is factual and within training knowledge
- User explicitly says "just tell me quickly"

**Compress steps when:**
- Problem has ≤ 2 sub-problems → merge Steps 2 and 3
- User is an expert → skip explaining obvious sub-steps
- Token budget is tight → use bullet summaries, not full prose per step

**Token efficiency:**
- Do not restate the problem in full — reference it by label
- Use `[SP-1]`, `[Path-A]` labels instead of repeating descriptions
- Prune ToT branches after scoring — don't narrate eliminated paths in detail

**Retry trigger:**
- If a step produces a contradiction, implausibility, or "I'm not sure" moment → stop
- Invoke `REFLECT_RETRY` template (see `references/prompts.md`)
- Max 2 retries before escalating to user for clarification

---

## 7. FAILURE MODES & MITIGATIONS

See `references/failure_modes.md` for full details. Summary:

| Failure | Signal | Fix |
|---------|--------|-----|
| Overthinking | 5+ sub-problems for a simple task | Force-cap at 3 sub-problems |
| Wrong premise | Answer contradicts stated constraint | Re-parse Step 1 with fresh eyes |
| Branch explosion | ToT generates 6+ paths | Prune to top 3 before evaluating |
| Circular reasoning | Step 4 references Step 2 as proof | Flag + invoke Reflection mode |
| Confidence inflation | Says "High" but answer is speculative | Require evidence before High rating |

---

## 8. INTEGRATION NOTES

### Memory / RAG
- Before Step 1 (Parse), query memory for prior context on this problem domain
- After Step 8 (Output), write the `final_answer` + `confidence_score` to memory
- Tag memory entries: `reasoning`, `decision`, `[domain]`

### Tool Use
- Tools can be called between Steps 4 and 5 (after generating paths, before evaluating)
- Example: web search to validate a factual assumption in a reasoning branch
- Tool results feed back into the evaluation step as evidence

### Autonomous Agents
- Use `AGENT_PLAN` template from `references/prompts.md`
- Output `reasoning_steps` as an executable task queue
- Pass `alternatives` to a supervisor agent for human-in-the-loop decisions on High-Risk branches
- Re-run this skill at each major decision node in a multi-step pipeline

---

## 9. REFERENCE FILES

| File | When to Read |
|------|-------------|
| `references/modes.md` | Need full CoT vs ToT decision logic |
| `references/prompts.md` | Need a copy-paste prompt template |
| `references/failure_modes.md` | Debugging a bad reasoning output |
| `references/use_cases.md` | Need worked examples for a domain |

Load only what you need. Default: start with SKILL.md, load references on demand.
