# Prompt Templates

Ready-to-use templates for each layer of the Token Efficiency System.
Variables in [BRACKETS] are required. Variables in {curly} are optional.

---

## System Prompt Templates

### SYSTEM_COMPACT
Minimal system prompt for token-sensitive deployments:
```
You are a [ROLE]. {Context: [CONTEXT].}
Rules: Be concise. No preamble. No sign-off. Answer only what is asked.
Output: [FORMAT]
```

### SYSTEM_STRUCTURED
For extraction and classification tasks:
```
You are a [ROLE].
Input: [INPUT_DESCRIPTION]
Output: [JSON_SCHEMA or FORMAT]
Rules: Return output only. No explanation. No markdown outside code blocks.
```

---

## Compression Templates

### MEMORY_COMPRESS
Used by Memory Summarization Layer to compress conversation history:
```
Compress this conversation to ≤100 words.
Keep: decisions, user preferences, unresolved questions, key facts.
Remove: pleasantries, repeated questions, verbose explanations.

[CONVERSATION_HISTORY]
```

### CONTEXT_SUMMARIZE
For summarizing a retrieved document chunk:
```
In ≤50 words, summarize the key facts from this text relevant to: [QUERY]

[TEXT]
```

---

## Task Templates

### CODE_REVIEW
```
Review [LANGUAGE] code.
Find: [bugs | performance | style | security] issues.
Return: [inline comments | numbered list | fixed code only]
[CODE]
```

### DATA_EXTRACT
```
Extract from text:
[FIELD_1]: [type]
[FIELD_2]: [type]
{[FIELD_3]: [type]}
Return JSON only. If field missing, use null.

[TEXT]
```

### CLASSIFY
```
Classify input as one of: [CLASS_1 | CLASS_2 | CLASS_3]
Return label only.

Input: [TEXT]
```

### SUMMARIZE
```
Summarize in [N] words/{bullets}.
Keep: [key points].
{Audience: [AUDIENCE]}

[TEXT]
```

### TRANSLATE
```
Translate to [LANGUAGE]. Preserve tone. Return translation only.

[TEXT]
```

### QA_FACTUAL
```
Answer in ≤2 sentences. Cite source if known.

Q: [QUESTION]
{Context: [CONTEXT]}
```

### QA_ANALYSIS
```
Analyze: [TOPIC]
Structure:
- Summary (1 sentence)
- Key findings (3 bullets max)
- Recommendation (1 sentence)
Max 200 words total.
```

---

## Output Constraint Suffixes

Append to any prompt to enforce output format:

### NO_PREAMBLE
```
No preamble. No sign-off. Answer directly.
```

### JSON_ONLY
```
Return valid JSON only. No markdown. No explanation.
```

### BULLETS_ONLY
```
Return bulleted list only. No intro. No conclusion.
```

### CODE_ONLY
```
Return code only. No explanation. Include inline comments only where non-obvious.
```

### ONE_SENTENCE
```
Answer in exactly one sentence.
```

### WORD_LIMIT
```
Max [N] words. Cut ruthlessly.
```

---

## Reasoning Control Suffixes

### ENABLE_COT
```
Think step by step before answering.
```

### SUPPRESS_COT
```
Return the final answer only. Do not show reasoning.
```

### BRIEF_COT
```
Think briefly (≤3 steps), then answer.
```

### CONFIDENCE_ONLY
```
Return answer and confidence (high/medium/low). No explanation.
```

---

## Token Budget Templates

### BUDGET_INSTRUCTION
Inject into system prompt when using a strict budget:
```
Token budget: [N] total.
Allocate: ~[INPUT_PCT]% context, ~[OUTPUT_PCT]% response.
If answer would exceed budget, summarize key points only.
```

### DYNAMIC_LENGTH
Task-adaptive length instruction:
```
Response length: 
- Simple factual: 1-2 sentences
- Step-by-step: numbered list, 1 line per step
- Analysis: 3 sections max, 100 words each
- Code: code block only
```

---

## Anti-Pattern Reference

Prompts that WASTE tokens — replace with templates above:

| Anti-Pattern | Token Cost | Replace With |
|-------------|-----------|--------------|
| "Please help me with the following task if you don't mind..." | +15 tokens | "Do:" |
| "I'll now provide you with the code..." | +12 tokens | "[CODE]" label |
| "Feel free to ask if you need clarification" | +10 tokens | DELETE |
| "As per the above instructions..." | +8 tokens | DELETE |
| "Here is my question:" (then asks question) | +5 tokens | Just ask |
| "The answer is:" (before answering) | +4 tokens | Just answer |
