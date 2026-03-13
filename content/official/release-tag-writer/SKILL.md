        ---
        name: release-tag-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/release-tag-writer/SKILL.md
        description: Create well-formed git tags and release notes following SemVer conventions.
        ---

        You create well-formed git tags and release notes following SemVer.

## SemVer Rules
- **MAJOR** (1.0.0 → 2.0.0) — breaking API changes
- **MINOR** (1.0.0 → 1.1.0) — new features, backward compatible
- **PATCH** (1.0.0 → 1.0.1) — bug fixes, backward compatible

## Tag Command
```bash
git tag -a v1.2.3 -m "Release v1.2.3 — <one-line summary>"
git push origin v1.2.3
```

## Release Notes Template
```markdown
## v1.2.3 — <date>

### What's New
- <feature>

### Bug Fixes
- <fix>

### Breaking Changes
- None

### Upgrade Notes
<any migration steps>
```

## Rules
- Pre-release: `1.0.0-alpha.1`, `1.0.0-rc.1`
- Build metadata: `1.0.0+build.123`
- Tag the commit, not the branch.
