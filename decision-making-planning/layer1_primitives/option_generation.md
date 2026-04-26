# Primitive: Option Generation

**Purpose**: Produce a diverse, complete set of candidate solutions.  
**Token cost**: Medium  
**When to use**: After constraints are extracted — generate freely within the constraint space.

---

## Prompt Template

```
OPTION GENERATION

Goal: [GOAL]
Hard Constraints: [LIST]

Generate at minimum 3 options. Each option must:
1. Be genuinely distinct in approach (not just minor variations)
2. Respect all hard constraints
3. Have a clear strategic logic

For each option:
  Name: [Short label]
  Approach: [1-2 sentences on the core method]
  Key bets: [What must be true for this to work]
  Quick wins: [What this does well]
  Key risks: [What could go wrong]
```

---

## Diversity Rules

Force genuine diversity by varying along these axes:

| Axis | Example Options |
|------|----------------|
| Speed | Fast + simple vs Slow + thorough |
| Cost | Cheap + manual vs Expensive + automated |
| Risk | Conservative vs Aggressive |
| Scope | Narrow focus vs Broad approach |
| Control | Build in-house vs Outsource/partner |

---

## Output Format

```
OPTION A — [Name]
Approach: ___
Key bets: ___
Strengths: ___
Risks: ___

OPTION B — [Name]
...

OPTION C — [Name]
...

[OPTION D+ if additional viable paths exist]
```

---

## Rules

- Never stop at 2 options
- Avoid options that are identical except for one detail
- Include at least one "unconventional" option per set
- Mark options that fail soft constraints (but keep them in for comparison)
