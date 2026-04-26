# Framework: Cost vs. Benefit Analysis

**What it is**: Quantitative comparison of total costs vs. total benefits over a defined time horizon.  
**When to use**: Financial decisions, resource allocation, build vs. buy, invest vs. defer.

---

## Categories

**Costs**
- Direct: money, time, headcount
- Indirect: opportunity cost, distraction, technical debt
- One-time vs. recurring

**Benefits**
- Direct: revenue, savings, efficiency gains
- Indirect: brand, morale, strategic optionality
- Certain vs. probabilistic

---

## Prompt Template

```
COST-BENEFIT ANALYSIS

Option: [NAME]
Time horizon: [X months/years]

COSTS (estimate each):
  Setup/one-time costs: $___
  Recurring monthly costs: $___
  Time cost: [X hours at $Y/hr] = $___
  Opportunity cost: $___
  Total cost (time horizon): $___

BENEFITS (estimate each):
  Direct financial benefit: $___/month × [months] = $___
  Time saved: [X hrs/month × $Y/hr] = $___
  Risk reduction value: $___
  Strategic value: [qualitative or $___]
  Total benefit (time horizon): $___

NET VALUE = Total Benefits - Total Costs = $___
ROI = Net Value / Total Costs = ___%
Payback period = Total Costs / Monthly Net Benefit = ___ months
```

---

## Example

**Decision**: Hire a contractor vs. use internal team for a 3-month project

| | Contractor | Internal Team |
|--|-----------|--------------|
| Setup cost | $0 | $2,000 (onboarding) |
| Monthly cost | $8,000 | $5,000 (allocated) |
| 3-month cost | **$24,000** | **$17,000** |
| Speed benefit | Deliver 4 weeks faster = $12,000 revenue earlier | Baseline |
| Quality risk | Medium | Low |
| Net cost | $24,000 - $12,000 = **$12,000** | **$17,000** |

**Result**: Contractor is cheaper when speed benefit is counted. Internal team wins on quality.

---

## Rules

- Always specify time horizon before calculating
- Flag estimates vs. known costs
- Include opportunity cost — it's often the largest cost
- Probabilistic benefits: multiply by probability (e.g., $100K benefit at 60% = $60K)
