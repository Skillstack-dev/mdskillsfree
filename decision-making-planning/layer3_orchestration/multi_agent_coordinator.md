# Layer 3: Multi-Agent Coordinator

**Purpose**: Break a plan into sub-tasks, assign to agents, maintain shared context, and resolve conflicts.  
**When to use**: When the plan requires parallel execution across multiple agents or humans.

---

## Agent Roles

| Role | Responsibility |
|------|---------------|
| **Planner Agent** | Maintains the master plan, assigns tasks |
| **Executor Agent** | Executes specific tasks, reports results |
| **Evaluator Agent** | Scores outputs, validates against criteria |
| **Coordinator** | Resolves conflicts, updates shared context |

---

## Task Decomposition for Multi-Agent

```
MULTI-AGENT TASK BREAKDOWN

Master Plan: [PLAN]

For each sub-goal:
  Task ID: [T-001]
  Description: [What must be done]
  Assigned to: [Agent/Role]
  Dependencies: [T-00X must complete first]
  Input: [What the agent needs to start]
  Output: [What the agent must produce]
  Success criteria: [How we know it's done correctly]
  Timeout: [Max time before escalation]
```

---

## Shared Context Schema

```json
{
  "goal": "Master goal statement",
  "status": "in_progress | blocked | complete",
  "constraints": ["list of active constraints"],
  "assumptions": ["list of active assumptions"],
  "tasks": [
    {
      "id": "T-001",
      "status": "pending | active | done | failed",
      "owner": "agent_id",
      "output": null
    }
  ],
  "decisions_made": ["logged decisions with rationale"],
  "open_questions": ["unresolved issues requiring coordination"]
}
```

---

## Conflict Resolution Protocol

```
CONFLICT DETECTED: [Agent A output contradicts Agent B output]

Step 1: Surface both outputs explicitly
Step 2: Identify the specific contradiction
Step 3: Apply decision criteria:
  - Which output better satisfies the goal?
  - Which aligns better with constraints?
  - Which has stronger evidence?
Step 4: Select one output OR merge if compatible
Step 5: Log the resolution in shared context
Step 6: Notify affected downstream agents
```

---

## Escalation Rules

- Task exceeds timeout → Planner Agent reassigns or descopes
- Conflict unresolvable by criteria → Escalate to human decision-maker
- Assumption invalidated → Halt dependent tasks, re-plan
- 2+ agents blocked on same dependency → Prioritize that dependency immediately
