        ---
        name: contract-test-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/contract-test-writer/SKILL.md
        description: Write consumer-driven contract tests to catch API compatibility breaks across services.
        ---

        You write consumer-driven contract tests that catch API compatibility breaks.

## Contract Testing Concepts
- **Consumer** defines what it expects from a Provider
- **Provider** verifies it can satisfy all Consumer contracts
- **Pact** is the record of the contract

## Consumer Test Example (Pact)
```python
# Consumer (service that calls User API)
def test_get_user():
    pact.given("User 123 exists").upon_receiving(
        "a request for user 123"
    ).with_request("GET", "/users/123").will_respond_with(
        200, body={"id": "123", "name": Like("Alice")}
    )
    user = client.get_user("123")
    assert user.name  # just verify we can use the response
```

## Rules
- Contracts are owned by the Consumer — Providers verify against all Consumers.
- Use matchers (`Like`, `EachLike`) not exact values — contracts shouldn't be brittle.
- Store contract artifacts in a Pact Broker for Provider verification in CI.
