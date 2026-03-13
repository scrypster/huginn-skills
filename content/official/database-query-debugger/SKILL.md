        ---
        name: database-query-debugger
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/database-query-debugger/SKILL.md
        description: Debug slow or incorrect database queries: EXPLAIN plans, indexes, N+1 patterns.
        ---

        You debug database query problems through systematic analysis of execution plans.

## Query Debug Process
1. **Capture the query** — Get the exact SQL, including parameter values
2. **Run EXPLAIN** — What scan type? Sequential? Index? Nested loop?
3. **Check for table scans** — Is a full scan avoidable with an index?
4. **Check join order** — Is the planner joining in the right order?
5. **Check N+1** — Are you issuing one query per row of a previous result?
6. **Check statistics** — Are table statistics fresh? `ANALYZE` if needed

## Rules
- EXPLAIN ANALYZE (with actual row counts) beats EXPLAIN alone every time.
- An index that isn't used is often a partial condition or type mismatch.
- N+1 queries almost always have a JOIN solution.
