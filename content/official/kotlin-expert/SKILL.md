        ---
        name: kotlin-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/kotlin-expert/SKILL.md
        description: Write idiomatic Kotlin: data classes, coroutines, sealed classes, and extensions.
        ---

        You write idiomatic Kotlin for JVM and Android.

## Kotlin Patterns
```kotlin
// Data class with copy
data class User(val id: Long, val name: String, val active: Boolean = true)
val updated = user.copy(name = "Alice")

// Sealed class + when
sealed class Result<out T>
data class Success<T>(val value: T) : Result<T>()
data class Failure(val error: Throwable) : Result<Nothing>()

fun render(result: Result<User>) = when (result) {
    is Success -> renderUser(result.value)
    is Failure -> renderError(result.error)
}

// Coroutines
suspend fun fetchUser(id: Long): User = withContext(Dispatchers.IO) {
    db.getUser(id) ?: throw NotFoundException(id)
}
```

## Rules
- Prefer `data class` over POJOs — free equals/hashCode/copy.
- Use `suspend` functions, not callbacks.
- Scope coroutines to a lifecycle (`viewModelScope`, `lifecycleScope`).
- Use `?.let`, `?.run` for null-safe transformations.
