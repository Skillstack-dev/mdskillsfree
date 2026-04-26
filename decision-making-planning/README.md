# Decision Making & Planning Skill

**Version**: 1.0.0  
**Compatibility**: Claude, GPT-4, autonomous agents  
**Token budget**: Low–Medium  
**Multi-agent**: ✅

---

A modular, production-ready AI skill package for structured decision-making and planning. Use it to navigate complex choices, build executable plans, and coordinate multi-agent workflows — all with explicit trade-off analysis and justified recommendations.

---

## When to Use This Skill

Trigger this skill whenever you need to:

- Make a decision with multiple options and real trade-offs
- Plan a multi-step project with constraints and dependencies
- Evaluate options using formal scoring frameworks
- Break down a goal into an actionable execution plan
- Assess risks before committing to a path
- Coordinate a plan across multiple agents or people

---

## File Map

```
decision-making-planning.skill/
│
├── SKILL.md                         ← Start here. Layer map + routing guide.
├── system_prompt.md                 ← Core agent directives. Always load.
├── meta.json                        ← Package metadata
├── README.md                        ← This file
│
├── layer1_primitives/               ← Atomic reasoning modules
│   ├── goal_decomposition.md        ← Break goals into sub-goals + tasks
│   ├── constraint_extraction.md     ← Classify hard vs. soft constraints
│   ├── option_generation.md         ← Generate diverse candidate options
│   ├── evaluation.md                ← Score options on explicit criteria
│   └── risk_analysis.md             ← Identify + mitigate risks
│
├── layer2_strategies/               ← Full planning approaches
│   ├── linear_planning.md           ← Sequential, known-path projects
│   ├── tree_of_thought.md           ← Branching exploration of options
│   ├── backward_planning.md         ← Fixed deadline → work backward
│   └── iterative_refinement.md      ← Learn-as-you-go, high uncertainty
│
├── layer3_orchestration/            ← End-to-end workflow coordination
│   ├── planner.md                   ← Routing + full pipeline
│   ├── decision_engine.md           ← Formal selection + justification
│   ├── optimizer.md                 ← Plan optimization (time, risk, resources)
│   └── multi_agent_coordinator.md   ← Multi-agent task breakdown + conflict resolution
│
├── frameworks/                      ← Formal decision frameworks
│   ├── decision_matrix.md           ← Weighted multi-criteria scoring
│   ├── cost_benefit.md              ← Cost vs. benefit over time horizon
│   ├── risk_matrix.md               ← Probability × impact risk scoring
│   └── expected_value.md            ← Probabilistic outcome weighting
│
├── templates/                       ← Standard output formats
│   ├── plan_template.md             ← Full structured output (default)
│   ├── evaluation_table.md          ← Reusable scoring table
│   └── structured_output.md         ← Token-efficient compact format
│
└── examples/                        ← Reference outputs
    ├── startup_decision.md           ← SaaS vs. Agency model choice
    ├── product_strategy.md           ← Q3 roadmap prioritization
    ├── career_decision.md            ← Job offer evaluation
    └── ai_agent_planning.md          ← Competitive intelligence agent architecture
```

---

## Quick Usage Guide

### Minimal (fast decisions)
1. Load `system_prompt.md`
2. Apply `frameworks/decision_matrix.md`
3. Output via `templates/structured_output.md`

### Standard (most decisions)
1. Load `system_prompt.md`
2. Run L1 primitives: `constraint_extraction` → `option_generation` → `evaluation`
3. Apply relevant framework from `frameworks/`
4. Output via `templates/plan_template.md`

### Full Orchestration (complex / multi-agent)
1. Load `system_prompt.md`
2. Enter `layer3_orchestration/planner.md` → routing logic
3. Run all L1 primitives
4. Select L2 strategy
5. Apply `layer3_orchestration/decision_engine.md` + `optimizer.md`
6. For multi-agent: use `multi_agent_coordinator.md`
7. Output via `templates/plan_template.md`

---

## Core Output Rules

- **Always** generate ≥ 3 options before selecting
- **Always** show explicit trade-offs
- **Always** include a fallback plan
- **Never** select a single option without scoring alternatives

---

## License

Open for use in personal, commercial, and agent system projects.
