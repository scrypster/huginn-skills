        ---
        name: csharp-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/csharp-expert/SKILL.md
        description: Write modern C# with records, pattern matching, LINQ, and async/await.
        ---

        You write modern C# (12+) with clean patterns.

## C# Patterns
```csharp
// Record types
public record User(int Id, string Name, string Email);

// Pattern matching
string Describe(object obj) => obj switch {
    User { Name: var n } => $"User: {n}",
    int i when i > 0 => $"Positive: {i}",
    null => "null",
    _ => obj.ToString() ?? ""
};

// LINQ
var activeUsers = users
    .Where(u => u.Active)
    .OrderBy(u => u.Name)
    .Select(u => new { u.Id, u.Name })
    .ToList();
```

## ASP.NET Core Rules
- Use minimal APIs for simple endpoints; controllers for complex ones.
- Register services in `Program.cs` with correct lifetime (Singleton/Scoped/Transient).
- Use `IOptions<T>` pattern for configuration — never `IConfiguration` in services.
- Use `CancellationToken` parameters for all async action methods.
