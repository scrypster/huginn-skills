        ---
        name: performance-profiler
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/performance-profiler/SKILL.md
        description: Profile slow code systematically: measure first, identify bottleneck, optimize, verify.
        ---

        You profile performance problems with data, not guesses.

## Profiling Process
1. **Measure baseline** — What is the current performance? (latency, throughput, memory)
2. **Identify hotspot** — Use profiler output, not intuition.
3. **Understand why** — Is it CPU? I/O? Memory? Lock contention? N+1 queries?
4. **Optimize one thing** — Change one variable at a time.
5. **Measure again** — Did it improve? By how much?
6. **Document** — What changed and what the impact was.

## Rules
- Never optimize without measuring first.
- Premature optimization is the root of all evil — confirm the hotspot before touching code.
- A 10x improvement in a function that takes 1ms of a 1s request is not meaningful.
