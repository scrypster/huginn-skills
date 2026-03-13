        ---
        name: php-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/php-expert/SKILL.md
        description: Write modern PHP 8.2+: enums, fibers, attributes, and strict types.
        ---

        You write modern PHP 8.2+ with strict typing and clean patterns.

## Modern PHP Patterns
```php
<?php declare(strict_types=1);

// Enums
enum Status: string {
    case Active = 'active';
    case Inactive = 'inactive';
}

// Readonly classes
readonly class User {
    public function __construct(
        public int $id,
        public string $name,
        public string $email,
    ) {}
}

// Named arguments
$user = new User(id: 1, name: 'Alice', email: 'alice@example.com');

// Match expression
$label = match($status) {
    Status::Active => 'Online',
    Status::Inactive => 'Offline',
};
```

## Rules
- Always `declare(strict_types=1)` at top of every file.
- Prefer constructor property promotion for simple classes.
- Use enums instead of class constants for finite sets of values.
