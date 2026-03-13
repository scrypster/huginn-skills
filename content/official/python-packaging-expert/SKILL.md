        ---
        name: python-packaging-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/python-packaging-expert/SKILL.md
        description: Set up modern Python packages with pyproject.toml, uv, and publishing best practices.
        ---

        You set up modern Python packages correctly.

## pyproject.toml Template
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["httpx>=0.27"]

[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff"]

[tool.ruff]
line-length = 100

[tool.mypy]
strict = true
```

## Rules
- Always pin transitive dependencies in `requirements.lock`, not `pyproject.toml`.
- Use `uv` for fast dependency management.
- Publish to PyPI from CI only, never manually.
