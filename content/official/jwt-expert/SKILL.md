        ---
        name: jwt-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/jwt-expert/SKILL.md
        description: Implement JWTs securely: algorithm choice, validation, expiry, and refresh flows.
        ---

        You implement JWT authentication securely.

## JWT Security Checklist
- [ ] Algorithm: RS256 or ES256 (asymmetric) — never HS256 in distributed systems
- [ ] `alg` header validated server-side — never trust client-provided algorithm
- [ ] `exp` claim always set (15-60 min for access tokens)
- [ ] `iss` and `aud` claims validated on every request
- [ ] Signature verified with the correct key
- [ ] Tokens stored in httpOnly cookies — never in localStorage

## Refresh Token Pattern
```
Access token: short-lived (15 min), in memory or httpOnly cookie
Refresh token: long-lived (7 days), httpOnly cookie, single-use
On access token expiry: exchange refresh token → new access + refresh pair
On refresh token use: rotate and invalidate previous
```

## Rules
- Never store sensitive data in JWT payload — it's base64, not encrypted.
- Invalidating JWTs requires a blocklist (they're stateless by design).
- Rotate signing keys annually; support key rollover with `kid` claim.
