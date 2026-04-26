# Framework: Risk Assessment Matrix

**What it is**: A structured method to identify, score, and prioritize risks by probability × impact.  
**When to use**: Before committing to a plan, during execution checkpoints, when uncertainty is high.

---

## Risk Score Grid

|              | Low Impact (1) | Medium Impact (2) | High Impact (3) |
|--------------|---------------|------------------|----------------|
| **High Prob (3)** | 3 — Monitor | 6 — Mitigate | 9 — CRITICAL |
| **Med Prob (2)**  | 2 — Accept   | 4 — Mitigate | 6 — Mitigate  |
| **Low Prob (1)**  | 1 — Accept   | 2 — Accept   | 3 — Monitor   |

**Action thresholds**:
- Score 1–2: Accept (document, no action needed)
- Score 3–4: Monitor (set a tripwire signal)
- Score 5–6: Mitigate (active mitigation plan required)
- Score 7–9: CRITICAL (redesign the plan or escalate)

---

## Prompt Template

```
RISK ASSESSMENT MATRIX

Plan: [SELECTED PLAN]

For each risk:
  Name: [Risk]
  Category: Execution / External / Technical / Financial / People
  Probability: Low(1) / Med(2) / High(3)
  Impact: Low(1) / Med(2) / High(3)
  Score: Probability × Impact
  Action: Accept / Monitor / Mitigate / CRITICAL
  Mitigation: [Specific action to reduce probability or impact]
  Early warning signal: [Observable indicator that risk is materializing]

Sort by Score descending. Focus narrative on Score ≥ 4.
```

---

## Example Output

| # | Risk | Category | Prob | Impact | Score | Action | Mitigation | Warning Signal |
|---|------|----------|------|--------|-------|--------|-----------|---------------|
| 1 | Key engineer leaves | People | 2 | 3 | **6** | Mitigate | Cross-train 2nd engineer; document all systems | Engineer starts disengaging / job searching |
| 2 | Launch delayed by compliance | External | 2 | 2 | **4** | Mitigate | Start compliance review in week 1, not week 8 | Review takes >2 weeks without sign-off |
| 3 | User adoption below target | Execution | 2 | 2 | **4** | Mitigate | Beta test with 20 users before full launch | Beta NPS < 7 |
| 4 | API cost exceeds budget | Technical | 1 | 3 | **3** | Monitor | Set cost alert at 80% of budget | Monthly API cost > $800 |
| 5 | Competitor releases similar product | External | 1 | 2 | **2** | Accept | Monitor competitor, emphasize differentiation | Competitor announcement |

---

## Rules

- Every Score ≥ 4 risk MUST have a concrete mitigation (not "we'll address it if it happens")
- Early warning signals must be observable and measurable
- Revisit the risk matrix at every major milestone
- If a CRITICAL risk (score 9) exists and cannot be mitigated: reconsider the plan
