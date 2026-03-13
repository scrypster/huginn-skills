        ---
        name: json-yaml-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/json-yaml-expert/SKILL.md
        description: Validate and transform JSON/YAML: schema, jq queries, and common pitfalls.
        ---

        You validate, query, and transform JSON and YAML data.

## jq — JSON Query Language
```bash
# Extract field
cat data.json | jq '.users[].email'

# Filter
jq '.users[] | select(.active == true)'

# Transform
jq '.users[] | {name: .name, domain: (.email | split("@")[1])}'

# Count
jq '.users | length'

# Group by
jq 'group_by(.role) | map({role: .[0].role, count: length})'
```

## YAML Pitfalls
```yaml
# Gotcha: YES/NO/TRUE/FALSE are booleans in YAML 1.1
enabled: yes    # boolean true
country: NO     # boolean false! Quote it: "NO"

# Gotcha: octal numbers
port: 0777      # YAML 1.1 parses as octal = 511

# Gotcha: multiline strings
description: |    # literal block (preserves newlines)
  Line one
  Line two
description: >    # folded block (newlines → spaces)
  Line one
  Line two
```

## Rules
- Validate JSON with `jq empty file.json` — exits 0 if valid.
- Use `yq` for YAML command-line queries (same syntax as jq).
- Always quote YAML strings that might be misinterpreted (YES, NO, 1.0, null).
