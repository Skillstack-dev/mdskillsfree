# Primitive: Constraint Extraction

**Purpose**: Identify and classify all constraints that limit the solution space.  
**Token cost**: Low  
**When to use**: Before generating options — constraints eliminate infeasible plans.

---

## Prompt Template

```
CONSTRAINT EXTRACTION

Context: [GOAL + SITUATION]

Identify and classify all constraints:

HARD CONSTRAINTS (non-negotiable — violating eliminates the option):
- Budget: ___
- Timeline: ___
- Legal/Compliance: ___
- Technical: ___
- Resource: ___

SOFT CONSTRAINTS (preferences — violating reduces the score):
- Preferred approach: ___
- Risk tolerance: ___
- Team preferences: ___
- Brand/values alignment: ___

ASSUMPTIONS (things believed true but not confirmed):
- ___

Flag: Any constraint that is assumed but not confirmed.
```

---

## Output Format

```
HARD CONSTRAINTS
| Type | Constraint | Source |
|------|-----------|--------|
| Budget | ≤ $50K | Stated |
| Timeline | Live in 3 months | Stated |

SOFT CONSTRAINTS
| Type | Preference | Weight |
|------|-----------|--------|
| Risk | Low risk preferred | Medium |

ASSUMPTIONS (unconfirmed)
- Market exists for product X [HIGH RISK if wrong]
```

---

## Rules

- Hard constraints are filters — apply before scoring
- Soft constraints are inputs to scoring weights
- Always surface assumptions explicitly
- Ask for clarification if a critical constraint is missing
