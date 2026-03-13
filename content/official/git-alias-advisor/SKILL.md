        ---
        name: git-alias-advisor
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/git-alias-advisor/SKILL.md
        description: Set up powerful git aliases and config that reduce friction in daily workflows.
        ---

        You set up git aliases and config that dramatically reduce daily friction.

## Essential Aliases
```ini
[alias]
    st = status -sb
    co = checkout
    br = branch -vv
    lg = log --oneline --graph --decorate --all
    last = log -1 HEAD --stat
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
    wip = !git add -A && git commit -m "WIP: $(date)"
    standup = log --since=yesterday --author="$(git config user.name)" --oneline
    aliases = config --get-regexp alias
```

## Useful Config
```ini
[core]
    autocrlf = input
    editor = vim
[push]
    default = current
[pull]
    rebase = true
[diff]
    tool = vimdiff
```

## Rules
- Aliases should save keystrokes AND prevent mistakes (e.g., `push -f` should never be aliased).
- Document any non-obvious aliases with a comment.
