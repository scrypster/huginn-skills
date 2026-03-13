        ---
        name: typescript-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/typescript-expert/SKILL.md
        description: Write strict TypeScript: utility types, generics, discriminated unions, type guards.
        ---

        You write strict, expressive TypeScript.

## Type Patterns
```typescript
// Discriminated unions
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: Error }

// Type guards
function isUser(x: unknown): x is User {
  return typeof x === "object" && x !== null && "id" in x
}

// Utility types
type PartialUser = Partial<User>
type RequiredUser = Required<User>
type ReadonlyUser = Readonly<User>
type UserWithoutId = Omit<User, "id">
type UserId = Pick<User, "id">
```

## Rules
- Never use `any`. Use `unknown` and narrow with type guards.
- Prefer `interface` for objects, `type` for unions/intersections.
- Enable `strict: true` in tsconfig — no exceptions.
