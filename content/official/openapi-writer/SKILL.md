        ---
        name: openapi-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/openapi-writer/SKILL.md
        description: Write complete OpenAPI 3.1 specifications with schemas, examples, and error responses.
        ---

        You write complete, accurate OpenAPI 3.1 specifications.

## OpenAPI Structure
```yaml
openapi: '3.1.0'
info:
  title: My API
  version: '1.0.0'

paths:
  /users/{id}:
    get:
      summary: Get user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
              example:
                id: usr_01HNMKP
                name: Alice
        '404':
          $ref: '#/components/responses/NotFound'
```

## Rules
- Use `$ref` for reusable schemas — don't repeat definitions.
- Every endpoint must document all possible error responses.
- Every schema property must have a `description`.
- Use examples — they're often more useful than schema descriptions.
