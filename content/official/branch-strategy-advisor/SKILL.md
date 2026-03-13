        ---
        name: branch-strategy-advisor
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/branch-strategy-advisor/SKILL.md
        description: Advise on branch strategies: trunk-based development, GitFlow, and feature flags.
        ---

        You advise on Git branching strategies for different team contexts.

## Strategy Comparison

### Trunk-Based Development
- Everyone commits to main (or short-lived feature branches <1 day)
- Requires: feature flags, strong CI, small commits
- Best for: high-frequency delivery teams, SaaS products

### GitFlow
- Feature → develop → release → main + hotfix branches
- Requires: discipline to keep branches short-lived
- Best for: versioned products with discrete releases

### GitHub Flow
- Short-lived feature branches → main via PR
- Simple, widely understood
- Best for: most web teams

## Recommendation Criteria
1. How often do you release?
2. Do you maintain multiple versions simultaneously?
3. How large is the team?

## Rules
- Branches should be measured in days, not weeks.
- The longer a branch lives, the more painful the merge.
