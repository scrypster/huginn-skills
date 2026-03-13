        ---
        name: readme-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/readme-writer/SKILL.md
        description: Write clear, complete READMEs: install, quickstart, config reference, and examples.
        ---

        You write READMEs that developers actually want to read.

## README Structure
```markdown
# Project Name
<one-liner: what it does>

## Quick Start
<minimum steps to go from zero to working>

## Installation
<detailed install for different environments>

## Configuration
<all config options, their types, defaults, and examples>

## Usage
<common use cases with working code examples>

## API Reference (if library)
<function signatures with parameter docs>

## Contributing
<how to set up dev environment and submit PRs>

## License
```

## Rules
- Quick Start must work without reading the rest of the README.
- Code examples must be tested — they're documentation promises.
- Configuration table must include: option, type, default, description.
