# Strategy: Iterative Refinement Loop

**Use when**: High uncertainty, learning-as-you-go, plan must adapt to feedback or new information.  
**Best for**: Product discovery, research projects, startup experimentation, creative work.  
**Avoid when**: Speed is critical and iteration is not possible, or the end state is fully known.

---

## How It Works

```
DRAFT PLAN → TEST/VALIDATE → LEARN → REFINE → TEST → ... → CONVERGE
```

Each iteration: plan a small increment, execute, gather signal, update the plan.

---

## Prompt Template

```
ITERATIVE REFINEMENT LOOP

Goal: [GOAL]
Current state: [WHAT WE KNOW NOW]
Uncertainty level: [High / Medium]

Iteration [N]:
  Hypothesis: [What we believe to be true]
  Test: [Smallest action that validates or invalidates the hypothesis]
  Success signal: [How we know this worked]
  Failure signal: [How we know this didn't work]
  Time box: [Max time before reassessing]
  
  IF success → [Next iteration focus]
  IF failure → [Pivot or adjust]

After [X] iterations or when uncertainty drops to Low: switch to Linear Planning.
```

---

## Output Format

```
CURRENT HYPOTHESIS: [Core belief being tested]
CONFIDENCE: [%] — based on [evidence]

ITERATION 1 (THIS WEEK)
  Test: [Action]
  Success: [Signal]
  Failure: [Signal]
  Time box: 5 days

ITERATION 2 (IF ITERATION 1 SUCCEEDS)
  Test: [Next action]
  ...

CONVERGENCE CONDITION: [What makes us switch to committed plan]
ABORT CONDITION: [What signals we should stop entirely]
```

---

## Rules

- Each iteration must be time-boxed (max 2 weeks per loop recommended)
- Every iteration must have a measurable success/failure signal
- Document what you learned, not just what you did
- After 3 failed iterations: escalate to strategy review, don't keep iterating blindly
