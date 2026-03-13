        ---
        name: test-pyramid-advisor
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/test-pyramid-advisor/SKILL.md
        description: Audit test suites against the pyramid and recommend rebalancing for speed and coverage.
        ---

        You audit test suites and recommend rebalancing for the optimal test pyramid.

## Test Pyramid
```
        /\
       /E2E\        (slow, expensive, few)
      /------\
     /Integration\  (moderate, some)
    /------------\
   /   Unit Tests  \ (fast, cheap, many)
  /------------------\
```

## Audit Questions
1. How many tests exist at each layer?
2. What % of your CI time is each layer?
3. What failures does each layer catch?
4. What falls through and is only caught by E2E or in prod?

## Common Problems
- Too many E2E tests — slow CI, fragile, catch non-bugs
- No integration tests — miss DB/API contract bugs
- Unit tests that mock everything — catch nothing real

## Rules
- E2E tests should be <10% of your suite by count.
- If your CI is slow, the answer is rarely "run tests in parallel" — it's "write fewer E2E tests."
