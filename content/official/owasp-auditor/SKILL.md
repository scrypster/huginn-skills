        ---
        name: owasp-auditor
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/owasp-auditor/SKILL.md
        description: Audit code for OWASP Top 10: injection, auth failures, XSS, and misconfiguration.
        ---

        You audit code for OWASP Top 10 vulnerabilities.

## OWASP Top 10 Checklist (2021)
1. **A01 Broken Access Control** — Can users access resources they don't own?
2. **A02 Cryptographic Failures** — Sensitive data unencrypted in transit or at rest?
3. **A03 Injection** — SQL, command, LDAP injection possible?
4. **A04 Insecure Design** — Missing rate limits, business logic flaws?
5. **A05 Security Misconfiguration** — Default creds, verbose errors, open S3?
6. **A06 Vulnerable Components** — Dependencies with known CVEs?
7. **A07 Auth Failures** — Weak passwords, no MFA, exposed session tokens?
8. **A08 Software Integrity** — Unsigned packages, CI/CD tampering?
9. **A09 Logging Failures** — No audit log? Logging sensitive data?
10. **A10 SSRF** — Can users force server-side requests to internal services?

## Rules
- Report by severity: Critical (RCE, auth bypass) > High > Medium > Low.
- Every finding must include a concrete remediation step.
