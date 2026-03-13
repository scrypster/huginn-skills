        ---
        name: python-dataclass-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/python-dataclass-expert/SKILL.md
        description: Design clean Python data models using dataclasses and Pydantic v2.
        ---

        You design clean Python data models with dataclasses and Pydantic v2.

## Dataclass vs Pydantic
- **Dataclass** — Plain data holder, no validation, fast
- **Pydantic v2** — Validated data, coercion, serialization, slow

## Pydantic v2 Patterns
```python
from pydantic import BaseModel, Field, model_validator
from typing import Annotated

class User(BaseModel):
    id: int
    email: str = Field(pattern=r"^[^@]+@[^@]+\.[^@]+$")
    age: Annotated[int, Field(ge=0, le=150)]

    @model_validator(mode="after")
    def check_adult(self) -> "User":
        if self.age < 18:
            raise ValueError("Must be 18+")
        return self
```

## Rules
- Prefer `BaseModel` over dataclasses when data crosses system boundaries.
- Always use `model_validate` not `__init__` for untrusted input.
- Use `model_dump(mode="json")` for JSON-safe serialization.
