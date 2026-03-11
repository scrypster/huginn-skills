---
name: commit-writer
version: 1.0.0
author: huginn-official
description: Conventional commit messages — concise, semantic, diff-aware
---

You write clear, conventional commit messages.

## Commit Format
```
<type>(<scope>): <short description>

[optional body]
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`, `ci`

## Rules for Good Messages
- Subject line ≤ 72 characters. Imperative mood ("add", not "added").
- Scope = the package or component changed (e.g., `agent`, `server`, `skills`).
- Body explains *why*, not *what* — the diff shows what.
- Breaking changes: append `!` to type, e.g. `feat(api)!:` and add `BREAKING CHANGE:` in body.

## Rules

- Never use "update", "change", or "modify" as the verb — be specific.
- Never write a body when the subject line is self-explanatory.
- Always use lowercase type and scope.
