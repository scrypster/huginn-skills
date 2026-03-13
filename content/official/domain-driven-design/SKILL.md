        ---
        name: domain-driven-design
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/domain-driven-design/SKILL.md
        description: Apply DDD concepts: aggregates, entities, value objects, and bounded contexts.
        ---

        You apply Domain-Driven Design to complex business domains.

## DDD Building Blocks

### Value Object
- Defined by its attributes, not identity
- Immutable
- Example: `Money(amount=100, currency="USD")`

### Entity
- Has a unique identity that persists through state changes
- Example: `User(id=123)` — same user even if name changes

### Aggregate
- Cluster of entities/value objects with a root entity
- External code accesses only through the root
- Invariants enforced within the aggregate

### Domain Event
- Something that happened in the domain
- Example: `OrderConfirmed(order_id, total, items)`

## Bounded Context
- A linguistic boundary where a term has a single, precise meaning
- Map how contexts relate: Shared Kernel, Customer/Supplier, Anti-Corruption Layer

## Rules
- Ubiquitous language: same terms in code, docs, and conversations.
- Aggregates should be small — one or two entities max.
- Domain events as the integration mechanism between bounded contexts.
