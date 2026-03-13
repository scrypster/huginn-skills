# huginn-skills

The official skills registry for [Huginn](https://huginncloud.com). Browse and install
skills at [skills.huginncloud.com](https://skills.huginncloud.com).

## What is this?

Skills are Markdown files that get injected into an agent's context to give it
structured capabilities — debugging workflows, code review discipline, TDD processes, etc.

This repo is the **metadata registry** — a curated index of skills from the community.
Skill content stays in each author's own repo. Huginn fetches it at install time.

## Structure

```
registry/
  skills/
    official/      # First-party Huginn skills
    obra/          # Superpowers collection by @obra
    {handle}/      # Community submissions
  collections/     # Skill packs (groups of related skills)
content/
  official/        # Content for official skills hosted here
scripts/
  build_index.py   # Builds dist/index.json
  validate.py      # Validates registry YAML files
```

## For developers

```bash
pip install pyyaml
python scripts/validate.py    # Validate all registry files
python scripts/build_index.py # Build dist/ output locally
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) to add your skill to the registry.
