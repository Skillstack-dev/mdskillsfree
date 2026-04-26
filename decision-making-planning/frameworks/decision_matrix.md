# Framework: Decision Matrix

**What it is**: A weighted scoring model that evaluates multiple options against multiple criteria.  
**When to use**: 2+ options, 2+ criteria, need objective comparison.

---

## How It Works

1. Define criteria and assign weights (weights must sum to 100%)
2. Score each option on each criterion (1–5)
3. Multiply score × weight for each cell
4. Sum weighted scores — highest wins

---

## Prompt Template

```
DECISION MATRIX

Options: [A, B, C]
Criteria and weights:
  - [Criterion 1]: [W]%
  - [Criterion 2]: [W]%
  - [Criterion 3]: [W]%
  (weights sum to 100%)

Score each option on each criterion (1=very low, 5=very high).
Note: For negative criteria (cost, risk), score inversely (1=worst, 5=best).

Calculate: Weighted Score = Σ(score × weight)
Rank options by weighted score.
```

---

## Example

**Decision**: Which project management tool to adopt?  
**Options**: Notion, Linear, Jira  
**Criteria**: Ease of use (30%), Features (25%), Cost (20%), Integration (15%), Team fit (10%)

| Option | Ease (×0.30) | Features (×0.25) | Cost (×0.20) | Integration (×0.15) | Team fit (×0.10) | **Total** |
|--------|-------------|-----------------|-------------|-------------------|-----------------|-----------|
| Notion | 5 → 1.50 | 3 → 0.75 | 4 → 0.80 | 3 → 0.45 | 5 → 0.50 | **4.00** |
| Linear | 4 → 1.20 | 4 → 1.00 | 4 → 0.80 | 4 → 0.60 | 4 → 0.40 | **4.00** |
| Jira   | 2 → 0.60 | 5 → 1.25 | 3 → 0.60 | 5 → 0.75 | 2 → 0.20 | **3.40** |

**Tie between Notion and Linear** → Apply sensitivity analysis or use a tiebreaker criterion.

---

## Rules

- Weights reflect priorities — adjust to context
- Never use equal weights without justification
- If one criterion dominates (>50% weight), question whether the decision is really about that one thing
- Sensitivity test: change top weight by ±10% — does winner change?
