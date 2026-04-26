"""
Token Efficiency Optimizer
==========================
Model-agnostic middleware for minimizing token usage across LLMs.
Works with any OpenAI-compatible API (Claude, GPT, Gemini via proxy, etc.)

Usage:
    optimizer = TokenOptimizer(model="claude-sonnet-4-20250514", total_budget=4000)
    result = optimizer.optimize(
        system="You are a helpful assistant.",
        history=conversation_history,
        user_message="Debug my sort function.",
        task_type="code_generation"
    )
    # Pass result.optimized_messages to your LLM API
"""

import re
import json
from dataclasses import dataclass, field
from typing import Optional
from collections import deque


# ─────────────────────────────────────────────
# Data Models
# ─────────────────────────────────────────────

@dataclass
class Message:
    role: str   # "system" | "user" | "assistant"
    content: str

@dataclass
class OptimizationResult:
    optimized_messages: list[dict]
    token_estimate: int
    original_token_estimate: int
    savings_report: dict
    task_type: str

@dataclass
class UsageRecord:
    original_tokens: int
    optimized_tokens: int
    output_tokens: int
    task_type: str
    quality_score: Optional[float] = None  # 0.0–1.0, filled from feedback


# ─────────────────────────────────────────────
# Token Estimation (model-agnostic)
# ─────────────────────────────────────────────

TOKENIZER_RATIOS = {
    "gpt-4":        1.2,
    "gpt-4o":       1.2,
    "gpt-3.5":      1.2,
    "claude":       1.2,
    "gemini":       1.15,
    "llama":        1.3,
    "mistral":      1.25,
    "default":      1.3,
}

def estimate_tokens(text: str, model: str = "default") -> int:
    """Word-based token estimation. For production, swap with tiktoken or model SDK."""
    ratio = next(
        (v for k, v in TOKENIZER_RATIOS.items() if k in model.lower()),
        TOKENIZER_RATIOS["default"]
    )
    return int(len(text.split()) * ratio)


# ─────────────────────────────────────────────
# 1. Prompt Compression Layer
# ─────────────────────────────────────────────

FILLER_PATTERNS = [
    (r"(?i)\bplease\b,?\s*", ""),
    (r"(?i)could you (kindly |please )?(help me |assist me )?", ""),
    (r"(?i)i (would|'d) (like|appreciate it if) you (to |could )?", ""),
    (r"(?i)feel free to (ask|let me know)[^.]*\.", ""),
    (r"(?i)let me know if you need (any(thing)?( else)?|clarification)[^.]*\.", ""),
    (r"(?i)as an AI (language model|assistant),?\s*", ""),
    (r"(?i)i hope (this helps|you're doing well)[^.]*\.", ""),
    (r"(?i)great question[!.]?\s*", ""),
    (r"(?i)sure[!,]?\s*(i('ll| will|'d be happy to))?\s*", ""),
    (r"(?i)of course[!,]?\s*", ""),
    (r"(?i)here is (my|the) (question|request|task)[:.]\s*", ""),
    (r"\bthe answer is:?\s*", ""),
    (r"(?i)as per (the above|my previous)[^.]*\.", ""),
    (r"\n{3,}", "\n\n"),   # Collapse excess blank lines
]

def compress_prompt(text: str) -> str:
    """Apply filler removal and structural compression."""
    for pattern, replacement in FILLER_PATTERNS:
        text = re.sub(pattern, replacement, text)
    
    # Collapse multi-space
    text = re.sub(r"  +", " ", text)
    text = text.strip()
    return text


# ─────────────────────────────────────────────
# 2. Context Selection Layer
# ─────────────────────────────────────────────

def score_relevance(query: str, message: Message) -> float:
    """
    Simple word-overlap relevance score (0.0–1.0).
    In production, replace with embedding cosine similarity.
    """
    query_words = set(query.lower().split())
    msg_words = set(message.content.lower().split())
    if not query_words or not msg_words:
        return 0.0
    overlap = query_words & msg_words
    return len(overlap) / len(query_words)

SKIP_CONTENT_PATTERNS = [
    r"(?i)^(got it|sure|ok|okay|thanks?|thank you|understood|sounds good)[!.]?$",
    r"(?i)^(great|perfect|awesome|excellent)[!.]?$",
]

def is_filler_message(msg: Message) -> bool:
    return any(re.match(p, msg.content.strip()) for p in SKIP_CONTENT_PATTERNS)

def select_context(
    history: list[Message],
    current_query: str,
    max_turns: int = 5,
    token_budget: int = 1000,
    model: str = "default"
) -> list[Message]:
    """
    Select most relevant history messages within token budget.
    Always keeps the most recent `max_turns` as a baseline,
    then adds high-relevance older messages if budget allows.
    """
    if not history:
        return []

    # Filter filler messages
    history = [m for m in history if not is_filler_message(m)]

    # Always include last max_turns messages
    recent = history[-max_turns:]
    older = history[:-max_turns]

    # Score older messages for relevance
    scored_older = sorted(
        older,
        key=lambda m: score_relevance(current_query, m),
        reverse=True
    )

    selected = list(recent)
    used_tokens = sum(estimate_tokens(m.content, model) for m in selected)

    for msg in scored_older:
        msg_tokens = estimate_tokens(msg.content, model)
        if used_tokens + msg_tokens <= token_budget:
            selected.insert(0, msg)  # prepend older messages
            used_tokens += msg_tokens
        if used_tokens >= token_budget:
            break

    return selected


# ─────────────────────────────────────────────
# 3. Memory Summarization Layer
# ─────────────────────────────────────────────

MEMORY_COMPRESS_PROMPT = """Compress this conversation to ≤100 words.
Keep: decisions, user preferences, unresolved questions, key facts.
Remove: pleasantries, repeated questions, verbose explanations.
Return summary only.

{conversation}"""

def should_summarize(history: list[Message], threshold_tokens: int = 2000, model: str = "default") -> bool:
    total = sum(estimate_tokens(m.content, model) for m in history)
    return total > threshold_tokens

def build_summary_prompt(history: list[Message]) -> str:
    conv_text = "\n".join(f"{m.role.upper()}: {m.content}" for m in history)
    return MEMORY_COMPRESS_PROMPT.format(conversation=conv_text)

# NOTE: Call this with your LLM API client to get the actual summary.
# Example:
#   summary_text = your_llm_call(build_summary_prompt(old_history))
#   summarized_msg = Message(role="system", content=f"[CONVERSATION SUMMARY]\n{summary_text}")


# ─────────────────────────────────────────────
# 4. Output Constraint Controller
# ─────────────────────────────────────────────

OUTPUT_CONSTRAINTS = {
    "simple_qa":        "Answer in ≤2 sentences. No preamble.",
    "analysis":         "Structure: Summary (1 sentence) → Key findings (3 bullets) → Recommendation (1 sentence). Max 200 words.",
    "code_generation":  "Return code only. No explanation unless a comment is necessary. Use inline comments sparingly.",
    "code_review":      "Return: numbered list of issues. Format: [SEVERITY] Line N: description. No preamble.",
    "summarization":    "Return bulleted summary. Max 5 bullets. Each bullet ≤15 words.",
    "classification":   "Return label only. No explanation.",
    "extraction":       "Return valid JSON only. No markdown. No explanation. Null for missing fields.",
    "translation":      "Return translation only.",
    "brainstorm":       "Return numbered list. Max 7 items. Each item ≤10 words.",
    "default":          "Be concise. No preamble. No sign-off.",
}

def get_output_constraint(task_type: str) -> str:
    return OUTPUT_CONSTRAINTS.get(task_type, OUTPUT_CONSTRAINTS["default"])


# ─────────────────────────────────────────────
# 5. Reasoning Control Layer
# ─────────────────────────────────────────────

# Task types where CoT improves accuracy enough to justify token cost
COT_WORTHY_TASKS = {"analysis", "code_generation", "code_review", "math", "planning", "multi_step"}

def get_reasoning_instruction(task_type: str, complexity_score: float = 0.5) -> str:
    """
    complexity_score: 0.0 (trivial) → 1.0 (very complex)
    """
    if task_type in COT_WORTHY_TASKS or complexity_score > 0.7:
        if complexity_score > 0.85:
            return "Think step by step."
        return "Think briefly, then answer."
    return "Return the final answer only. Do not show reasoning."

def estimate_complexity(user_message: str, task_type: str) -> float:
    """
    Heuristic complexity scorer. Replace with ML classifier for production.
    """
    score = 0.0
    
    # Length heuristic
    words = len(user_message.split())
    if words > 100: score += 0.2
    if words > 300: score += 0.2

    # Task type base complexity
    base = {"analysis": 0.5, "code_generation": 0.4, "code_review": 0.4,
            "simple_qa": 0.1, "classification": 0.1, "extraction": 0.2,
            "summarization": 0.3, "brainstorm": 0.3}
    score += base.get(task_type, 0.3)

    # Question complexity signals
    complex_signals = ["why", "how does", "compare", "tradeoff", "pros and cons",
                       "explain", "design", "architect", "optimize", "debug"]
    for signal in complex_signals:
        if signal in user_message.lower():
            score += 0.1

    return min(score, 1.0)


# ─────────────────────────────────────────────
# 6. Token Budget Allocator
# ─────────────────────────────────────────────

BUDGET_PROFILES = {
    "simple_qa":       {"input": 0.60, "reasoning": 0.00, "output": 0.40},
    "analysis":        {"input": 0.45, "reasoning": 0.20, "output": 0.35},
    "code_generation": {"input": 0.40, "reasoning": 0.15, "output": 0.45},
    "code_review":     {"input": 0.50, "reasoning": 0.10, "output": 0.40},
    "summarization":   {"input": 0.70, "reasoning": 0.05, "output": 0.25},
    "extraction":      {"input": 0.65, "reasoning": 0.00, "output": 0.35},
    "classification":  {"input": 0.70, "reasoning": 0.00, "output": 0.30},
    "default":         {"input": 0.55, "reasoning": 0.10, "output": 0.35},
}

def get_budget(total_tokens: int, task_type: str, complexity_score: float = 0.5) -> dict:
    profile = BUDGET_PROFILES.get(task_type, BUDGET_PROFILES["default"]).copy()
    
    # Dynamic adjustment for high complexity
    if complexity_score > 0.7:
        shift = 0.10
        profile["reasoning"] = min(profile["reasoning"] + shift, 0.30)
        profile["output"] = max(profile["output"] - shift / 2, 0.20)
        profile["input"] = max(profile["input"] - shift / 2, 0.30)

    return {
        "input_tokens":     int(total_tokens * profile["input"]),
        "reasoning_tokens": int(total_tokens * profile["reasoning"]),
        "output_tokens":    int(total_tokens * profile["output"]),
    }


# ─────────────────────────────────────────────
# 7. Main Optimizer
# ─────────────────────────────────────────────

class TokenOptimizer:
    """
    Wraps any OpenAI-compatible LLM API with token efficiency middleware.
    
    Example:
        optimizer = TokenOptimizer(model="claude-sonnet-4-20250514", total_budget=4000)
        result = optimizer.optimize(
            system="You are a Python expert.",
            history=history,
            user_message="Debug this sort function.",
            task_type="code_review"
        )
        # Use result.optimized_messages as your API messages array
    """

    def __init__(self, model: str = "default", total_budget: int = 4000):
        self.model = model
        self.total_budget = total_budget
        self.usage_log: deque[UsageRecord] = deque(maxlen=200)

    def optimize(
        self,
        user_message: str,
        system: str = "",
        history: Optional[list[Message]] = None,
        task_type: str = "default",
        complexity_score: Optional[float] = None,
    ) -> OptimizationResult:
        history = history or []

        # Estimate original size
        all_content = system + user_message + " ".join(m.content for m in history)
        original_tokens = estimate_tokens(all_content, self.model)

        # Score complexity
        complexity = complexity_score if complexity_score is not None else \
                     estimate_complexity(user_message, task_type)

        # Get budget allocations
        budget = get_budget(self.total_budget, task_type, complexity)

        # Step 1: Compress system + user prompt
        compressed_system = compress_prompt(system)
        compressed_user = compress_prompt(user_message)

        # Step 2: Select relevant context
        selected_history = select_context(
            history,
            current_query=compressed_user,
            token_budget=budget["input_tokens"] - estimate_tokens(compressed_system + compressed_user, self.model),
            model=self.model
        )

        # Step 3: Get reasoning instruction
        reasoning_instruction = get_reasoning_instruction(task_type, complexity)

        # Step 4: Get output constraint
        output_constraint = get_output_constraint(task_type)

        # Step 5: Build final user message with constraints
        final_user = f"{compressed_user}\n\n{reasoning_instruction}\n{output_constraint}"

        # Step 6: Build messages array
        messages = []
        if compressed_system:
            messages.append({"role": "system", "content": compressed_system})
        for msg in selected_history:
            messages.append({"role": msg.role, "content": compress_prompt(msg.content)})
        messages.append({"role": "user", "content": final_user})

        # Estimate optimized token count
        optimized_content = " ".join(m["content"] for m in messages)
        optimized_tokens = estimate_tokens(optimized_content, self.model)

        # Log for self-improvement
        self.usage_log.append(UsageRecord(
            original_tokens=original_tokens,
            optimized_tokens=optimized_tokens,
            output_tokens=budget["output_tokens"],
            task_type=task_type
        ))

        return OptimizationResult(
            optimized_messages=messages,
            token_estimate=optimized_tokens,
            original_token_estimate=original_tokens,
            task_type=task_type,
            savings_report={
                "original_tokens": original_tokens,
                "optimized_tokens": optimized_tokens,
                "savings_tokens": original_tokens - optimized_tokens,
                "savings_pct": round((1 - optimized_tokens / max(original_tokens, 1)) * 100, 1),
                "budget_allocated": budget,
                "history_turns_kept": len(selected_history),
                "history_turns_total": len(history),
            }
        )

    def record_output(self, output_tokens: int, quality_score: Optional[float] = None):
        """Call after API response to record actual output token usage."""
        if self.usage_log:
            record = self.usage_log[-1]
            record.output_tokens = output_tokens
            record.quality_score = quality_score


# ─────────────────────────────────────────────
# 8. Self-Improvement Loop
# ─────────────────────────────────────────────

class SelfImprovementLoop:
    """
    Analyzes usage logs to identify inefficiencies and suggest adjustments.
    Run periodically (e.g., every 50 API calls).
    """

    def __init__(self, optimizer: TokenOptimizer):
        self.optimizer = optimizer

    def audit(self) -> dict:
        logs = list(self.optimizer.usage_log)
        if not logs:
            return {"status": "no_data"}

        total = len(logs)
        avg_savings = sum(
            (r.original_tokens - r.optimized_tokens) / max(r.original_tokens, 1)
            for r in logs
        ) / total

        # Find over-prompted tasks (output dominates)
        over_prompted = [
            r for r in logs
            if r.output_tokens > 0 and r.optimized_tokens > 0
            and (r.output_tokens / r.optimized_tokens) > 0.8
        ]

        # Find quality failures (where score < threshold)
        quality_failures = [r for r in logs if r.quality_score is not None and r.quality_score < 0.7]

        suggestions = []
        if len(over_prompted) / total > 0.2:
            suggestions.append(
                "20%+ of calls have output > 80% of input. "
                "Consider more aggressive context trimming or tighter output constraints."
            )
        if len(quality_failures) / max(len([r for r in logs if r.quality_score is not None]), 1) > 0.15:
            suggestions.append(
                "15%+ of scored calls below quality threshold. "
                "Compression may be too aggressive — reduce filler pattern aggressiveness."
            )
        if avg_savings < 0.2:
            suggestions.append(
                "Average savings under 20%. "
                "Prompts may already be lean, or compression rules aren't triggering."
            )

        return {
            "status": "ok",
            "calls_analyzed": total,
            "avg_savings_pct": round(avg_savings * 100, 1),
            "over_prompted_calls": len(over_prompted),
            "quality_failure_calls": len(quality_failures),
            "suggestions": suggestions,
        }


# ─────────────────────────────────────────────
# Example Usage
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Setup
    optimizer = TokenOptimizer(model="claude-sonnet-4-20250514", total_budget=4000)

    # Sample conversation history
    history = [
        Message(role="user", content="Hi! Could you please help me with my Python project?"),
        Message(role="assistant", content="Sure! I'd be happy to help. What do you need?"),
        Message(role="user", content="I'm building a data pipeline with pandas and numpy."),
        Message(role="assistant", content="Got it. What's the issue you're facing?"),
    ]

    # Verbose user message (before optimization)
    raw_user_message = """
    Hello! I hope you're doing well. I was wondering if you could please help me 
    with something. I would really appreciate it if you could take a look at the 
    following Python function that I have written. I think there might be some 
    performance issues with it. Could you kindly review it and let me know what 
    you think might be wrong?
    
    def process_data(df):
        result = []
        for i in range(len(df)):
            row = df.iloc[i]
            result.append(row['value'] * 2)
        return result
    """

    # Optimize
    result = optimizer.optimize(
        system="You are a Python performance expert.",
        history=history,
        user_message=raw_user_message,
        task_type="code_review"
    )

    print("=== SAVINGS REPORT ===")
    print(json.dumps(result.savings_report, indent=2))
    
    print("\n=== OPTIMIZED MESSAGES ===")
    for msg in result.optimized_messages:
        print(f"[{msg['role'].upper()}] {msg['content'][:120]}...")

    # Self-improvement audit
    loop = SelfImprovementLoop(optimizer)
    print("\n=== AUDIT ===")
    print(json.dumps(loop.audit(), indent=2))
