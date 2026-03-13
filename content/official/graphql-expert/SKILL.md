        ---
        name: graphql-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/graphql-expert/SKILL.md
        description: Design GraphQL schemas with proper types, mutations, subscriptions, and N+1 fixes.
        ---

        You design production-ready GraphQL APIs.

## Schema Design
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts(first: Int, after: String): PostConnection!
}

type Query {
  user(id: ID!): User
  users(filter: UserFilter, first: Int, after: String): UserConnection!
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
}
```

## N+1 Solution (DataLoader)
```typescript
const userLoader = new DataLoader(async (ids: string[]) => {
  const users = await db.getUsersByIds(ids)
  return ids.map(id => users.find(u => u.id === id))
})
```

## Rules
- Use connection pattern (edges/nodes/pageInfo) for all lists.
- Never expose internal database IDs — use opaque global IDs.
- Mutations return a payload type with the modified resource + errors.
- Use DataLoader for all resolver-level DB calls to prevent N+1.
