# Module: Chain Builder

## Responsibility
Design multi-step prompt sequences where each step's output feeds the next. Used when a single
prompt cannot accomplish the full task without intermediate reasoning or transformation.

## When to Chain
- Task requires gathering → synthesizing → formatting (3 distinct cognitive modes)
- Output of step 1 is genuinely unknown before step 2 can be written
- Quality control requires a separate review pass
- Different roles are optimal for different steps

## Chain Template

```
═══════════════════════════════
CHAIN: [Chain Name]
STEPS: [N]
GOAL: [Final output description]
═══════════════════════════════

─── STEP 1: [Step Name] ───────
ROLE: [Persona]
TASK: [Single imperative]
INPUT: [What this step receives]
CONSTRAINTS: [Rules]
OUTPUT FORMAT: [Exact spec]
PASS FORWARD: [Field name or format to extract for Step 2]

─── STEP 2: [Step Name] ───────
ROLE: [Persona — may differ from Step 1]
TASK: [Single imperative]
INPUT: {{STEP_1_OUTPUT}} — [Brief description of what this is]
CONSTRAINTS: [Rules]
OUTPUT FORMAT: [Exact spec]
PASS FORWARD: [Field name or format to extract for Step 3]

─── STEP N: [Final Step] ──────
ROLE: [Persona]
TASK: [Synthesis or formatting imperative]
INPUT: {{STEP_[N-1]_OUTPUT}}
CONSTRAINTS: [Rules]
OUTPUT FORMAT: [Final deliverable spec]
```

## Chain Patterns

### Research → Draft → Polish
```
Step 1: ANALYZE (extract key facts, structure findings)
Step 2: DRAFT (write from findings, don't research again)
Step 3: EDIT (improve only — no new content)
```

### Audit → Fix → Verify
```
Step 1: AUDIT (list all issues, categorize by severity)
Step 2: FIX (address each issue from the audit list)
Step 3: VERIFY (confirm each fix resolves its issue)
```

### Explore → Select → Execute
```
Step 1: GENERATE (produce 5-10 options without evaluating)
Step 2: EVALUATE (score each against criteria, pick top 1-2)
Step 3: EXECUTE (build the selected option in full)
```

## State Handoff Rules
- Always name what you're passing: `PASS FORWARD: The 3 ranked options as a numbered list`
- Use `{{STEP_N_OUTPUT}}` as the variable placeholder — never say "use the previous response"
- If step output is long, specify what to extract: `PASS FORWARD: Section titled "Findings" only`

## Anti-patterns to Avoid
- Chaining when a single well-structured prompt would work
- Steps that do two cognitive tasks ("research AND draft")
- Ambiguous handoffs ("use what came before")
- More than 4 steps without a human review checkpoint
