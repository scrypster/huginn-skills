        ---
        name: llm-output-parser
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/llm-output-parser/SKILL.md
        description: Build reliable LLM output parsers with schema validation and retry logic.
        ---

        You build reliable LLM output parsers with validation and retry.

## Parsing Strategy
1. **Constrained generation** — Use JSON mode or function calling where available.
2. **Schema validation** — Validate output against Pydantic/Zod schema.
3. **Retry with feedback** — On validation failure, re-prompt with the error.
4. **Graceful degradation** — Fall back to regex extraction if structured parsing fails.

## Python Pattern
```python
from pydantic import BaseModel
import instructor
import anthropic

class ExtractedData(BaseModel):
    entities: list[str]
    sentiment: Literal['positive', 'negative', 'neutral']

client = instructor.from_anthropic(anthropic.Anthropic())
data = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": text}],
    response_model=ExtractedData,
)
```

## Rules
- Never parse LLM JSON with regex — use a real parser with error recovery.
- Log raw LLM output before parsing — invaluable for debugging.
- Set max_retries=3 — most failures resolve on retry with the error message.
