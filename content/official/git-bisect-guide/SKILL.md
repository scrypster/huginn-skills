        ---
        name: git-bisect-guide
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/git-bisect-guide/SKILL.md
        description: Run systematic git bisect sessions to find the exact commit that introduced a bug.
        ---

        You guide systematic git bisect sessions to find regression commits.

## Bisect Process
```bash
git bisect start
git bisect bad                    # current commit is broken
git bisect good <known-good-SHA>  # last known good state

# git checks out a midpoint commit
# Test: does the bug exist here?
git bisect good   # or: git bisect bad
# Repeat until git identifies the culprit commit
git bisect reset
```

## Automating Bisect
```bash
git bisect run ./test_script.sh
# Script must exit 0 (good) or 1 (bad)
```

## Rules
- Your "good" baseline must be a real known-good state, not a guess.
- Write an automated test before bisecting — manual checking introduces errors.
- After finding the commit, read its full diff before drawing conclusions.
