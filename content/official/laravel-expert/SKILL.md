        ---
        name: laravel-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/laravel-expert/SKILL.md
        description: Build Laravel applications with Eloquent, queues, and proper service architecture.
        ---

        You build clean Laravel applications following Laravel conventions.

## Service Layer Pattern
```php
class UserService
{
    public function __construct(
        private readonly UserRepository $users,
        private readonly Dispatcher $events,
    ) {}

    public function create(CreateUserData $data): User
    {
        $user = $this->users->create([
            'name' => $data->name,
            'email' => $data->email,
            'password' => Hash::make($data->password),
        ]);

        $this->events->dispatch(new UserCreated($user));
        return $user;
    }
}
```

## Rules
- Thin controllers — logic belongs in service classes.
- Use form requests for validation — not inline `$request->validate()`.
- Queue all non-critical work (emails, webhooks, notifications).
- Use `DB::transaction()` for operations that must be atomic.
