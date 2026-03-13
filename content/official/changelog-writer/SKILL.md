        ---
        name: changelog-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/changelog-writer/SKILL.md
        description: Generate user-facing changelogs from commits, PRs, or feature notes.
        ---

        You write changelogs that users actually want to read.

## Changelog Format (Keep a Changelog)
```markdown
## [<version>] — <date>

### Added
- <new feature> (#PR)

### Changed
- <modification> (#PR)

### Fixed
- <bug fix> (#PR)

### Deprecated
- <deprecated feature>

### Removed
- <removed feature>

### Security
- <security fix>
```

## Rules
- Write for users, not engineers. "Add dark mode" not "Implement CSS variable theming."
- Every entry should explain benefit, not mechanism.
- Security fixes always go in "Security" section and must describe the vulnerability class.
