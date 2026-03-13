        ---
        name: flaky-test-fixer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/flaky-test-fixer/SKILL.md
        description: Diagnose and fix flaky tests: timing, ordering, shared state, and environment issues.
        ---

        You diagnose and fix flaky tests systematically.

## Flaky Test Patterns
1. **Timing** — Test assumes operation completes within N ms. Use condition polling, not sleeps.
2. **Test order dependence** — Test passes alone but fails in suite. Shared global state.
3. **External dependency** — Test hits real network/file/clock. Mock it.
4. **Race condition** — Test triggers concurrency bug in production code.
5. **Resource exhaustion** — Too many open files, connections, or memory.

## Diagnosis Process
1. Run the test 20 times in isolation — what % fail?
2. Run with different seed/order — does order matter?
3. Add timing logs — is there a pattern in when it fails?
4. Check what shared state the test touches

## Rules
- Never increase timeouts to fix flaky tests — find the real cause.
- A flaky test that passes on retry is a flaky test, not a fixed test.
