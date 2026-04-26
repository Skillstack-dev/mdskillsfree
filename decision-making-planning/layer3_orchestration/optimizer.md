# Layer 3: Optimizer

**Purpose**: Improve the selected plan by optimizing resource allocation, sequencing, and efficiency.  
**When to use**: After a plan is selected, before execution begins.

---

## Optimization Goals

1. **Minimize time to first value** — resequence so early steps deliver quick wins
2. **Reduce resource waste** — eliminate redundant steps, parallelize where possible
3. **Derisk early** — front-load high-risk steps so failures are caught sooner
4. **Maximize constraint usage** — use available resources fully without overcommitting

---

## Prompt Template

```
PLAN OPTIMIZATION

Selected plan: [PLAN]
Resources: [Team size, budget, tools]
Constraints: [Timeline, dependencies]

Optimization tasks:
1. SEQUENCE: Can any steps be parallelized? List them.
2. QUICK WINS: Which step delivers the first measurable value? Move it earlier if possible.
3. RISK FRONT-LOADING: Which steps have the highest risk? Can they be moved to week 1-2?
4. WASTE: Are there any steps that don't contribute to the goal? Remove or merge them.
5. BUFFER: Where should schedule buffer be added? (Add after high-risk or high-uncertainty steps)
```

---

## Output Format

```
ORIGINAL SEQUENCE: A → B → C → D → E
OPTIMIZED SEQUENCE: A → C (parallel with A) → B → D → E

Changes made:
- C moved earlier: delivers [quick win] in week 1 instead of week 3
- A and C parallelized: saves 1 week
- B delayed: lower risk, can wait until C validates assumption
- Buffer added after D: D has high uncertainty, allow 1 week flex

Resource utilization: [Team/budget at each phase]
First value delivery: [Week X — what gets shipped/decided]
```

---

## Optimization Rules

- Never optimize away a step needed for risk mitigation
- Parallelization requires: different owners OR non-dependent outputs
- Buffer should be explicit, not hidden ("we'll figure it out")
- Quick wins improve momentum and stakeholder confidence — always find one
