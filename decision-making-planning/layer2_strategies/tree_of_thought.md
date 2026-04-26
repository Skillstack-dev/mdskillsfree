# Strategy: Tree-of-Thought Planning

**Use when**: Multiple viable paths exist, high uncertainty, creative solutions needed, or exploring a problem space.  
**Best for**: Strategic decisions, product direction, ambiguous problems, innovation challenges.  
**Avoid when**: Answer is clear, time is short, or computational simplicity is needed.

---

## How It Works

```
GOAL
├── Branch A: Approach 1
│   ├── A1: Sub-option
│   └── A2: Sub-option  ← prune if infeasible
├── Branch B: Approach 2
│   ├── B1: Sub-option  ← highest promise
│   └── B2: Sub-option
└── Branch C: Approach 3
    └── C1: Sub-option
```

At each branch: evaluate, score, prune weak branches, deepen promising ones.

---

## Prompt Template

```
TREE-OF-THOUGHT PLANNING

Goal: [GOAL]
Constraints: [CONSTRAINTS]

Round 1 — Generate 3 top-level strategic approaches (branches).
Round 2 — For each branch, generate 2 sub-options.
Round 3 — Score each leaf (1-5 on Feasibility + Impact). Prune < 3.
Round 4 — Deepen the top 2 leaves: break into execution steps.
Round 5 — Select the winning leaf. Justify vs. runner-up.
```

---

## Output Format

```
ROOT: [Goal]

BRANCH A — [Approach name]  Score: 3.2
  A1 — [Sub-option]  Score: 2.8 → PRUNED
  A2 — [Sub-option]  Score: 4.1 → DEEPEN

BRANCH B — [Approach name]  Score: 4.0
  B1 — [Sub-option]  Score: 4.5 → WINNER
  B2 — [Sub-option]  Score: 3.6 → Runner-up

BRANCH C — [Approach name]  Score: 2.5 → PRUNED

WINNER: B1 — [Full execution plan]
Runner-up: A2 — [Why not chosen]
```

---

## Pruning Rules

- Score < 3.0 on Feasibility: prune immediately (hard constraint violation)
- Score < 2.5 combined: prune
- Only deepen top 2–3 leaves to manage token cost
