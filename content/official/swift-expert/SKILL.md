        ---
        name: swift-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/swift-expert/SKILL.md
        description: Write idiomatic Swift: optionals, Codable, async/await, and SwiftUI patterns.
        ---

        You write idiomatic modern Swift.

## Swift Patterns
```swift
// Codable
struct User: Codable, Identifiable {
    let id: UUID
    let name: String
    let email: String
}

// async/await
func fetchUser(id: UUID) async throws -> User {
    let url = URL(string: "/api/users/\(id)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// SwiftUI
struct UserView: View {
    @StateObject private var vm = UserViewModel()

    var body: some View {
        List(vm.users) { user in
            Text(user.name)
        }
        .task { await vm.load() }
    }
}
```

## Rules
- Use `async/await` not Combine for new code (iOS 15+).
- Use `@StateObject` for owned view models, `@ObservedObject` for injected.
- Force unwrap (`!`) only in test code or `IBOutlet` — never in production logic.
