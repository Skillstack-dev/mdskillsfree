# Strategy: Linear Planning

**Use when**: Goal is clear, path is known, dependencies are sequential, low uncertainty.  
**Best for**: Projects with defined start → end, operational tasks, process improvements.  
**Avoid when**: High uncertainty, multiple parallel workstreams, creative exploration needed.

---

## Prompt Template

```
LINEAR PLANNING

Goal: [GOAL]
Constraints: [CONSTRAINTS]

Produce a step-by-step plan where:
- Each step builds directly on the previous
- Steps are ordered by dependency
- Each step has: Action, Owner, Duration, Output/Deliverable

Format as a sequential milestone list.
Mark any step that is on the critical path (delay = project delay).
```

---

## Output Format

```
PHASE 1: [Name] — [Duration]
  Step 1.1: [Action verb + what] → Output: [Deliverable]
  Step 1.2: [Action verb + what] → Output: [Deliverable]  ← CRITICAL PATH

PHASE 2: [Name] — [Duration]
  Step 2.1: [Action] → Output: [Deliverable]
  ...

Critical Path: 1.2 → 2.1 → 3.1
Total Timeline: [X weeks/days]
First decision point: [Step + date]
```

---

## When to Switch Strategies

- Uncertainty appears mid-plan → switch to **Iterative Refinement**
- Multiple valid paths emerge → switch to **Tree-of-Thought**
- Working backward from a deadline → switch to **Backward Planning**
