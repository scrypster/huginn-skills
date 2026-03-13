        ---
        name: git-history-cleaner
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/git-history-cleaner/SKILL.md
        description: Clean up messy commit history with interactive rebase: squash, fixup, reword.
        ---

        You clean up commit history to produce a clear, meaningful record.

## Interactive Rebase Commands
```bash
git rebase -i HEAD~N    # clean up last N commits
git rebase -i <SHA>^    # clean up from SHA to HEAD
```

## Commands in Rebase Editor
- `pick` — keep commit as-is
- `reword (r)` — keep but edit message
- `squash (s)` — merge into previous commit, combine messages
- `fixup (f)` — merge into previous commit, discard this message
- `drop (d)` — delete this commit

## Clean History Checklist
- [ ] Each commit does one logical thing
- [ ] No "WIP", "fixup", "typo" commits
- [ ] No merge commits in feature branch (use rebase)
- [ ] Commit messages are meaningful

## Rules
- Never rebase commits that have been pushed to shared branches.
- Squash "fixup" commits into their parents before merging.
