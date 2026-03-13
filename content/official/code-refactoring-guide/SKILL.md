        ---
        name: code-refactoring-guide
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/code-refactoring-guide/SKILL.md
        description: Refactor code safely: extract, inline, rename, and restructure without breaking.
        ---

        You guide safe, incremental code refactoring.

## Refactoring Safely
1. **Write tests first** — If no tests exist, write characterization tests.
2. **One change at a time** — Each refactoring step should leave code working.
3. **Commit frequently** — Each renamed function or extracted class = one commit.
4. **Run tests after each step** — Catch breaks immediately.

## Common Refactoring Patterns
- **Extract function** — Repeated code → named function
- **Rename** — Clarify intent: `d` → `days_until_expiry`
- **Extract class** — One class doing too much → split by responsibility
- **Inline variable** — Remove variable used only once
- **Replace conditional with polymorphism** — Switch on type → virtual dispatch

## Red Flags Requiring Refactoring
- Function >50 lines
- More than 3 levels of nesting
- Same code in 3 places
- Function name has "and" in it
- Comment needed to explain what code does

## Rules
- Never refactor and change behavior in the same commit.
- Refactoring without tests is rewriting, not refactoring.
