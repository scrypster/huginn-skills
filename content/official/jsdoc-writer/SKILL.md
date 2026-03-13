        ---
        name: jsdoc-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/jsdoc-writer/SKILL.md
        description: Write complete JSDoc comments for public APIs with types, params, and examples.
        ---

        You write complete JSDoc documentation for JavaScript and TypeScript APIs.

## JSDoc Template
```typescript
/**
 * Creates a new user account and sends a welcome email.
 *
 * @param options - User creation options
 * @param options.email - User's email address (must be unique)
 * @param options.name - User's display name
 * @param options.role - User's role (defaults to 'member')
 * @returns The created user object
 * @throws {ValidationError} If email format is invalid
 * @throws {DuplicateError} If email is already registered
 *
 * @example
 * const user = await createUser({
 *   email: 'alice@example.com',
 *   name: 'Alice',
 * })
 * console.log(user.id) // 'usr_01HNMKP'
 */
async function createUser(options: CreateUserOptions): Promise<User>
```

## Rules
- Document every public function — types alone are not documentation.
- Every `@param` needs a description, not just a name.
- Every `@throws` must document the class and trigger condition.
- `@example` is required for non-trivial functions.
