        ---
        name: cqrs-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/cqrs-expert/SKILL.md
        description: Implement CQRS: separate read/write models, command handlers, and query projections.
        ---

        You implement CQRS (Command Query Responsibility Segregation) correctly.

## CQRS Structure
```
Commands → Command Handlers → Write Model → Events → Event Handlers → Read Models
                                                                      ↓
Queries → Query Handlers → Read Models (optimized for query)
```

## Command Handler Pattern
```python
@dataclass
class PlaceOrderCommand:
    user_id: str
    items: list[OrderItem]

class PlaceOrderHandler:
    def handle(self, cmd: PlaceOrderCommand) -> OrderId:
        order = Order.create(cmd.user_id, cmd.items)
        self.repo.save(order)
        self.events.publish(order.uncommitted_events)
        return order.id
```

## When to Use CQRS
- Read patterns differ dramatically from write patterns
- High read load that can't be addressed with simple indexes
- Complex domain logic that benefits from event sourcing

## Rules
- Start without CQRS — add it when you feel the pressure.
- Commands are imperative requests; they can be rejected.
- Events are facts; they cannot be "rejected."
