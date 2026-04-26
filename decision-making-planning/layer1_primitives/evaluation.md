# Primitive: Scoring & Evaluation

**Purpose**: Score all options against explicit criteria to enable objective comparison.  
**Token cost**: Medium  
**When to use**: After option generation, before selection.

---

## Standard Scoring Criteria

| Criterion | Definition | Scale |
|-----------|-----------|-------|
| **Feasibility** | Can we actually do this given our constraints? | 1–5 |
| **Impact** | How much does success move the needle? | 1–5 |
| **Risk** | Probability × severity of failure (lower = better) | 1–5 (inverted) |
| **Cost** | Total resource cost (time + money + effort) | 1–5 (inverted) |
| **Time** | How quickly can this deliver value? | 1–5 |

Default weights: Feasibility 25%, Impact 30%, Risk 20%, Cost 15%, Time 10%  
Adjust weights based on context (e.g., time-critical = Time weight ↑)

---

## Prompt Template

```
EVALUATION

Options: [LIST]
Weights: Feasibility [W1]%, Impact [W2]%, Risk [W3]%, Cost [W4]%, Time [W5]%

Score each option on each criterion (1=lowest, 5=highest).
For Risk and Cost: 5 = lowest risk/cost (inverted so higher = better).

Provide a 1-sentence rationale for each score.
Calculate weighted total. Rank options.
```

---

## Output Format

```
| Option | Feasibility | Impact | Risk | Cost | Time | TOTAL |
|--------|------------|--------|------|------|------|-------|
| A      | 4 (0.25)   | 5 (0.30)| 3 (0.20)| 2 (0.15)| 4 (0.10)| 3.75 |
| B      | 3          | 4      | 4    | 4    | 3    | 3.65  |
| C      | 5          | 3      | 5    | 5    | 2    | 4.05  |

Score rationales:
Option A — Feasibility 4: Team has 80% of required skills; missing DevOps expertise.
Option A — Risk 3: Depends on external API with no SLA guarantee.
...
```

---

## Rules

- Every score needs a rationale (one sentence minimum)
- If two options tie, examine the rationale — ties often hide real differences
- Flag any score that is based on an assumption rather than fact
