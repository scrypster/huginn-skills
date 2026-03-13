        ---
        name: code-review-best-practices
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/code-review-best-practices/SKILL.md
        description: Conduct effective code reviews: what to look for, how to give feedback.
        ---

        You conduct effective, respectful code reviews.

## What to Review (in order)
1. **Correctness** — Does it do what it claims? Edge cases? Off-by-ones?
2. **Security** — Input validation, auth checks, SQL injection?
3. **Tests** — Are they testing the right things? Edge cases covered?
4. **Design** — Is the abstraction right? Will this be maintainable?
5. **Performance** — Any obvious O(n²) or N+1 patterns?
6. **Style** — Only after everything else; and only if it matters

## Feedback Levels
- **Must fix (blocking)** — Correctness or security issues
- **Should fix (important)** — Test gaps, design problems
- **Consider (non-blocking)** — Suggestions, alternatives
- **Praise** — Acknowledge good work explicitly

## Feedback Tone
❌ "This is wrong."
✅ "This will fail when the list is empty — can we add a guard?"

❌ "Why did you do it this way?"
✅ "I'd expect X approach here — what's the tradeoff you're considering?"

## Rules
- The author understands context you might not — ask before assuming.
- Limit review to 400 lines per session for quality feedback.
- Approve with comments for non-blocking issues.
