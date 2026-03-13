        ---
        name: api-doc-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/api-doc-writer/SKILL.md
        description: Write clear API documentation: endpoint descriptions, request/response examples.
        ---

        You write clear, usable API documentation.

## API Doc Template (per endpoint)
```markdown
### POST /api/v1/users

Create a new user account.

**Authentication:** Bearer token required

**Request Body**
```json
{
  "email": "alice@example.com",
  "name": "Alice Smith",
  "role": "member"
}
```

**Response: 201 Created**
```json
{
  "id": "usr_01HNMKP",
  "email": "alice@example.com",
  "name": "Alice Smith",
  "created_at": "2025-01-01T00:00:00Z"
}
```

**Errors**
| Status | Code | Description |
|--------|------|-------------|
| 400 | invalid_email | Email format invalid |
| 409 | email_taken | Email already registered |
```

## Rules
- Every endpoint needs at least one request example and one response example.
- Document ALL error codes — clients must handle them.
- Authentication requirements must be explicit, never assumed.
