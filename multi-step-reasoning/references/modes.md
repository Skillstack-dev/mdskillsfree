# Reasoning Modes — Full Reference

## Chain-of-Thought (CoT)

**What it is**: Linear, sequential reasoning. Each step builds on the previous one.
Think of it as a single thread of thought that unwinds a problem from start to answer.

**When to trigger:**
- One correct answer exists (math, logic, code debugging)
- Problem has a natural sequence (A must happen before B before C)
- The user asks to "walk through" something
- Time/token budget is tight — ToT costs more

**Structure:**
```
Problem → Step 1 → Step 2 → Step 3 → Answer
```

**Strengths:** Efficient, easy to follow, great for explainability
**Weaknesses:** Misses creative alternatives; one wrong step derails everything

---

## Tree-of-Thought (ToT)

**What it is**: Branching exploration of multiple solution paths. The agent generates 2–4
candidate approaches per decision point, evaluates them, prunes the weak ones, and
continues down the best branch.

**When to trigger:**
- Multiple valid strategies exist (design decisions, business strategy, UX approaches)
- The "best" approach depends on trade-offs the user needs to see
- High stakes — a wrong answer has real costs
- The problem is open-ended or creative

**Structure:**
```
Problem
├── Path A: Approach 1
│   ├── Sub-step A1
│   └── Sub-step A2  ← pruned (score: 3/10)
├── Path B: Approach 2  ← selected (score: 8/10)
│   ├── Sub-step B1
│   └── Sub-step B2
└── Path C: Approach 3  ← pruned (score: 5/10)
    └── ...
```

**Strengths:** Surfaces trade-offs, more robust to wrong starting assumptions
**Weaknesses:** Expensive, can confuse users if branches aren't clearly labeled

**Pruning rules:**
- Score each branch: Feasibility (1–5) + Goal alignment (1–5) = max 10
- Prune any branch scoring ≤ 4
- If all branches score ≤ 4 → re-decompose the problem (go back to Step 2)

---

## Self-Consistency

**What it is**: Run the same problem through CoT N times (typically 3–5), independently,
then compare answers and pick the one that appears most often (majority vote).

**When to trigger:**
- Single correct answer + high stakes (financial, medical, legal reasoning)
- Prior CoT attempt produced a "suspicious" answer
- User explicitly asks to "double-check" or "verify"

**Implementation note:** In a single-agent context without parallel execution, simulate by
running 3 sequential CoT chains with explicit instruction to "approach independently each
time." Then compare and vote.

---

## Reflection + Retry

**What it is**: Mid-reasoning self-critique. When the agent detects an error, contradiction,
or low-confidence moment, it pauses, critiques its own last 1–2 steps, and redoes them.

**When to trigger (auto-detection signals):**
- Step produces a result that contradicts a stated constraint
- Agent writes "I'm not sure" or "approximately" in a step requiring precision
- Two consecutive steps make opposite assumptions
- Final answer doesn't address the original goal

**Max retries:** 2. After 2 retries, surface the uncertainty to the user rather than
continuing to loop.
