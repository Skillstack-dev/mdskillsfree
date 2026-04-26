# Example: Product Roadmap Planning

**Scenario**: A 5-person startup has a working B2B SaaS product with 80 paying customers. They need to plan Q3 roadmap with limited engineering capacity (2 engineers, 1 designer) and must choose between: (A) Doubling down on retention features, (B) Building integrations to drive acquisition, or (C) Adding a new user tier to expand revenue.

---

## DECISION: Q3 Product Roadmap Priority

**Date**: 2024-Q2  
**Type**: Product strategy  
**Urgency**: Medium (quarterly planning cycle)  
**Confidence**: Medium

---

## Goal

Allocate Q3 engineering capacity (2 engineers × 12 weeks) to maximize ARR growth, targeting +40% ARR by Q4.

---

## Constraints

**Hard**
- Engineering: 2 engineers + 1 designer, no new hires
- Budget for tooling/infrastructure: ≤ $5K
- Cannot break existing functionality (80 paying customers at risk)

**Soft**
- Prefer work that compounds (builds on itself)
- Investor update in week 8 — growth metrics must look strong
- Team is fatigued; avoid over-scoping

---

## Assumptions

| Assumption | Confidence | Risk if Wrong |
|-----------|-----------|--------------|
| Churn rate will stay at 8%/month without retention work | Medium | Over-investing in retention if churn is already improving |
| Integrations will reduce sales cycle by 30% | Low | Integration effort wasted if not a true blocker |
| A new pricing tier can generate $15K ARR in Q3 | Medium | Revenue projection misses; looks bad to investors |

---

## Options

### Plan A — Retention Features
Build: in-app onboarding improvements, usage analytics dashboard for users, automated health score alerts.

**Strengths**: Reduces churn (8% → ~5%), protects existing ARR, improves NPS  
**Weaknesses**: Doesn't directly drive new revenue, hard to demo to investors

### Plan B — Integrations (Slack, HubSpot, Zapier)
Build 3 integrations most requested by prospects. Makes product stickier and removes a common sales objection.

**Strengths**: Unlocks new customer segments, speeds up sales cycle, demo-able  
**Weaknesses**: High build complexity, each integration is a new maintenance surface, benefits are delayed

### Plan C — New Pricing Tier (Enterprise/Teams plan)
Add a Teams tier at $199/month (current plan $49/month). Target existing power users + new enterprise prospects.

**Strengths**: Direct revenue uplift, can launch in 4–6 weeks, low engineering complexity  
**Weaknesses**: Requires sales + pricing experimentation, may confuse current customers, needs CS support

---

## Evaluation

*Weights adjusted: Impact 35%, Feasibility 25%, Risk 20%, Cost 10%, Time 10% — growth quarter, impact matters most*

| Option | Feasibility (×0.25) | Impact (×0.35) | Risk (×0.20) | Cost (×0.10) | Time (×0.10) | **TOTAL** |
|--------|--------------------|--------------  |-------------|-------------|-------------|-----------|
| A — Retention | 5 → 1.25 | 3 → 1.05 | 5 → 1.00 | 5 → 0.50 | 4 → 0.40 | **4.20** |
| B — Integrations | 3 → 0.75 | 4 → 1.40 | 3 → 0.60 | 3 → 0.30 | 2 → 0.20 | **3.25** |
| C — New Tier | 4 → 1.00 | 5 → 1.75 | 3 → 0.60 | 4 → 0.40 | 5 → 0.50 | **4.25** |

---

## Selected Plan

**Winner**: Plan C — New Pricing Tier (Score: 4.25, narrow lead over Plan A at 4.20)

**Why**: Direct revenue impact is highest (5/5), fastest to ship (4–6 weeks), and uses existing product strengths. With an investor update in week 8, demonstrable revenue growth matters more than retention improvements that take longer to show in metrics.

**Trade-off vs. Plan A (Retention)**: Plan C doesn't address churn. If churn worsens, new revenue may be offset by losses.

**Why acceptable**: Pair Plan C with a small retention initiative (1 engineer, weeks 1–4) to catch the top churn signals. This is a 70/30 split, not a pure choice.

**Modified Plan**: 
- Engineer 1 + Designer → Teams tier (weeks 1–10)
- Engineer 2 → Retention: onboarding improvements only (weeks 1–4), then joins Teams tier (weeks 5–10)

---

## Execution Steps

| # | Action | Owner | By When | Output |
|---|--------|-------|---------|--------|
| 1 | Define Teams tier features + pricing | PM + Founder | Week 1 | Pricing page spec |
| 2 | Interview 10 current power users on willingness to pay | PM | Week 1–2 | Pricing validation doc |
| 3 | Build Teams tier (permissions, billing, admin dashboard) | Eng 1 + Design | Weeks 2–8 | Teams feature live |
| 4 | Fix top 3 churn-causing friction points | Eng 2 | Weeks 1–4 | Onboarding improvements |
| 5 | Soft launch Teams to 10 existing customers | PM | Week 9 | First Teams upgrades |
| 6 | Full launch + investor update | CEO | Week 10–11 | Revenue milestone + deck |

**First checkpoint**: Week 2 — Pricing validation complete, adjust if willingness-to-pay is lower than expected  
**First value**: Week 9 — first Teams upgrades generate revenue

---

## Top Risks

| # | Risk | Score | Mitigation | Warning Signal |
|---|------|-------|-----------|---------------|
| 1 | Churn spikes while focused on new tier | 6 | Eng 2 fixes top 3 churn triggers in weeks 1–4 | Monthly churn > 10% |
| 2 | Power users don't upgrade (WTP too low) | 6 | Validate pricing with interviews before building | < 3 of 10 interviewees say they'd pay $199 |
| 3 | Teams tier scope creeps past week 8 | 4 | Lock scope at week 3, defer nice-to-haves to Q4 | Feature list grows > 15% from original spec |

---

## Fallback Plan

**Trigger**: Fewer than 5 Teams upgrades by end of week 10  
**Fallback**: Pivot pricing strategy — offer Teams features as add-ons ($29/seat) rather than a new tier; re-run customer interviews to find correct price point  
**Owner**: CEO + PM decide by end of week 10
