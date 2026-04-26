---
name: context-intelligence
description: >
  Context Intelligence: Memory & RAG — a production-ready AI skill for managing
  conversational memory, knowledge retrieval, and context injection. Invoke this
  skill whenever an agent needs to remember prior interactions, retrieve relevant
  documents, or intelligently assemble context before generating a response.
  Trigger on phrases like: "remember this", "what did I say about", "find relevant
  docs", "use my history", "based on previous context", "look this up in my knowledge
  base", or whenever a multi-turn task requires persistent state or grounded answers.
  This skill handles the full pipeline: memory read → retrieval → context fusion →
  prompt construction → response → memory write.
version: "1.0.0"
category: memory-retrieval
tags:
  - memory
  - RAG
  - context
  - retrieval
  - embeddings
  - vector-search
  - long-context
  - agents
author: generated
compatible_with:
  - claude
  - chatgpt
  - agents
---

# Context Intelligence: Memory & RAG

A complete agent skill for context-aware AI systems. Agents using this skill
never answer cold — they always check what they know (memory) and what they
can retrieve (RAG) before generating a response.

---

## 1. PURPOSE

| Dimension | Detail |
|-----------|--------|
| **Problem** | LLMs forget prior turns, hallucinate on domain facts, and lose context in long sessions. |
| **When to invoke** | Any query that benefits from history, grounded docs, or persistent user state. |
| **Inputs** | `query` (string), `session_id`, optional `user_id`, optional `domain` tag. |
| **Outputs** | `response` (string), updated memory objects, `sources[]` used in answer. |

---

## 2. CORE CAPABILITIES

### Module A — Memory Management
- Read/write short-term (session) and long-term (user profile) memory.
- Detect memory conflicts and resolve by recency or confidence score.
- Summarize stale memory to free token budget.

### Module B — Context Filtering
- Score candidate memory chunks by query relevance (semantic + recency).
- Prune low-signal context before injecting into the prompt.
- Apply domain tags to restrict retrieval scope.

### Module C — Retrieval (RAG)
- Embed query → vector search → top-K candidates → re-rank → assemble.
- Support hybrid search: dense (semantic) + sparse (BM25 keyword).
- Handle empty retrieval gracefully (fallback to memory-only or parametric).

### Module D — Context Injection
- Merge memory + retrieved docs into a single structured context block.
- Apply token budget rules to prevent prompt overflow.
- Insert citations / source references inline.

### Module E — Memory Persistence
- After response, decide what new information merits storage.
- Update `user_profile`, `conversation_summary`, and `task_history`.
- Expire entries older than `memory_retention_limit`.

---

## 3. EXECUTION LOGIC

```
STEP 1 ─ PARSE QUERY
  input  : raw user message
  action : extract intent, entities, domain tags, temporal signals
  output : structured query object  { text, intent, entities[], domain }

STEP 2 ─ MEMORY READ
  action : load session memory (short-term) + user profile (long-term)
  filter : keep chunks where relevance_score > SIMILARITY_THRESHOLD
  output : memory_context[]  (ranked, deduplicated)

STEP 3 ─ ROUTE DECISION
  rules  :
    if intent == "recall"          → memory_only path
    if intent == "lookup"          → retrieval_only path
    if intent == "reason/analyze"  → memory + retrieval path
    default                        → memory + retrieval path
  output : path ∈ { MEMORY, RETRIEVAL, HYBRID }

STEP 4 ─ RETRIEVAL  (if path ∈ RETRIEVAL | HYBRID)
  4a. embed query  →  dense_vector
  4b. vector_search(dense_vector, top_k=TOP_K)
  4c. hybrid_search(query.text, top_k=TOP_K)   ← BM25
  4d. merge + deduplicate candidates
  4e. cross_encoder_rerank(candidates, query)
  4f. select top_k_final ≤ TOP_K results above SIMILARITY_THRESHOLD
  output : retrieved_docs[]  { text, score, source, chunk_id }

STEP 5 ─ CONTEXT ASSEMBLY
  action : merge memory_context[] + retrieved_docs[]
  budget : total tokens ≤ MAX_CONTEXT_TOKENS
  pruning: drop lowest-score chunks until budget is met
  output : assembled_context  (ordered: user_profile → summary → docs → recent_turns)

STEP 6 ─ PROMPT CONSTRUCTION
  select template based on path:
    MEMORY    → MEMORY_ONLY_TEMPLATE
    RETRIEVAL → RAG_TEMPLATE
    HYBRID    → MEMORY_RAG_TEMPLATE
  inject: {query}, {memory}, {documents}, {instructions}
  output : final_prompt  (≤ MAX_CONTEXT_TOKENS + response_budget)

STEP 7 ─ GENERATE RESPONSE
  call LLM with final_prompt
  extract: response_text, confidence_signals, citations[]
  output : response object

STEP 8 ─ MEMORY WRITE  (async, post-response)
  evaluate: does this turn contain new facts / preferences / decisions?
  if yes:
    update user_profile   (if personal info)
    append task_history   (if task completed)
    refresh conv_summary  (if session > SUMMARY_THRESHOLD turns)
    cache doc chunks that scored highly  (knowledge_cache)
  expire entries older than MEMORY_RETENTION_LIMIT
```

---

## 4. MEMORY SCHEMA

### 4.1 `user_profile`
```json
{
  "user_id": "usr_abc123",
  "name": "Priya",
  "preferences": {
    "tone": "concise",
    "language": "en",
    "domain_interests": ["design systems", "AI tools"]
  },
  "known_facts": [
    { "fact": "Uses Figma as primary design tool", "confidence": 0.95, "updated_at": "2025-04-01" },
    { "fact": "Prefers dark mode interfaces", "confidence": 0.80, "updated_at": "2025-03-20" }
  ],
  "last_seen": "2025-04-10T14:32:00Z"
}
```

### 4.2 `conversation_summary`
```json
{
  "session_id": "sess_xyz789",
  "user_id": "usr_abc123",
  "created_at": "2025-04-10T13:00:00Z",
  "summary": "User is building an AI-powered design feedback tool. Discussed component library structure and accessibility requirements. Decision: use WCAG 2.2 AA as baseline.",
  "key_decisions": [
    "Use WCAG 2.2 AA",
    "Component library in React + Storybook"
  ],
  "open_questions": ["How to handle dark mode tokens?"],
  "turn_count": 14,
  "compressed_at_turn": 10
}
```

### 4.3 `knowledge_cache`
```json
{
  "cache_id": "kc_001",
  "query_fingerprint": "hash_of_query_embedding",
  "chunks": [
    {
      "chunk_id": "doc_42_chunk_3",
      "text": "WCAG 2.2 introduces new success criteria for focus appearance and dragging movements.",
      "source": "wcag_2_2_overview.pdf",
      "score": 0.91,
      "cached_at": "2025-04-10T13:15:00Z"
    }
  ],
  "ttl_seconds": 3600
}
```

### 4.4 `task_history`
```json
{
  "user_id": "usr_abc123",
  "tasks": [
    {
      "task_id": "tsk_001",
      "description": "Generate component accessibility checklist",
      "status": "completed",
      "output_summary": "12-item checklist covering WCAG 2.2 criteria",
      "completed_at": "2025-04-10T13:45:00Z"
    }
  ]
}
```

---

## 5. RETRIEVAL PIPELINE

```python
# ── RETRIEVAL PIPELINE (pseudo-code) ──────────────────────────────────────

def retrieve(query: str, config: Config) -> list[Chunk]:

    # Step 1: Embed query
    dense_vec = embedding_model.encode(query)          # float[1536]

    # Step 2: Dense vector search
    dense_results = vector_db.search(
        vector    = dense_vec,
        top_k     = config.top_k * 2,                 # over-fetch for reranking
        namespace = config.domain or "global"
    )  # → [{ chunk_id, text, score, source }]

    # Step 3: Sparse / BM25 search (hybrid)
    sparse_results = keyword_index.search(
        query  = query,
        top_k  = config.top_k * 2
    )

    # Step 4: Merge + deduplicate
    candidates = deduplicate(dense_results + sparse_results)

    # Step 5: Cross-encoder re-ranking
    ranked = cross_encoder.rerank(
        query      = query,
        candidates = candidates
    )  # → sorted by semantic relevance

    # Step 6: Threshold filter + top-K selection
    final = [
        c for c in ranked
        if c.score >= config.similarity_threshold
    ][:config.top_k]

    # Step 7: Assemble context string
    context_blocks = [
        f"[Source: {c.source}]\n{c.text}"
        for c in final
    ]

    return final, "\n\n---\n\n".join(context_blocks)
```

---

## 6. PROMPT TEMPLATES

### Template 1 — RAG Only
```
SYSTEM:
You are a helpful assistant. Answer using ONLY the documents provided.
If the answer is not in the documents, say "I don't have enough information."
Always cite sources as [Source: filename].

CONTEXT DOCUMENTS:
{documents}

USER QUERY:
{query}

ASSISTANT:
```

---

### Template 2 — Memory + RAG (Hybrid)
```
SYSTEM:
You are a personalized assistant with memory of past interactions.
Use memory context to personalize and documents to ground your answer.
Prefer document facts over memory when they conflict.
Cite document sources inline as [Source: name].

USER PROFILE:
{memory.user_profile}

CONVERSATION SUMMARY:
{memory.conversation_summary}

RELEVANT DOCUMENTS:
{documents}

CURRENT QUERY:
{query}

ASSISTANT:
```

---

### Template 3 — Context Compression (for long sessions)
```
SYSTEM:
Compress the following conversation into a structured summary.
Output ONLY valid JSON matching this schema:
{
  "summary": "<2-3 sentence overview>",
  "key_decisions": ["...", "..."],
  "open_questions": ["...", "..."],
  "important_facts": ["...", "..."]
}

CONVERSATION TURNS:
{raw_conversation_turns}

OUTPUT:
```

---

### Template 4 — Memory-Only (Recall)
```
SYSTEM:
You are a helpful assistant. Use ONLY the user's memory context below.
Do not invent information not present in memory.

USER PROFILE:
{memory.user_profile}

CONVERSATION SUMMARY:
{memory.conversation_summary}

TASK HISTORY:
{memory.task_history}

RECALL QUERY:
{query}

ASSISTANT:
```

---

## 7. TOOL INTERFACES

```typescript
// Abstract interfaces — implement with any vendor

interface EmbeddingModel {
  encode(text: string): Promise<number[]>;
  dimension: number;  // e.g. 1536 for ada-002, 768 for bge
}

interface VectorDatabase {
  search(params: {
    vector: number[];
    top_k: number;
    namespace?: string;
    filter?: Record<string, unknown>;
  }): Promise<Chunk[]>;

  upsert(chunks: Chunk[]): Promise<void>;
  delete(chunk_ids: string[]): Promise<void>;
}

interface MemoryStore {
  get(key: string): Promise<MemoryObject | null>;
  set(key: string, value: MemoryObject, ttl?: number): Promise<void>;
  delete(key: string): Promise<void>;
  list(prefix: string): Promise<string[]>;
}

interface CrossEncoder {
  rerank(query: string, candidates: Chunk[]): Promise<Chunk[]>;
}

interface KeywordIndex {
  search(query: string, top_k: number): Promise<Chunk[]>;
}

// Vendor mapping examples (not required — implement as needed):
// EmbeddingModel  → OpenAI ada-002 | Cohere embed | BGE-large | Voyage
// VectorDatabase  → Pinecone | Weaviate | Qdrant | pgvector | Chroma
// MemoryStore     → Redis | DynamoDB | Supabase | in-memory Map
// CrossEncoder    → Cohere rerank | BGE-reranker | Jina reranker
```

---

## 8. CONFIGURATION

```yaml
# context_intelligence_config.yaml

retrieval:
  top_k: 5                        # Final docs injected into prompt
  top_k_fetch_multiplier: 2       # Over-fetch before reranking (top_k × this)
  similarity_threshold: 0.72      # Min cosine similarity to include a chunk
  hybrid_alpha: 0.7               # 1.0 = dense only, 0.0 = sparse only

context:
  max_context_tokens: 6000        # Hard cap on assembled context block
  response_budget_tokens: 1000    # Reserved for LLM response
  user_profile_token_limit: 300
  summary_token_limit: 400
  docs_token_limit: 5000

memory:
  memory_retention_limit_days: 30   # Expire entries older than this
  summary_threshold_turns: 10       # Compress conversation after N turns
  knowledge_cache_ttl_seconds: 3600 # TTL for cached retrieval results
  max_task_history_entries: 50

routing:
  recall_intent_keywords:
    - "what did i say"
    - "remember when"
    - "previous session"
    - "my preference"
  lookup_intent_keywords:
    - "find"
    - "look up"
    - "search"
    - "what is"
    - "how does"
  default_path: "hybrid"
```

---

## 9. TOKEN OPTIMIZATION

### Strategy 1 — Tiered Context Loading
```
Priority 1 (always include):  user_profile      ≤ 300 tokens
Priority 2 (include if fits): conv_summary      ≤ 400 tokens
Priority 3 (fill remainder):  retrieved_docs    ≤ remaining budget
Priority 4 (drop first):      task_history      (lowest priority)
```

### Strategy 2 — Dynamic Pruning
```python
def prune_to_budget(chunks: list[Chunk], budget: int) -> list[Chunk]:
    selected, used = [], 0
    for chunk in sorted(chunks, key=lambda c: c.score, reverse=True):
        tokens = count_tokens(chunk.text)
        if used + tokens <= budget:
            selected.append(chunk)
            used += tokens
        else:
            break
    return selected
```

### Strategy 3 — Summarization Trigger
```
if session.turn_count % SUMMARY_THRESHOLD == 0:
    raw_turns = get_last_N_turns(SUMMARY_THRESHOLD)
    summary   = llm.complete(COMPRESSION_TEMPLATE.format(raw_conversation_turns=raw_turns))
    memory.set(f"summary:{session_id}", parse_json(summary))
    # Raw turns are now retired — summary replaces them
```

### Strategy 4 — Chunk Truncation
```
If a single chunk exceeds 400 tokens:
  → Keep first 300 tokens + "[...truncated]"
  → Preserves source attribution and key opening content
```

---

## 10. FAILURE HANDLING

| Failure Mode | Detection | Action |
|---|---|---|
| **No relevant docs found** | `len(retrieved_docs) == 0` | Use memory-only path; flag `grounding: none` in response metadata |
| **All docs below threshold** | All scores < `similarity_threshold` | Lower threshold by 0.1, retry once; if still empty → memory-only |
| **Memory conflict** | Two facts contradict (same entity, different value) | Keep most recent; log conflict with both versions |
| **Token budget exceeded** | assembled_context > MAX_CONTEXT_TOKENS | Prune by priority tier (see §9); never drop user_profile |
| **Memory store unavailable** | Connection error | Proceed with retrieval-only; log warning; skip memory write |
| **Vector DB unavailable** | Timeout / error | Proceed with memory-only; surface `retrieval: unavailable` in metadata |
| **Low-confidence response** | LLM outputs hedge phrases like "I'm not sure" | Append sources list; advise user to verify |
| **Embedding model failure** | API error | Fallback to keyword-only search (BM25 path) |

---

## 11. EVALUATION METRICS

```yaml
metrics:

  retrieval_precision:
    definition: "Fraction of retrieved chunks actually relevant to the query"
    target: ≥ 0.75
    measure: human_label or LLM-as-judge on 100-query sample

  retrieval_recall:
    definition: "Fraction of relevant chunks that were retrieved (of all available)"
    target: ≥ 0.65

  hallucination_rate:
    definition: "% of factual claims in response NOT grounded in context or memory"
    target: ≤ 0.05
    measure: fact_check against source chunks

  response_relevance:
    definition: "Semantic similarity between response and query intent (0–1)"
    target: ≥ 0.80
    measure: embedding cosine sim or LLM rating (1-5 scale)

  token_efficiency:
    definition: "Response quality per 1000 tokens of context used"
    target: maximize; flag if context > 5000 tokens for simple queries

  memory_hit_rate:
    definition: "% of queries where memory was usefully retrieved"
    target: ≥ 0.60 for returning users

  latency_p95:
    definition: "95th percentile end-to-end response time"
    target: ≤ 3000ms (retrieval + generation)

  context_utilization:
    definition: "% of injected context tokens referenced in response"
    target: ≥ 0.50  (low = wasted context)
```

---

## 12. EXAMPLE INPUTS / OUTPUTS

### Example A — Retrieval-Only (cold user, domain query)

**Input:**
```json
{
  "session_id": "sess_new",
  "user_id": null,
  "query": "What are the WCAG 2.2 new success criteria for focus indicators?"
}
```

**Path:** `RETRIEVAL`

**Output:**
```json
{
  "response": "WCAG 2.2 introduced two new success criteria for focus indicators: SC 2.4.11 (Focus Appearance – Minimum, Level AA) and SC 2.4.12 (Focus Appearance – Enhanced, Level AAA). The minimum criterion requires the focus indicator to have a minimum area and contrast ratio. [Source: wcag_2_2_spec.pdf]",
  "sources": ["wcag_2_2_spec.pdf"],
  "grounding": "document",
  "memory_written": false
}
```

---

### Example B — Memory + Retrieval (returning user)

**Input:**
```json
{
  "session_id": "sess_xyz789",
  "user_id": "usr_abc123",
  "query": "How should I handle focus rings in my dark mode component library?"
}
```

**Path:** `HYBRID`

**Memory loaded:**
- user_profile: uses Figma, prefers dark mode, React + Storybook
- summary: building AI feedback tool, WCAG 2.2 AA baseline decided

**Output:**
```json
{
  "response": "For your dark mode Storybook component library, use a focus ring with at least 3:1 contrast against the dark background per WCAG 2.2 SC 2.4.11. A practical approach: define a CSS custom property --focus-ring-color that swaps via your dark mode token. Since you're already on WCAG 2.2 AA, the minimum focus area (perimeter × 2px) criterion also applies. [Source: wcag_2_2_spec.pdf]",
  "sources": ["wcag_2_2_spec.pdf"],
  "grounding": "memory + document",
  "memory_written": false
}
```

---

### Example C — Memory-Only (recall)

**Input:**
```json
{
  "session_id": "sess_xyz789",
  "user_id": "usr_abc123",
  "query": "What did we decide about the accessibility standard to use?"
}
```

**Path:** `MEMORY`

**Output:**
```json
{
  "response": "In your earlier session, you decided to use WCAG 2.2 AA as the accessibility baseline for your component library.",
  "sources": [],
  "grounding": "memory",
  "memory_written": false
}
```

---

### Example D — Memory Write Trigger

**Input:**
```json
{
  "query": "Actually, we just decided to upgrade to WCAG 2.2 AAA for enterprise clients."
}
```

**Output:**
```json
{
  "response": "Got it — I've updated your context. For enterprise clients, you'll now target WCAG 2.2 AAA, which includes the enhanced focus appearance criterion (SC 2.4.12) and stricter contrast ratios.",
  "memory_written": true,
  "memory_update": {
    "key_decisions": ["WCAG 2.2 AAA for enterprise clients (upgraded from AA)"],
    "conflict_resolved": "Previous decision: WCAG 2.2 AA → superseded by recency"
  }
}
```

---

## 13. LIGHTWEIGHT VERSION

> Use when token budget is critical or latency must be minimized.
> Drops: cross-encoder reranking, BM25 hybrid, tiered memory, task history.

```
─── CONTEXT-INTELLIGENCE LITE ──────────────────────────────────────────────

CONFIG:  top_k=3 | threshold=0.75 | max_ctx=2500 | memory=summary_only

PIPELINE:
  1. embed(query) → vector_search(top_k=3)
  2. filter scores ≥ 0.75
  3. load conv_summary (≤ 250 tokens)
  4. assemble: summary + docs (≤ 2500 tokens total)
  5. use RAG_TEMPLATE_LITE (below)
  6. generate → respond

LITE TEMPLATE:
┌──────────────────────────────────────────────────────────────┐
│ SYSTEM: Answer using the context below. Cite sources.        │
│                                                              │
│ PRIOR CONTEXT: {memory.summary}                              │
│                                                              │
│ DOCUMENTS: {documents}                                        │
│                                                              │
│ QUERY: {query}                                               │
└──────────────────────────────────────────────────────────────┘

FAILURE: if no docs → answer from summary only, flag grounding=low
MEMORY WRITE: skip (stateless lite mode)

Token savings vs full skill: ~40–60% reduction in context tokens.
Recommended for: chat UIs, real-time agents, cost-sensitive deployments.
─────────────────────────────────────────────────────────────────────────────
```

---

## 14. INTEGRATION CHECKLIST

Before deploying this skill, verify:

- [ ] Embedding model chosen and dimension configured
- [ ] Vector DB namespace matches your domain tags
- [ ] Memory store connected (Redis / KV / DB)
- [ ] `session_id` propagated through all agent turns
- [ ] Token counter matches your LLM's tokenizer (tiktoken / sentencepiece)
- [ ] `similarity_threshold` tuned on your corpus (start at 0.72, adjust)
- [ ] Compression template tested — output must be valid JSON
- [ ] Failure paths return valid `response` objects (never raise to user)
- [ ] Memory TTL expiry tested (no stale facts bleeding across users)
- [ ] Evaluation baseline run (retrieval_precision ≥ 0.75 before launch)

---

*Skill version 1.0.0 — generated for claude / chatgpt / agent runtimes*
*Modular: import any single section independently.*
