# Layer 3: Decision Engine

**Purpose**: Apply formal decision frameworks to produce a justified, defensible selection.  
**When to use**: When scoring alone is insufficient — high-stakes decisions, competing values, or stakeholder accountability required.

---

## Decision Engine Pipeline

```
INPUT: Evaluated options with scores
  ↓
STEP 1: Constraint filter (eliminate hard violations)
  ↓
STEP 2: Dominance check (does any option win on ALL criteria?)
  ↓
STEP 3: Framework application (see below)
  ↓
STEP 4: Sensitivity analysis (does the ranking change with different weights?)
  ↓
STEP 5: Justified selection output
```

---

## Framework Selection Guide

| Situation | Use |
|-----------|-----|
| Multiple quantifiable criteria | Decision Matrix |
| Financial decision | Cost-Benefit + Expected Value |
| High-stakes with uncertainty | Risk Matrix + Expected Value |
| Values conflict between options | Decision Matrix with custom weights |

Load the relevant framework from `frameworks/`.

---

## Dominance Check Prompt

```
DOMINANCE CHECK

For each pair of options (A vs B):
Does A score ≥ B on ALL criteria?
  YES → A dominates B → eliminate B
  NO → keep both

If one option dominates all others → select immediately.
If no dominance → proceed to weighted scoring.
```

---

## Sensitivity Analysis

```
SENSITIVITY ANALYSIS

Base ranking: [A > B > C]

Test 1: Double the weight of Risk
  New ranking: [___]
  Rank stable? [Yes/No]

Test 2: Double the weight of Cost
  New ranking: [___]
  Rank stable? [Yes/No]

If rank changes: flag to decision-maker. The choice depends on values, not facts alone.
```

---

## Justified Selection Output

```
SELECTED: Option [X]

Beats [Y] because: [specific score advantage on key criteria]
Beats [Z] because: [specific score advantage on key criteria]

What Option [X] sacrifices vs. [Y]: [explicit trade-off]
Why that trade-off is acceptable: [reasoning]

This selection is robust to: [weight changes that don't affect ranking]
This selection is sensitive to: [assumptions that, if wrong, would change the answer]
```
