# Template: Structured Output (Token-Efficient)

Use when brevity is required. Same logic as full plan_template.md — just compressed.

---

```markdown
## DECISION: [Title]

**GOAL**: [1 sentence]
**HARD CONSTRAINTS**: [Comma-separated]
**ASSUMPTIONS**: [Key ones only, flagged if uncertain]

---

**OPTIONS**
- A: [Name] — [One line description]
- B: [Name] — [One line description]
- C: [Name] — [One line description]

**SCORES** (Feasibility / Impact / Risk / Cost / Time → Total)
- A: _ / _ / _ / _ / _ → _
- B: _ / _ / _ / _ / _ → _
- C: _ / _ / _ / _ / _ → _

---

**SELECTED**: Plan [X]
**Why**: [2 sentences max]
**Trade-off**: [What Plan X gives up]

---

**NEXT 3 STEPS**
1. [Action] — [Owner] — [By when]
2. [Action] — [Owner] — [By when]
3. [Action] — [Owner] — [By when]

**TOP RISK**: [Risk] → Mitigation: [Action]
**FALLBACK**: [Plan B trigger + action]
```

---

## When to Use This vs. Full Template

| Use Full Template | Use This Template |
|-------------------|------------------|
| High-stakes decision | Quick operational decision |
| Stakeholder presentation needed | Internal / personal use |
| Multiple reviewers | Single decision-maker |
| Complex trade-offs | Clear winner |
| First time addressing this problem | Recurring decision type |
