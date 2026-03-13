        ---
        name: bash-scripting-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/bash-scripting-expert/SKILL.md
        description: Write robust Bash scripts: error handling, quoting, and portable patterns.
        ---

        You write robust, portable Bash scripts.

## Script Header
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Usage
usage() { echo "Usage: $0 <arg>" >&2; exit 1; }
[[ $# -lt 1 ]] && usage

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```

## Safe Patterns
```bash
# Temp files with cleanup
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT

# Default values
name="${1:-default}"
verbose="${VERBOSE:-false}"

# Check command exists
command -v jq &>/dev/null || { echo "jq required" >&2; exit 1; }

# Safely iterate files
while IFS= read -r -d '' file; do
  process "$file"
done < <(find . -name "*.yaml" -print0)
```

## Rules
- Always quote variables: `"$var"` not `$var`.
- `set -euo pipefail` at the top of every script.
- Use `[[ ]]` not `[ ]` for conditionals in bash.
- Never use `ls` in scripts — use globbing or `find`.
