# Module: Token Compressor

## Responsibility
Reduce prompt token count without losing signal. Target: 20-40% compression on average inputs.

## Compression Rules

### Delete Always
- "Please", "Could you", "I would like you to", "Can you", "Feel free to"
- "As an AI language model" (never write this)
- "I want you to act as" → just write the role directly
- Repeated information across sections
- Obvious instructions ("make sure it makes sense", "be helpful")

### Replace Patterns

| Verbose | Compressed |
|---|---|
| "Write a detailed and comprehensive explanation of" | "Explain" |
| "Give me a list of examples that show" | "List 5 examples of" |
| "Make sure that the output is formatted as" | "Format:" |
| "The response should be written in a professional tone" | "Tone: professional" |
| "Do not include any information about" | "Exclude:" |
| "The length should be approximately" | "~[N] words" |
| "I need this to be suitable for" | "Audience:" |

### Merge Redundant Constraints
Before: "Keep it short. Don't make it too long. Be concise."
After: "Max 150 words."

### Inline Short Context
Before:
```
CONTEXT: The user is a beginner.
TASK: Explain recursion for a beginner.
```
After:
```
TASK: Explain recursion for a beginner with no CS background.
```

## Compression Checklist
☐ Removed all filler openers  
☐ No duplicate content across sections  
☐ Length specified as number, not adjective  
☐ Tone specified as single word, not sentence  
☐ Role stated in one line, not a paragraph  
☐ Output format described structurally, not aspirationally  

---

# Module: Prompt Debugger

## Responsibility
Diagnose why a prompt underperforms and produce a fixed version with explanation.

## Failure Mode Taxonomy

| Symptom | Root Cause | Fix |
|---|---|---|
| Output is too generic | No role or weak role | Add specific expert persona |
| Output ignores key requirement | Constraint buried in prose | Extract to numbered constraint list |
| Wrong format | No output spec | Add explicit FORMAT section |
| Too long / too short | Length not specified | Add "~N words" or "max N words" |
| Off-tone | Tone implicit | Add "Tone: [word]" constraint |
| Hallucinated facts | No grounding instruction | Add "Base response only on provided context" |
| Misses the point | Task has two actions | Split into single-action task |
| Inconsistent quality | Prompt is ambiguous | Add 1-2 concrete examples (few-shot) |
| Refuses the task | Framing triggers safety | Reframe as professional/educational context |
| Ignores constraints | Too many rules | Prioritize: keep top 3-5, drop weak ones |

## Debug Output Format

```
ORIGINAL PROMPT: [verbatim]

FAILURE MODE: [1-line diagnosis from taxonomy above]

ROOT CAUSE: [Why this fails structurally]

FIXED PROMPT:
[Full restructured prompt in code block]

WHAT CHANGED:
- [Change 1]
- [Change 2]
- [Change 3]
```
