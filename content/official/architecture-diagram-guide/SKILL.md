        ---
        name: architecture-diagram-guide
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/architecture-diagram-guide/SKILL.md
        description: Create clear architecture diagrams with Mermaid: system context, component, sequence.
        ---

        You create clear architecture diagrams using Mermaid syntax.

## Diagram Types

### System Context (C4 Level 1)
```mermaid
graph TD
    User[👤 User] --> App[Web App]
    App --> API[API Server]
    API --> DB[(PostgreSQL)]
    API --> Cache[(Redis)]
    API --> Email[📧 SendGrid]
```

### Sequence Diagram
```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant D as Database

    C->>A: POST /users
    A->>D: INSERT INTO users
    D-->>A: user_id = 123
    A-->>C: 201 Created {id: 123}
```

### State Machine
```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Processing: payment_received
    Processing --> Shipped: fulfill()
    Shipped --> Delivered: delivery_confirmed
    Processing --> Cancelled: cancel()
```

## Rules
- Label all arrows with the action or data, not just directions.
- Each diagram should answer one question.
- Keep diagrams under 15 nodes — complex diagrams hide complexity.
