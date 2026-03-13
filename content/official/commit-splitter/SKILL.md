        ---
        name: commit-splitter
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/commit-splitter/SKILL.md
        description: Split large commits into focused, atomic commits using git add -p.
        ---

        You split large commits into focused, atomic commits.

## Splitting a Commit
```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Interactively stage partial changes
git add -p    # select hunks for first commit

# Commit first logical change
git commit -m "feat: add user model"

# Stage remaining changes
git add -p    # select hunks for second commit
git commit -m "feat: add user repository"
```

## What Makes a Good Atomic Commit
- One logical change (feature, fix, or refactor — not mixed)
- Tests committed with the code they test
- Passes CI on its own (can be checked out and built)

## Rules
- Never split a commit that leaves the code in a broken state.
- If a commit is hard to split, that's a signal it's doing too much.
