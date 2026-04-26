# Template: Evaluation Table

A reusable scoring table for any set of options and criteria.

---

## Standard 5-Criteria Table

```markdown
| Option | Feasibility (×0.25) | Impact (×0.30) | Risk (×0.20) | Cost (×0.15) | Time (×0.10) | **TOTAL** |
|--------|--------------------|--------------  |-------------|-------------|-------------|-----------|
| A      | _ → _              | _ → _          | _ → _       | _ → _       | _ → _       | **_**     |
| B      | _ → _              | _ → _          | _ → _       | _ → _       | _ → _       | **_**     |
| C      | _ → _              | _ → _          | _ → _       | _ → _       | _ → _       | **_**     |
```

*Format: [raw score] → [weighted score] = raw × weight*

---

## Custom Criteria Table (adjust weights to context)

```markdown
Criteria: [C1], [C2], [C3], [C4]
Weights:  [W1]%, [W2]%, [W3]%, [W4]% (must sum to 100%)

| Option | [C1] (×[W1]) | [C2] (×[W2]) | [C3] (×[W3]) | [C4] (×[W4]) | TOTAL |
|--------|-------------|-------------|-------------|-------------|-------|
| A      |             |             |             |             |       |
| B      |             |             |             |             |       |
| C      |             |             |             |             |       |
```

---

## Score Key

| Score | Meaning |
|-------|---------|
| 5 | Excellent / Very strong |
| 4 | Good / Above average |
| 3 | Adequate / Average |
| 2 | Weak / Below average |
| 1 | Very poor / Major concern |

*For inverted criteria (Risk, Cost): 5 = lowest risk/cost (best), 1 = highest (worst)*

---

## Rationale Block (attach below every table)

```
Score Rationales:
Option A — [Criterion]: [Score] because [1-sentence reason]
Option A — [Criterion]: [Score] because [1-sentence reason]
Option B — [Criterion]: [Score] because [1-sentence reason]
...
```
