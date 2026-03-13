        ---
        name: regex-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/regex-expert/SKILL.md
        description: Write and explain regular expressions for validation, extraction, and transformation.
        ---

        You write clear, correct regular expressions and explain them.

## Regex Building Blocks
```
.       Any character (except newline)
\d      Digit [0-9]
\w      Word character [a-zA-Z0-9_]
\s      Whitespace (space, tab, newline)
^       Start of string
$       End of string
[abc]   Character class (a, b, or c)
[^abc]  Negated class (not a, b, or c)
(a|b)   Alternation (a or b)
a?      Zero or one a
a*      Zero or more a
a+      One or more a
a{3}    Exactly 3 a's
a{2,4}  Two to four a's
(?:...)  Non-capturing group
(?=...) Positive lookahead
```

## Common Patterns
```
Email:    ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
URL:      https?://[\w\-.]+(:[\d]+)?(/[\w\-./?%&=]*)?
ISO Date: \d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])
UUID:     [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
IPv4:     (?:\d{1,3}\.){3}\d{1,3}
```

## Rules
- Use named groups `(?P<name>...)` for readability.
- Test regex against both matching AND non-matching examples.
- Add `x` flag for verbose mode — allows comments and whitespace in pattern.
