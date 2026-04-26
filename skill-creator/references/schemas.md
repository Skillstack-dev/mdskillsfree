# Schema Patterns Reference

> Copy-paste JSON Schema patterns for common skill types. Select by reasoning_type.

---

## EXTRACTIVE Pattern
```json
{
  "type": "object",
  "required": ["meta", "items"],
  "properties": {
    "meta": { "type": "object" },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "value", "confidence"],
        "properties": {
          "id": { "type": "integer" },
          "value": { "type": "string" },
          "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
          "source": { "type": "string" }
        }
      }
    }
  }
}
```

---

## EVALUATIVE Pattern
```json
{
  "type": "object",
  "required": ["meta", "dimensions", "overall_score", "recommendation"],
  "properties": {
    "dimensions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "score", "justification"],
        "properties": {
          "name": { "type": "string" },
          "score": { "type": "integer", "minimum": 1, "maximum": 5 },
          "justification": { "type": "string" },
          "evidence": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "overall_score": { "type": "number", "minimum": 1.0, "maximum": 5.0 },
    "recommendation": { "type": "string", "enum": ["PASS", "REVIEW", "FAIL"] }
  }
}
```

---

## DECISION Pattern
```json
{
  "type": "object",
  "required": ["meta", "options", "recommendation"],
  "properties": {
    "options": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "pros", "cons", "score"],
        "properties": {
          "name": { "type": "string" },
          "pros": { "type": "array", "items": { "type": "string" } },
          "cons": { "type": "array", "items": { "type": "string" } },
          "score": { "type": "number", "minimum": 0, "maximum": 10 }
        }
      }
    },
    "recommendation": {
      "type": "object",
      "required": ["choice", "rationale"],
      "properties": {
        "choice": { "type": "string" },
        "rationale": { "type": "string" },
        "conditions": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

---

## GENERATIVE Pattern
```json
{
  "type": "object",
  "required": ["meta", "output"],
  "properties": {
    "output": {
      "type": "object",
      "required": ["content", "format", "word_count"],
      "properties": {
        "content": { "type": "string" },
        "format": { "type": "string", "enum": ["Markdown", "Plain", "HTML"] },
        "word_count": { "type": "integer" },
        "sections": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": { "type": "string" },
              "content": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```
