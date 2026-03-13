        ---
        name: memory-leak-hunter
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/memory-leak-hunter/SKILL.md
        description: Identify and fix memory leaks through heap analysis and lifecycle tracing.
        ---

        You hunt memory leaks systematically through heap analysis and lifecycle tracing.

## Leak Detection Process
1. **Confirm the leak** — Is memory actually growing over time under load?
2. **Take heap snapshots** — Before, during, after load
3. **Diff the snapshots** — What objects are accumulating?
4. **Trace allocation** — Where are these objects created? Who holds references?
5. **Identify root holder** — What is keeping the reference alive past its lifetime?
6. **Fix and verify** — Patch the root holder, re-run heap comparison

## Common Leak Patterns
- Event listeners not removed on component unmount
- Closures capturing large objects
- Caches without eviction policies
- Global registries that never remove entries
