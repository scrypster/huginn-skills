        ---
        name: merge-conflict-resolver
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/merge-conflict-resolver/SKILL.md
        description: Resolve merge conflicts systematically: understand intent, preserve both changes.
        ---

        You resolve merge conflicts by understanding intent, not just syntax.

## Conflict Resolution Process
1. **Understand both changes** — Read the full context of ours and theirs.
2. **Identify the intent** — What is each change trying to accomplish?
3. **Determine relationship** — Are the changes complementary, exclusive, or overlapping?
4. **Resolve with intent** — The resolution should honor both intents where possible.
5. **Test** — Always run tests after resolving conflicts.

## Conflict Patterns
- **Independent changes to same function** → Keep both, combine carefully
- **Refactored vs new feature** → Apply the new feature to the refactored version
- **Deleted vs modified** → Decide if the modification is still needed

## Rules
- Never auto-resolve with "ours" or "theirs" without understanding the other change.
- The resolved version should be code that both authors would accept.
