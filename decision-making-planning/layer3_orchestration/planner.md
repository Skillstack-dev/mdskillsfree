# Layer 3: Planner — Orchestration Entry Point

**Purpose**: Route the incoming problem to the right strategy and coordinate the full decision workflow.  
**When to use**: Any complex problem requiring end-to-end planning.

---

## Routing Logic

```
INCOMING PROBLEM
    │
    ├─ Is end state fixed + deadline firm?
    │   YES → backward_planning.md
    │
    ├─ Is uncertainty HIGH or path unclear?
    │   YES → tree_of_thought.md (explore) or iterative_refinement.md (experiment)
    │
    ├─ Is this a clear sequential project?
    │   YES → linear_planning.md
    │
    └─ Mixed/complex → orchestration (this file)
```

---

## Full Orchestration Workflow

```
PHASE 0: INTAKE (load system_prompt.md)
  → Restate goal
  → Extract constraints [layer1/constraint_extraction.md]
  → Identify uncertainty level

PHASE 1: DECOMPOSE
  → Break goal into sub-goals [layer1/goal_decomposition.md]
  → Flag which sub-goals need separate planning

PHASE 2: GENERATE & EVALUATE
  → Generate options [layer1/option_generation.md]
  → Score options [layer1/evaluation.md]
  → Apply framework [frameworks/decision_matrix.md]

PHASE 3: SELECT & PLAN
  → Route to appropriate strategy [layer2/]
  → Produce execution plan
  → Run risk analysis [layer1/risk_analysis.md]

PHASE 4: OUTPUT
  → Render via [templates/plan_template.md]
  → Assign agents if multi-agent [layer3/multi_agent_coordinator.md]

PHASE 5: HANDOFF
  → Define success metrics
  → Set review checkpoints
  → Define fallback trigger conditions
```

---

## Dynamic Re-planning Triggers

| Signal | Action |
|--------|--------|
| Constraint changes | Re-run Phase 1–2 with new constraints |
| New information invalidates assumption | Re-run Phase 2 for affected options |
| Selected plan fails a milestone | Activate fallback plan |
| New option emerges | Insert into evaluation table, re-score |
| Timeline compresses | Switch to backward planning |
