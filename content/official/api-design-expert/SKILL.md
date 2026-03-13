        ---
        name: api-design-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/api-design-expert/SKILL.md
        description: Design intuitive REST APIs: resources, verbs, versioning, and error schemas.
        ---

        You design intuitive, consistent REST APIs.

## Resource Design
```
GET    /users          — list users
POST   /users          — create user
GET    /users/{id}     — get user
PUT    /users/{id}     — replace user
PATCH  /users/{id}     — update user fields
DELETE /users/{id}     — delete user

GET    /users/{id}/orders   — list user's orders
POST   /users/{id}/orders   — create order for user
```

## Versioning Strategies
- **URL**: `/api/v1/users` (most common, simplest)
- **Header**: `Accept: application/vnd.api+json; version=1`
- **Query**: `/users?api-version=1` (least preferred)

## Error Schema
```json
{
  "error": { "code": "USER_NOT_FOUND", "message": "User 123 not found" }
}
```

## Rules
- Nouns for resources, HTTP verbs for actions.
- 200 for success, 201 for created, 204 for deleted.
- Consistent error format across all endpoints.
- Pagination must use cursor-based for large datasets.
