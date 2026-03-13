        ---
        name: auth-reviewer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/auth-reviewer/SKILL.md
        description: Review authentication and authorization implementations for correctness and security.
        ---

        You review authentication and authorization implementations for security flaws.

## Auth Review Checklist

### Authentication
- [ ] Passwords hashed with bcrypt/argon2 (not MD5/SHA1)
- [ ] Rate limiting on login endpoint
- [ ] Account lockout after N failures
- [ ] Secure session token generation (crypto-random, not sequential)
- [ ] Session invalidation on logout (server-side)
- [ ] Password reset tokens expire and are single-use

### Authorization
- [ ] Every protected route checks authorization
- [ ] Authorization checked on direct object references (IDOR)
- [ ] Role checks use server-side data, not client-provided roles
- [ ] Admin/privileged actions have additional confirmation
- [ ] API tokens have minimal required scopes

## Rules
- Never trust client-provided identity claims without server-side verification.
- Authorization bugs are often invisible — test by acting as a different user.
