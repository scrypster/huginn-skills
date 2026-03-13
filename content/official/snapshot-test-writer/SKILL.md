        ---
        name: snapshot-test-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/snapshot-test-writer/SKILL.md
        description: Write focused snapshot tests with meaningful assertions and easy update paths.
        ---

        You write snapshot tests that catch meaningful regressions.

## When to Use Snapshots
- Complex rendered output (HTML, JSON, CLI output) where structure matters
- Not for: simple values, external data, frequently changing content

## Snapshot Test Rules
- **Name snapshots** — "renders correctly" is useless. "renders with error state" is meaningful.
- **Keep snapshots small** — Snapshot only the component, not the full page.
- **Review snapshot diffs** — A snapshot update that looks wrong IS wrong.
- **Delete obsolete snapshots** — Stale snapshots give false confidence.

## Snapshot Anti-Patterns
- Snapshotting random data (UUIDs, timestamps) — makes every run fail
- Snapshotting external API responses — external data changes
- Never reviewing snapshot updates (treat as code changes)
