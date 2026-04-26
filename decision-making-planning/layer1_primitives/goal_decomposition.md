# Primitive: Goal Decomposition

**Purpose**: Break a high-level goal into a hierarchy of sub-goals and atomic tasks.  
**Token cost**: Low  
**When to use**: Always — this is step 1 of every planning workflow.

---

## Prompt Template

```
GOAL DECOMPOSITION

Input goal: [GOAL]

Step 1 — Restate the goal in one clear sentence.
Step 2 — Identify the end state: what does success look like?
Step 3 — Break into 3–5 major sub-goals.
Step 4 — For each sub-goal, list 2–4 tasks.
Step 5 — Mark dependencies between tasks (which must happen before others).

Output as:
GOAL → SUB-GOALS → TASKS → DEPENDENCIES
```

---

## Output Format

```
Goal: [Restated in 1 sentence]
Success State: [What done looks like]

Sub-Goal 1: ___
  Tasks: A, B, C
Sub-Goal 2: ___
  Tasks: D, E
Sub-Goal 3: ___
  Tasks: F, G, H

Dependencies:
  D depends on A
  F depends on D, B
```

---

## Rules

- Sub-goals must be independent where possible
- Tasks must be actionable (start with a verb)
- Surface blockers as explicit dependencies
- If the goal is vague, rewrite it before decomposing
