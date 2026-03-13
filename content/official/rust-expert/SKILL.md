        ---
        name: rust-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/rust-expert/SKILL.md
        description: Write idiomatic Rust: ownership, error handling with ?, and iterator chains.
        ---

        You write idiomatic, safe Rust code.

## Rust Patterns
```rust
// Error handling
fn read_config(path: &Path) -> anyhow::Result<Config> {
    let contents = fs::read_to_string(path)
        .with_context(|| format!("reading config from {}", path.display()))?;
    let config: Config = toml::from_str(&contents)?;
    Ok(config)
}

// Iterator chains
let active_users: Vec<&User> = users.iter()
    .filter(|u| u.active)
    .take(10)
    .collect();

// Derive macros
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct User { id: u64, name: String, active: bool }
```

## Rules
- Use `anyhow` for application error handling, `thiserror` for library errors.
- Prefer `?` over `.unwrap()` in fallible functions.
- Never `clone()` to fix borrow checker — understand why borrowing fails first.
