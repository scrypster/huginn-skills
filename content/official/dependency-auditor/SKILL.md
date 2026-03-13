        ---
        name: dependency-auditor
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/dependency-auditor/SKILL.md
        description: Audit project dependencies for known CVEs and outdated packages.
        ---

        You audit project dependencies for security vulnerabilities.

## Audit Tools by Ecosystem
```bash
# npm/Node
npm audit
npx better-npm-audit audit

# Python
pip-audit
safety scan

# Go
govulncheck ./...

# Ruby
bundle audit
```

## Triage Process
1. **Critical/High CVEs** — Fix immediately
2. **Medium CVEs** — Fix in next sprint
3. **Low CVEs** — Track in backlog
4. **Outdated (no CVE)** — Schedule upgrade

## False Positive Handling
- CVE affects a code path you don't use? Document why + add exception
- No fix available? Add to risk register with mitigation plan

## Rules
- Run dependency audits in CI — fail builds on Critical/High CVEs.
- Pin exact versions in lockfiles to prevent supply chain drift.
- Track known-safe exceptions in `.audit-ignore` or equivalent.
