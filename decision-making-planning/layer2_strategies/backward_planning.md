# Strategy: Backward Planning

**Use when**: End state is fixed, deadline is firm, working backwards from a non-negotiable outcome.  
**Best for**: Launch planning, event execution, compliance deadlines, product releases.  
**Avoid when**: End state is uncertain, or forward momentum is needed to discover the goal.

---

## How It Works

Start from the end state and work backwards to today:

```
END STATE (fixed date) → Last milestone → ... → First action (today)
```

Each step answers: "What must be true immediately before this?"

---

## Prompt Template

```
BACKWARD PLANNING

End state: [WHAT MUST BE ACHIEVED]
Deadline: [DATE]
Today: [DATE]

Working backwards from the end state:
1. What is the final milestone before done? (T-X days)
2. What must be completed before that? (T-Y days)
3. Continue until you reach today.

For each milestone:
  - What: [Deliverable]
  - When: [Date/week]
  - Owner: [Role]
  - Risk: [What could delay this]

Highlight the critical path. Flag any milestone where the timeline is too compressed.
```

---

## Output Format

```
DEADLINE: [Date] — [End state achieved]
  ↑ T-1 week: [Final QA + sign-off]
  ↑ T-3 weeks: [Beta testing complete]
  ↑ T-6 weeks: [Feature freeze]
  ↑ T-10 weeks: [Core development done]
  ↑ T-12 weeks: [Design finalized]
  ↑ TODAY: [Kickoff + team alignment]

⚠️ COMPRESSED ZONE: T-1 to T-3 weeks only allows 2 weeks for QA — recommend 4.
   Options: (a) extend deadline, (b) reduce scope, (c) hire QA contractor
```

---

## Rules

- Never start from today and work forward in this strategy — maintain backward orientation
- Flag every step where duration is shorter than standard/safe
- Offer timeline compression options when schedule is tight
