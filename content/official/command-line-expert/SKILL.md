        ---
        name: command-line-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/command-line-expert/SKILL.md
        description: Master the command line: piping, text processing, process management, and shortcuts.
        ---

        You master the Unix command line for daily productivity.

## Essential Pipelines
```bash
# Find and process
find . -name "*.log" -newer yesterday.txt | xargs grep "ERROR" | sort -u

# Text processing
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -20

# JSON processing
curl -s api.example.com/data | jq '.items[] | select(.active) | .name'

# Replace in files (in-place)
find . -name "*.yaml" -exec sed -i 's/old-image/new-image/g' {} +
```

## Process Management
```bash
# Background jobs
./long-script.sh &
jobs           # list background jobs
fg %1          # bring job 1 to foreground
disown %1      # detach from shell (survives logout)

# Process info
ps aux | grep myprocess
lsof -i :8080  # what's using port 8080?
kill -9 PID    # force kill
```

## Productivity Shortcuts
```bash
ctrl+r         # reverse history search
!!             # last command
!$             # last argument of last command
cd -           # previous directory
```

## Rules
- `man command` before Googling — the manual is authoritative.
- Prefer `--long-options` over `-f` in scripts for readability.
- Test destructive commands with `echo` first: `echo rm -rf ...` before running.
