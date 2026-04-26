---
name: decision-making-planning
description: >
  A structured decision-making and planning engine for AI agents and humans.
  Use this skill whenever the user needs to: make a complex decision with trade-offs,
  plan a multi-step project or strategy, evaluate options using formal frameworks,
  break down a goal into actionable steps, assess risks before committing to a path,
  or coordinate plans across multiple people or agents. Trigger on phrases like
  "help me decide", "what should I do", "plan this out", "compare my options",
  "I'm stuck between", "build a strategy for", "what are the trade-offs", or any
  situation involving uncertainty + multiple paths forward. Also trigger for product
  roadmaps, career decisions, startup strategy, technical architecture choices, and
  resource allocation problems. When in doubt, use this skill — structured thinking
  always improves outcomes.
---

# Decision Making & Planning Engine

A layered, modular skill for producing structured, justified decisions and executable plans.

## How to Use This Skill

1. **Identify the layer needed** based on complexity:
   - Simple choice → Layer 1 primitives only
   - Multi-step problem → Layer 2 strategy
   - Complex / multi-agent / ongoing → Layer 3 orchestration

2. **Always produce the Standard Output Format** (see `templates/plan_template.md`)

3. **Always offer ≥ 3 alternative plans** before selecting one

4. **Never skip trade-off analysis** — it's the core value of this skill

---

## Layer Map

| Layer | Files | Use When |
|-------|-------|----------|
| **L1 Primitives** | `layer1_primitives/` | Atomic reasoning steps |
| **L2 Strategies** | `layer2_strategies/` | Full planning approaches |
| **L3 Orchestration** | `layer3_orchestration/` | End-to-end workflows |
| **Frameworks** | `frameworks/` | Formal scoring + evaluation |
| **Templates** | `templates/` | Standard output formats |
| **Examples** | `examples/` | Reference outputs |

---

## Quick Start Prompt

When this skill triggers, begin with:

```
You are a Decision Making & Planning Engine. Your job is to:
1. Understand the goal and constraints fully before proposing anything
2. Generate at least 3 distinct plans or options
3. Evaluate each using explicit criteria
4. Select the best option with clear justification
5. Produce an executable action plan with fallbacks

Load: system_prompt.md → identify strategy from layer2_strategies/ → apply frameworks/ → output via templates/plan_template.md
```

---

## File Loading Guide

- **Always load first**: `system_prompt.md`
- **For evaluation**: `frameworks/decision_matrix.md`
- **For output**: `templates/plan_template.md`
- **For complex problems**: `layer3_orchestration/planner.md`
- **For examples**: `examples/` (match to domain)

---

## Token-Efficient Mode

For fast responses, load only:
1. `system_prompt.md` (rules)
2. `templates/plan_template.md` (output format)
3. One framework from `frameworks/`

Skip layer2 strategy files unless the problem requires multi-step planning.
