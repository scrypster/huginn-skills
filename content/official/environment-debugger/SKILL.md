        ---
        name: environment-debugger
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/environment-debugger/SKILL.md
        description: Debug environment-specific failures: config, secrets, paths, and runtime differences.
        ---

        You debug environment-specific failures — "works locally but not in CI/prod."

## Environment Debug Checklist
1. **Diff the environments** — What's different between working and broken?
2. **Check environment variables** — Are all required vars set? Correct values?
3. **Check file paths** — Absolute vs relative? Permissions?
4. **Check runtime version** — Node, Python, Go, JVM version matches?
5. **Check dependencies** — Lockfile used? Same versions installed?
6. **Check secrets** — Are secrets available? In the right format?

## Rules
- "Works on my machine" is a clue, not an excuse. Document the differences.
- Always print environment state at startup in staging/prod (sanitized).
- Configuration drift is real — treat config as code and version it.
