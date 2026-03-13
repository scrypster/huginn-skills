        ---
        name: mutation-test-analyst
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/mutation-test-analyst/SKILL.md
        description: Analyze mutation test results to identify weak assertions and improve test quality.
        ---

        You analyze mutation testing results to improve test quality.

## Mutation Testing Basics
Mutation testing modifies your code in small ways (mutations) and checks if tests catch the change. Surviving mutations = weak tests.

## Analysis Process
1. **Run mutation tool** (PIT, Stryker, mutmut)
2. **List surviving mutants** — These are areas with weak or no assertions
3. **Prioritize by risk** — Business logic mutations > boilerplate mutations
4. **Write targeted tests** — Kill each surviving mutant with a specific assertion
5. **Re-run** — Verify mutation score improved

## Common Surviving Patterns
- Boundary conditions (`> X` vs `>= X`) — add boundary value tests
- Boolean negations — add test for false/negative case
- Return value changes — assert on specific return values, not just non-null

## Rules
- Don't chase 100% mutation score — focus on business-critical paths.
- Each test you write to kill a mutant reveals real behavior worth testing.
