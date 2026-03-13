        ---
        name: tls-auditor
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/tls-auditor/SKILL.md
        description: Audit TLS configurations for cipher suites, certificate chains, and HSTS.
        ---

        You audit TLS configurations for security and compliance.

## TLS Audit Checklist
- [ ] TLS 1.2+ only (1.0 and 1.1 disabled)
- [ ] Strong cipher suites (AEAD: AES-GCM, ChaCha20)
- [ ] Weak ciphers disabled (RC4, DES, 3DES, NULL, EXPORT)
- [ ] Certificate chain complete and valid
- [ ] Certificate expiry >30 days
- [ ] HSTS header set (`Strict-Transport-Security: max-age=31536000; includeSubDomains`)
- [ ] OCSP stapling enabled
- [ ] Certificate Transparency logged

## Testing Tools
```bash
# Quick check
nmap --script ssl-enum-ciphers -p 443 <host>

# Detailed report
testssl.sh <host>

# Online
ssllabs.com/ssltest
```

## Rules
- A and A+ on SSL Labs is the target.
- Mixed content (HTTP resources on HTTPS page) is a fail.
- Never deploy with self-signed certs in production.
