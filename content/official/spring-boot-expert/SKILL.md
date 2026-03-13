        ---
        name: spring-boot-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/spring-boot-expert/SKILL.md
        description: Build Spring Boot REST APIs with validation, error handling, and testing.
        ---

        You build production-ready Spring Boot REST APIs.

## Controller Pattern
```java
@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
public class UserController {
    private final UserService service;

    @GetMapping("/{id}")
    public ResponseEntity<UserResponse> getUser(@PathVariable Long id) {
        return service.findById(id)
            .map(ResponseEntity::ok)
            .orElseThrow(() -> new NotFoundException("User " + id));
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public UserResponse createUser(@Valid @RequestBody CreateUserRequest req) {
        return service.create(req);
    }
}
```

## Rules
- Use `@Valid` on all request bodies — never trust input.
- Define a global `@ControllerAdvice` for consistent error responses.
- Use `@Transactional` on service methods, not repository methods.
