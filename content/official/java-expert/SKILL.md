        ---
        name: java-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/java-expert/SKILL.md
        description: Write modern Java: records, sealed classes, pattern matching, and streams.
        ---

        You write modern Java (21+) with clean, idiomatic patterns.

## Modern Java Patterns
```java
// Records
record User(long id, String name, String email) {}

// Sealed classes + pattern matching
sealed interface Shape permits Circle, Rectangle {}
record Circle(double radius) implements Shape {}
record Rectangle(double w, double h) implements Shape {}

double area(Shape shape) {
    return switch (shape) {
        case Circle c -> Math.PI * c.radius() * c.radius();
        case Rectangle r -> r.w() * r.h();
    };
}

// Streams
var activeNames = users.stream()
    .filter(User::active)
    .map(User::name)
    .sorted()
    .toList();
```

## Rules
- Prefer records over POJOs for data holders.
- Use `Optional` only as return type — never as field or parameter type.
- `var` is fine for local variables where type is obvious from context.
