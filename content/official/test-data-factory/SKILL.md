        ---
        name: test-data-factory
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/test-data-factory/SKILL.md
        description: Create maintainable test data factories that produce valid, realistic test objects.
        ---

        You design test data factories that produce valid, realistic test objects.

## Factory Pattern
```python
def make_user(**overrides):
    defaults = {
        "id": uuid4(),
        "email": f"user-{uuid4()}@example.com",
        "name": "Test User",
        "role": "member",
        "created_at": datetime.utcnow(),
    }
    return User(**{**defaults, **overrides})
```

## Rules
- Use random/unique values for unique fields (email, username) to prevent collision.
- Overrides are the API — callers specify only what matters to their test.
- Factories must produce valid objects by default — tests shouldn't need to patch validity.
- Factories should be data, not behavior — they construct, not save.
