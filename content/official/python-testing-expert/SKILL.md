        ---
        name: python-testing-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/python-testing-expert/SKILL.md
        description: Write pytest suites with fixtures, parametrize, and async support.
        ---

        You write high-quality pytest test suites.

## Pytest Patterns
```python
# Fixtures
@pytest.fixture
def db(tmp_path):
    db = Database(tmp_path / "test.db")
    db.migrate()
    yield db
    db.close()

# Parametrize
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("", ""),
    ("123", "123"),
])
def test_upper(input, expected):
    assert upper(input) == expected

# Async
@pytest.mark.asyncio
async def test_fetch():
    result = await fetch("https://example.com")
    assert result.status == 200
```

## Rules
- Use `tmp_path` fixture for temp files — never hardcode `/tmp/`.
- Parametrize is better than multiple similar test functions.
- Mark slow tests with `@pytest.mark.slow` and skip in fast runs.
