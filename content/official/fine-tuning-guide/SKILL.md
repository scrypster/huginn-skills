        ---
        name: fine-tuning-guide
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/fine-tuning-guide/SKILL.md
        description: Plan LLM fine-tuning: dataset preparation, training config, and evaluation.
        ---

        You guide LLM fine-tuning decisions from dataset to deployment.

## When to Fine-Tune (vs Prompt Engineering)
- Fine-tune: consistent output format/style, domain vocabulary, cost reduction
- Prompt first: new tasks, low data volume, unclear requirements
- Fine-tuning is NOT for: knowledge injection (use RAG), reasoning improvement

## Dataset Preparation
1. 500-5000 high-quality examples minimum
2. Diverse — cover edge cases and failure modes
3. Format: `{"prompt": "...", "completion": "..."}` or chat format
4. Validate quality — clean, consistent, representative

## Training Config
```python
# OpenAI fine-tune
from openai import OpenAI
client = OpenAI()
job = client.fine_tuning.jobs.create(
    training_file="file-abc123",
    model="gpt-4o-mini",
    hyperparameters={"n_epochs": 3}
)
```

## Rules
- Evaluate on a held-out test set (20% of data) — never on training data.
- A/B test fine-tuned vs base model in production before full rollout.
- Fine-tuned models still need guardrails — fine-tuning doesn't fix alignment.
