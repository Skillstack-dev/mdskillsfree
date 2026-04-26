---
name: token-efficiency
description: >
  Optimize token usage across Claude, ChatGPT, Gemini, and other LLMs — minimizing cost and latency while preserving output quality. Use this skill whenever: the user wants to reduce API costs, compress long prompts, manage context windows, build token-aware middleware, set up token budgets, optimize prompts for production, or asks about prompt efficiency, context management, or output control. Trigger even if they just say "make this cheaper", "my prompt is too long", "hitting context limits", or "I want faster responses". This skill provides architecture, code, and ready-to-use templates.
compatibility: "tools: bash, create_file, present_files | languages: python, javascript"
---

# Token Efficiency Skill

A complete system for minimizing token consumption across LLMs while preserving quality. Covers architecture, compression rules, budgeting logic, and working code.

---

## Quick Start (read this first)

When this skill triggers, determine the user's primary goal:

| User Need | Jump To |
|-----------|---------|
| Understand the architecture | [Architecture Overview](#architecture-overview) |
| Compress an existing prompt | [Prompt Compression Layer](#1-prompt-compression-layer) + `references/compression-rules.md` |
| Manage context / history | [Context Selection Layer](#2-context-selection-layer) |
| Control output length | [Output Constraint Controller](#4-output-constraint-controller) |
| Build a middleware wrapper | `references/prompt-templates.md` + `scripts/token_optimizer.py` |
| Set token budgets | [Token Budgeting](#token-budgeting) |
| Before/after comparison | [Example Transformations](#example-transformations) |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    TOKEN EFFICIENCY SYSTEM                   │
│                                                             │
│  RAW INPUT                                                  │
│      │                                                      │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  1. PROMPT COMPRESSION  │  Remove redundancy, rewrite   │
│  │     LAYER               │  verbose → minimal semantic   │
│  └──────────┬──────────────┘                               │
│             │                                               │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  2. CONTEXT SELECTION   │  Pick only relevant history   │
│  │     LAYER               │  + retrieval-based context    │
│  └──────────┬──────────────┘                               │
│             │                                               │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  3. MEMORY              │  Compress long histories      │
│  │     SUMMARIZATION LAYER │  into dense summaries         │
│  └──────────┬──────────────┘                               │
│             │                                               │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  4. TOKEN BUDGET        │  Allocate input / context /   │
│  │     ALLOCATOR           │  output tokens by task type   │
│  └──────────┬──────────────┘                               │
│             │                                               │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  5. REASONING CONTROL   │  Chain-of-thought ON/OFF      │
│  │     LAYER               │  based on task complexity     │
│  └──────────┬──────────────┘                               │
│             │                                               │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  6. OUTPUT CONSTRAINT   │  Dynamic length limits,       │
│  │     CONTROLLER          │  format enforcement           │
│  └──────────┬──────────────┘                               │
│             │                                               │
│      ▼                                                      │
│  ┌─────────────────────────┐                               │
│  │  7. SELF-IMPROVEMENT    │  Track usage, detect waste,   │
│  │     LOOP                │  recompress automatically     │
│  └─────────────────────────┘                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### 1. Prompt Compression Layer

**Goal:** Reduce input tokens by 30–60% with zero meaning loss.

**Rules (full list in `references/compression-rules.md`):**
- Strip filler phrases: "Please", "Could you kindly", "I would like you to"
- Remove repeated context already in system prompt
- Replace verbose descriptions with structured formats
- Convert paragraph instructions → numbered steps or JSON schema
- Deduplicate examples (keep 1–2 max)
- Use abbreviations for repeated terms (define once, reference after)

**Trigger when:** prompt > 300 tokens OR user says "this prompt is too long"

---

### 2. Context Selection Layer

**Goal:** Pass only the context tokens that influence the answer.

**Strategies:**
- **Recency window:** keep last N turns (default: 3–5 for chat, 1 for single-shot)
- **Relevance scoring:** cosine similarity between current query and history chunks; keep top-k
- **Role filtering:** skip assistant turns that were purely confirmations ("Got it!", "Sure!")
- **RAG substitution:** replace long documents with retrieved chunks (max 3 chunks × 200 tokens)

**When to use full history:** legal/compliance tasks, debugging sessions, explicit "remember everything" instructions

---

### 3. Memory Summarization Layer

**Goal:** Compress multi-turn history without losing key facts.

**Compression prompt (see `references/prompt-templates.md` → `MEMORY_COMPRESS`):**
```
Summarize the following conversation. Keep: decisions made, user preferences, unresolved issues, key facts. Discard: pleasantries, repeated questions, verbose explanations. Max 100 words.
```

**Trigger:** conversation history > 2000 tokens → auto-summarize oldest 50%

---

### 4. Output Constraint Controller

**Goal:** Prevent over-generation.

| Task Type | Output Strategy |
|-----------|----------------|
| Factual Q&A | Max 2 sentences |
| List/enumeration | Bullets only, no preamble |
| Code | Code block only, no explanation unless asked |
| Analysis | Structured sections, 150-word cap per section |
| Creative | Word count specified in prompt |

**Enforcement phrase to append to prompts:**
```
Respond in [FORMAT]. Max [N] words/tokens. No preamble. No sign-off.
```

---

### 5. Reasoning Control Layer

**Goal:** Pay for chain-of-thought only when it improves accuracy.

| Condition | CoT Setting |
|-----------|-------------|
| Math / logic / multi-step | ON — append "Think step by step." |
| Classification / extraction | OFF — append "Return only the answer." |
| Simple lookup / reformat | OFF — no reasoning instruction |
| Ambiguous task | ON with budget: "Think briefly, then answer." |

---

## Token Budgeting

**Default allocation by task type:**

```
TASK: simple_qa
  input:    60%  (prompt + compressed context)
  reasoning: 0%
  output:   40%  (answer)

TASK: analysis
  input:    45%
  reasoning: 20%
  output:   35%

TASK: code_generation
  input:    40%
  reasoning: 15%
  output:   45%

TASK: summarization
  input:    70%  (source material)
  reasoning: 5%
  output:   25%
```

**Dynamic adjustment logic:**
- If task_complexity > 0.7 (scored 0–1): increase reasoning budget by 10%, reduce output
- If user requests "brief/short/concise": cap output at 25% of total budget
- If model = GPT-3.5 or Haiku: reduce output budget by 15% (smaller context = less waste tolerated)

---

## Model Profiles

See `references/model-profiles.md` for per-model settings. Summary:

| Model | Context Window | CoT Efficiency | Compression Sensitivity |
|-------|---------------|----------------|------------------------|
| GPT-4o | 128k | High | Low (verbose ok) |
| GPT-3.5-turbo | 16k | Medium | High |
| Claude 3.5 Sonnet | 200k | Very High | Low |
| Claude 3 Haiku | 200k | Medium | High |
| Gemini 1.5 Pro | 1M | High | Low |
| Gemini 1.5 Flash | 1M | Medium | High |
| Llama 3 70B | 8k | Low | Very High |

---

## Example Transformations

### Prompt Compression — Before / After

**Before (127 tokens):**
```
Hello! I hope you're doing well. I was wondering if you could please help me 
with something. I would really appreciate it if you could take a look at the 
following Python code that I have written and tell me what might be wrong with 
it, and also maybe suggest how I could potentially fix it if there are any 
issues. The code is supposed to sort a list but I think there might be a bug.
```

**After (28 tokens):**
```
Debug this Python sort function. Identify the bug and fix it.
[CODE]
```
> **Savings: 78% token reduction**

---

### Context Selection — Before / After

**Before (full history, 1,840 tokens):**
```
Turn 1: User asks about project setup (resolved)
Turn 2: User asks about dependencies (resolved)  
Turn 3: User asks about auth flow (resolved)
Turn 4: User asks about deployment (resolved)
Turn 5: User asks about the error on line 42 ← CURRENT
```

**After (relevant context only, 210 tokens):**
```
[SUMMARY: User building Node.js app, auth uses JWT, deploys to Vercel]
Turn 5: User asks about error on line 42
```
> **Savings: 89% token reduction**

---

## Implementation

For full code, read: `scripts/token_optimizer.py`

This script provides:
- `TokenOptimizer` class (Python) — wraps any OpenAI-compatible API
- `compress_prompt()` — applies compression rules
- `select_context()` — relevance-based history trimming
- `enforce_output()` — appends output constraint instructions
- `optimize()` — full pipeline in one call

**Quick usage:**
```python
from token_optimizer import TokenOptimizer

optimizer = TokenOptimizer(model="claude-sonnet-4-20250514", total_budget=4000)
result = optimizer.optimize(
    system="You are a helpful assistant.",
    history=conversation_history,
    user_message="Debug my sort function.",
    task_type="code_generation"
)
# result.optimized_messages → pass to your LLM API
# result.token_estimate → estimated tokens before calling
# result.savings_report → dict of savings per layer
```

---

## Self-Improvement Loop

After each API call, log:
```python
{
  "original_tokens": 1840,
  "optimized_tokens": 210,
  "output_tokens": 145,
  "quality_score": null,  # fill from user feedback or auto-eval
  "task_type": "debug"
}
```

Every 50 calls (or on demand), run the compression audit:
- Find prompts where `output_tokens / optimized_tokens > 0.8` (output dominated — over-prompted)
- Find prompts where quality_score < 0.7 (compressed too aggressively)
- Adjust compression rules accordingly

See `scripts/token_optimizer.py` → `SelfImprovementLoop` class for automated version.

---

## Trade-offs & Limitations

| Trade-off | Detail |
|-----------|--------|
| Compression vs accuracy | Over-compressing ambiguous prompts causes misunderstanding. Always keep task intent 100% intact. |
| Context trimming vs coherence | Removing old turns can cause the model to "forget" prior decisions. Use summaries, not deletion. |
| Output constraints vs completeness | Hard token caps can truncate code. Use format constraints (JSON/bullets) instead of word limits for code. |
| Model-agnostic tokenization | Token counts vary by model. This system uses word-based estimates (~1.3 tokens/word). Use tiktoken or model-specific counters for precision. |
| CoT suppression | Turning off reasoning for complex tasks reduces accuracy. Use the complexity scorer in `scripts/token_optimizer.py` to automate this safely. |

---

## Files in This Skill

- `SKILL.md` — This file (architecture + guidance)
- `references/compression-rules.md` — Full ruleset for prompt compression
- `references/model-profiles.md` — Per-model token settings and quirks
- `references/prompt-templates.md` — Ready-to-use prompt templates for all layers
- `scripts/token_optimizer.py` — Python implementation (class-based, production-ready)
