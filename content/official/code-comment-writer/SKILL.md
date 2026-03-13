        ---
        name: code-comment-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/code-comment-writer/SKILL.md
        description: Write meaningful code comments that explain why, not what.
        ---

        You write code comments that explain why, not what.

## Comment Types

### When to Comment
- **Non-obvious decisions** — Why did you choose this approach over the obvious one?
- **Tricky algorithms** — Reference the paper/spec the algorithm implements.
- **Workarounds** — Explain what bug/limitation you're working around.
- **Invariants** — State what must always be true at this point.

### When Not to Comment
- Code that is self-explanatory
- Comments that just repeat the code in English
- TODO comments that will never be done

## Good Comment Example
```go
// We use SHA-256 here instead of MD5 even though both would produce
// unique cache keys — MD5 is broken for cryptographic use and we
// don't want to set a precedent of using it anywhere in the codebase.
key := sha256sum(input)
```

## Rules
- If you need a comment to explain what code does, rewrite the code.
- Comments go stale — prefer names and structure that don't need comments.
