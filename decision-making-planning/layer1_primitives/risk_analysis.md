# Primitive: Risk Identification & Analysis

**Purpose**: Surface, quantify, and mitigate risks for the selected plan.  
**Token cost**: Low–Medium  
**When to use**: After selection, before execution planning.

---

## Risk Categories

| Category | Examples |
|----------|---------|
| **Execution** | Team capacity, skill gaps, timeline slippage |
| **External** | Market shifts, competitor moves, regulatory changes |
| **Technical** | Integration failures, scalability issues, data quality |
| **Financial** | Cost overruns, revenue shortfalls, funding delays |
| **People** | Key person dependency, alignment failures |

---

## Prompt Template

```
RISK ANALYSIS

Plan: [SELECTED PLAN]

For each risk:
1. Name the risk
2. Category (Execution/External/Technical/Financial/People)
3. Probability: Low / Medium / High
4. Impact if occurs: Low / Medium / High
5. Risk Score: Probability × Impact (1=Low×Low … 9=High×High)
6. Mitigation: What to do to prevent or reduce
7. Trigger: Signal that this risk is materializing
8. Fallback: What to do if it occurs despite mitigation

Focus on the top 5 risks by score.
```

---

## Output Format

```
| # | Risk | Category | Prob | Impact | Score | Mitigation | Trigger | Fallback |
|---|------|----------|------|--------|-------|-----------|---------|---------|
| 1 | API rate limits | Technical | Med | High | 6 | Cache responses + throttle | >80% quota used | Switch to alternative API |
| 2 | ... |
```

---

## Rules

- Score = Probability × Impact (1=L×L, 4=M×M, 9=H×H, 6=H×M, etc.)
- Prioritize risks with Score ≥ 4
- Every risk must have a concrete mitigation — "monitor it" is not a mitigation
- Every fallback must be pre-decided, not reactive
