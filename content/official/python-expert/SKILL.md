        ---
        name: python-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/python-expert/SKILL.md
        description: Write idiomatic Python: type hints, dataclasses, generators, context managers.
        ---

        You write idiomatic, modern Python (3.11+).

## Python Best Practices
1. **Type hints everywhere** — All functions, all class attributes.
2. **Dataclasses for data** — Use `@dataclass` for plain data holders.
3. **Context managers for resources** — Files, connections, locks.
4. **Generators for sequences** — Don't build lists you iterate once.
5. **f-strings for formatting** — Not `.format()` or `%`.
6. **Pathlib for paths** — Not `os.path`.
7. **Walrus operator** — `if (n := len(a)) > 10: print(n)`

## Rules
- Prefer composition over inheritance.
- Use `abc.ABC` for interfaces, not duck-typing-hope.
- Error handling: catch specific exceptions, not bare `except:`.
- Always add `if __name__ == "__main__":` guard to scripts.
