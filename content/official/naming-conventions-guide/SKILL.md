        ---
        name: naming-conventions-guide
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/naming-conventions-guide/SKILL.md
        description: Name variables, functions, and modules clearly: intent over abbreviation.
        ---

        You help name code entities clearly and consistently.

## Naming Principles
1. **Intent over brevity** — `days_until_renewal` not `d` or `dur`
2. **Pronounceable** — If you can't say it, readers can't think it
3. **Searchable** — Avoid single letters except loop counters
4. **Consistent** — Same concept, same name throughout the codebase
5. **Context-free** — Don't repeat class name in method name

## By Entity Type
```python
# Variables: noun phrases
user_count = 0         # not: cnt, n, uc
is_active = True       # not: active, a, flag

# Functions: verb phrases
def fetch_user(id):    # not: getUser, user, doFetch
def calculate_tax():   # not: tax, taxCalc

# Classes: singular nouns
class Order:           # not: Orders, OrderManager
class UserRepository:  # not: UserRepo, Users

# Constants: screaming snake
MAX_RETRY_COUNT = 3    # not: maxRetry, MAX_RETRIES, 3 (magic number)
```

## Rules
- If you need a comment to explain the name, rename it.
- Boolean names start with `is_`, `has_`, `can_`, `should_`.
- Never abbreviate unless the abbreviation is more familiar than the full word (HTTP, URL, ID).
