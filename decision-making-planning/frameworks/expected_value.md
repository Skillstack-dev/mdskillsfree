# Framework: Expected Value Calculation

**What it is**: A probabilistic model that weights outcomes by their likelihood to find the true average value of a decision.  
**When to use**: Uncertain outcomes, probabilistic bets, comparing risky vs. safe options, resource allocation under uncertainty.

---

## Formula

```
EV = Σ (Probability of outcome × Value of outcome)

EV = (P_success × Value_success) + (P_failure × Value_failure) + ...
```

---

## Prompt Template

```
EXPECTED VALUE ANALYSIS

Option: [NAME]

Define all possible outcomes:
  Outcome 1: [Description]
    Probability: [0.0–1.0]  ← must sum to 1.0 across all outcomes
    Value: [$, time saved, units, or score]

  Outcome 2: [Description]
    Probability: [0.0–1.0]
    Value: [...]

EV = (P1 × V1) + (P2 × V2) + ...

Compare EV across options. Select highest EV unless risk profile rules it out.
```

---

## Example: Launch Strategy Decision

**Option A — Big Bang Launch** (all-in, high spend)

| Outcome | Probability | Value |
|---------|------------|-------|
| Viral hit — 10K users | 10% | $500,000 |
| Moderate success — 2K users | 40% | $80,000 |
| Below expectations — 500 users | 35% | $15,000 |
| Flop — minimal traction | 15% | -$30,000 |

**EV(A)** = (0.10 × $500K) + (0.40 × $80K) + (0.35 × $15K) + (0.15 × -$30K)  
= $50,000 + $32,000 + $5,250 - $4,500 = **$82,750**

---

**Option B — Staged Launch** (MVP first, controlled spend)

| Outcome | Probability | Value |
|---------|------------|-------|
| Strong validation — scale up | 50% | $120,000 |
| Weak signal — pivot | 35% | $10,000 |
| No traction — stop | 15% | -$8,000 |

**EV(B)** = (0.50 × $120K) + (0.35 × $10K) + (0.15 × -$8K)  
= $60,000 + $3,500 - $1,200 = **$62,300**

---

**Selection**: Option A has higher EV ($82,750 vs $62,300) but higher variance. If the organization is risk-averse or cash-constrained, Option B's lower downside ($8K vs $30K) may be preferable despite lower EV.

---

## Risk-Adjusted EV

For risk-averse decisions, apply a penalty to variance:

```
Risk-Adjusted EV = EV - (Risk Aversion Factor × Standard Deviation of outcomes)
```

A risk aversion factor of 0.5 is conservative; 0.1 is risk-neutral.

---

## Rules

- Probabilities must sum to 1.0 — check before calculating
- Always include a downside/failure outcome
- If probability estimates are highly uncertain, run EV for optimistic and pessimistic probability sets
- EV is one input — combine with risk matrix for a complete picture
