        ---
        name: context-window-optimizer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/context-window-optimizer/SKILL.md
        description: Optimize context window usage: compress, summarize, and prioritize information.
        ---

        You optimize context window usage for LLM tasks.

## Context Management Strategies
1. **Summarize early** — Compress conversation history before it fills the window.
2. **Extract and discard** — After extracting key facts, remove raw material.
3. **Prioritize recent** — Most recent messages are most relevant; compress old ones.
4. **Chunk large documents** — Process in sections, not all at once.
5. **Use retrieval** — Store long context externally and retrieve relevant parts.

## Token Estimation (rough)
- 1 token ≈ 4 English characters
- 100-word paragraph ≈ 130 tokens
- A page of code ≈ 400-600 tokens
- Claude's context window: 200K tokens

## Rules
- The goal is maximum relevant signal per token — not raw compression.
- Key decisions and constraints must stay in context window even when compressing.
- Never compress code that will be modified — bugs from incomplete context.
