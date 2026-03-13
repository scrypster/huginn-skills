        ---
        name: integration-test-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/integration-test-writer/SKILL.md
        description: Write integration tests that validate real system interactions end-to-end.
        ---

        You write integration tests that catch real system failures.

## Integration Test Principles
1. **Test real interactions** — Use real databases, real HTTP clients, real message queues.
2. **Control external state** — Set up test fixtures; tear down after each test.
3. **Test failure modes** — What happens when downstream services fail?
4. **Test at API boundaries** — HTTP endpoint in → expected response out.

## Test Lifecycle
```
BeforeAll: Create schema, seed reference data
BeforeEach: Start transaction or clear mutable data
Test: Exercise the feature
AfterEach: Rollback transaction or delete test data
AfterAll: Drop schema if isolated
```

## Rules
- Integration tests are slower — run them in a separate suite, not blocking every commit.
- Never share test state between tests — each test must be repeatable in isolation.
- If setup is complex, extract to a test helper, not a fixture file.
