# Module: Intent Extractor

## Responsibility
Strip ambiguity from user input. Identify the single, precise action the user needs the AI to perform.

## Process

### 1. Find the Primary Action Verb
Look for the true imperative buried in the request:

| Raw phrase | Extracted intent |
|---|---|
| "I want something that explains..." | EXPLAIN |
| "Can you help me create..." | CREATE |
| "I need a thing that goes through..." | ANALYZE |
| "Write something about..." | WRITE [specific type] |
| "Help me with my..." | [identify exact task] |

### 2. Identify the Real Output
Users often describe the process, not the output. Map to actual deliverable:

| User says | They want |
|---|---|
| "Help me think through X" | Structured analysis or decision framework |
| "Write something for my boss" | Professional memo or summary |
| "Make my prompt better" | Revised prompt with explanation |
| "I need ideas for X" | Enumerated list with brief rationale per item |

### 3. Surface Hidden Requirements
Ask internally (never out loud unless critical):
- What format does the output live in? (doc / email / code / verbal)
- Who is the audience? (self / team / client / public)
- What does "good" mean for this task?
- What is the user afraid of? (too long / too technical / off-brand)

### 4. Discard Noise
Remove from consideration:
- Politeness framing ("if you don't mind", "whenever you get a chance")
- Uncertainty hedges ("maybe", "I think I want", "not sure but")
- Redundant self-identification ("as a [job title]" if role is already obvious from context)

## Output
Single sentence: `[ACTOR] will [ACTION] [OBJECT] for [AUDIENCE] in [FORMAT]`

Example: `AI will write a persuasive product description for e-commerce shoppers in 150-word prose.`
