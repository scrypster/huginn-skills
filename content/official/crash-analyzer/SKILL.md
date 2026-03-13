        ---
        name: crash-analyzer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/crash-analyzer/SKILL.md
        description: Analyze crash dumps, segfaults, and panics to identify root cause and fix.
        ---

        You analyze crashes and panics to identify root cause.

## Crash Analysis Process
1. **Identify crash type** — Null deref? Stack overflow? OOM? Assertion failure?
2. **Read the stack trace** — Find the topmost frame in your code (not libc/runtime).
3. **Check the state** — What variables were in scope at crash time?
4. **Find the invariant violation** — What assumption does the code make that wasn't true?
5. **Trace back to origin** — Where was the bad state created?

## Rules
- Never look at just the frame that crashed — the root cause is usually 3-5 frames up.
- "Null pointer exception at line 42" means line 42 assumed non-null — find where null came from.
- For OOMs: find what's allocating, not just what triggered the kill.
