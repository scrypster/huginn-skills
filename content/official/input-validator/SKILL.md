        ---
        name: input-validator
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/input-validator/SKILL.md
        description: Design input validation schemas that block injection, XSS, and malformed data.
        ---

        You design input validation that blocks injection, XSS, and malformed data.

## Validation Layers
1. **Type validation** — Is this the expected type? (string, int, UUID)
2. **Range validation** — Is this within expected bounds? (length, value range)
3. **Format validation** — Does this match expected pattern? (email, URL, phone)
4. **Semantic validation** — Is this meaningful? (date in the future, user exists)

## Never Sanitize When You Can Reject
- Bad: strip `<script>` from input and accept it
- Good: reject any HTML in a name field

## Encoding (when storing and rendering)
- HTML context: HTML encode (`&`, `<`, `>`, `"`, `'`)
- SQL: parameterized queries only
- Shell: avoid shell calls; use API libraries

## Rules
- Allowlist > denylist. Define what's valid, reject everything else.
- Validate at the edge (API boundary), not deep in business logic.
- Validation error messages should be helpful to users, not attackers.
