        ---
        name: unit-test-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/unit-test-writer/SKILL.md
        description: Write thorough unit tests: happy path, error paths, edge cases, and mocks.
        ---

        You write thorough, maintainable unit tests.

## Test Structure (AAA)
```
// Arrange — set up inputs, mocks, expected outputs
// Act — call the function under test
// Assert — verify the output
```

## Test Coverage Checklist
- [ ] Happy path
- [ ] Empty / zero / null inputs
- [ ] Boundary values (min, max, off-by-one)
- [ ] Error conditions (what does it do when upstream fails?)
- [ ] Concurrent/parallel access (if applicable)

## Rules
- One assertion per test (or a tight group of related assertions).
- Test behavior, not implementation — don't assert on private state.
- Mock only what crosses a system boundary (I/O, clock, randomness, network).
- Test names should be sentences: "returns empty list when input is nil" not "testNilInput."
