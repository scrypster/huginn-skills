        ---
        name: api-test-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/api-test-writer/SKILL.md
        description: Write API tests that verify request/response contracts, auth, and error codes.
        ---

        You write API tests that verify full request/response contracts.

## API Test Checklist
- [ ] Happy path: correct request → expected status + response body
- [ ] Auth: unauthenticated → 401, unauthorized → 403
- [ ] Validation: bad input → 400 with descriptive error
- [ ] Not found: missing resource → 404
- [ ] Server error: simulate downstream failure → 500 + safe error message
- [ ] Pagination: correct `next` cursor, correct page size
- [ ] Idempotency (if applicable): repeat request → same result

## Response Contract Checks
- Status code matches spec
- Response body matches schema (required fields, correct types)
- Error responses are consistent (same error shape across all endpoints)

## Rules
- Test the HTTP contract, not internal state.
- Always test error codes — they're the API's error contract.
- Use a contract test library when possible (Pact, OpenAPI validator).
