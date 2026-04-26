# Model Profiles

Per-model token optimization settings. Load this when configuring the optimizer for a specific model.

---

## Profile Schema

Each profile defines:
- `context_window`: max tokens (input + output)
- `recommended_input_budget`: % of context for input+context
- `recommended_output_budget`: % for output
- `cot_efficiency`: how much CoT improves accuracy (high = worth the tokens)
- `compression_sensitivity`: how much quality drops when prompts are over-compressed
- `tokenizer`: which tokenizer to use for counting
- `quirks`: model-specific behavior notes

---

## Profiles

### claude-3-5-sonnet (Anthropic)
```yaml
context_window: 200000
recommended_input_budget: 65%
recommended_output_budget: 35%
cot_efficiency: very_high
compression_sensitivity: low
tokenizer: claude (approx 1.2 tokens/word)
quirks:
  - Follows XML-tagged instructions reliably
  - Handles compressed bullet-style prompts well
  - Naturally concise; output constraints rarely needed
  - Works well with structured output (JSON) requests
```

### claude-3-haiku (Anthropic)
```yaml
context_window: 200000
recommended_input_budget: 60%
recommended_output_budget: 40%
cot_efficiency: medium
compression_sensitivity: high
tokenizer: claude (approx 1.2 tokens/word)
quirks:
  - Compress aggressively; Haiku is cost-optimized
  - Add explicit output format instructions (less autonomous)
  - Limit CoT — reasoning quality drops faster than Sonnet
  - Good for extraction and classification tasks
```

### claude-3-opus (Anthropic)
```yaml
context_window: 200000
recommended_input_budget: 55%
recommended_output_budget: 45%
cot_efficiency: very_high
compression_sensitivity: very_low
tokenizer: claude (approx 1.2 tokens/word)
quirks:
  - Can handle highly compressed prompts without quality loss
  - Over-generates by default — always add output constraints
  - Best reasoning model; enable CoT for complex tasks
  - Most expensive; prioritize compression of all layers
```

### gpt-4o (OpenAI)
```yaml
context_window: 128000
recommended_input_budget: 60%
recommended_output_budget: 40%
cot_efficiency: high
compression_sensitivity: low
tokenizer: tiktoken cl100k_base
quirks:
  - Handles verbose and compressed prompts equally well
  - Responds well to role-based system prompts
  - JSON mode available — use it for structured output
  - Slightly over-explains; add "No preamble." to output constraints
```

### gpt-3.5-turbo (OpenAI)
```yaml
context_window: 16000
recommended_input_budget: 55%
recommended_output_budget: 45%
cot_efficiency: medium
compression_sensitivity: very_high
tokenizer: tiktoken cl100k_base
quirks:
  - Small context window — compress aggressively
  - Struggles with highly compressed abstract prompts
  - Keep examples concrete; don't over-abbreviate
  - Best for simple extraction, classification, reformatting
  - CoT helps with math but not worth cost for simple tasks
```

### gemini-1.5-pro (Google)
```yaml
context_window: 1000000
recommended_input_budget: 70%
recommended_output_budget: 30%
cot_efficiency: high
compression_sensitivity: low
tokenizer: google sentencepiece (approx 1.15 tokens/word)
quirks:
  - Massive context window — context selection less critical
  - Still compress to reduce latency and cost
  - Good at following structured schemas
  - May pad output; enforce format constraints
```

### gemini-1.5-flash (Google)
```yaml
context_window: 1000000
recommended_input_budget: 65%
recommended_output_budget: 35%
cot_efficiency: medium
compression_sensitivity: high
tokenizer: google sentencepiece (approx 1.15 tokens/word)
quirks:
  - Cost-optimized — compress all layers aggressively
  - Strong at structured extraction tasks
  - Lower accuracy on complex reasoning; use CoT selectively
```

### llama-3-70b (Meta / local)
```yaml
context_window: 8192
recommended_input_budget: 50%
recommended_output_budget: 50%
cot_efficiency: low
compression_sensitivity: very_high
tokenizer: llama tokenizer (approx 1.3 tokens/word)
quirks:
  - Very small context window — every token counts
  - Prioritize task + immediate context only; no history
  - Struggles with JSON output — use simplified formats
  - CoT rarely worth it; adds tokens without proportional gain
  - Best results with direct imperative prompts
```

### mistral-7b (Mistral / local)
```yaml
context_window: 32000
recommended_input_budget: 55%
recommended_output_budget: 45%
cot_efficiency: low
compression_sensitivity: high
tokenizer: mistral sentencepiece (approx 1.25 tokens/word)
quirks:
  - Compact model — use for simple, well-defined tasks
  - Avoid complex multi-step reasoning
  - Works well with numbered instruction formats
```

---

## Tokenizer Utilities

```python
# For OpenAI models
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
token_count = len(enc.encode(text))

# For Claude models (approximation)
def claude_token_estimate(text: str) -> int:
    return int(len(text.split()) * 1.2)

# For Gemini models (approximation)  
def gemini_token_estimate(text: str) -> int:
    return int(len(text.split()) * 1.15)

# Universal fallback
def universal_token_estimate(text: str) -> int:
    return int(len(text.split()) * 1.3)  # conservative
```
