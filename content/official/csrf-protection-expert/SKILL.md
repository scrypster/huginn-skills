        ---
        name: csrf-protection-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/csrf-protection-expert/SKILL.md
        description: Implement CSRF protection: synchronizer tokens, SameSite cookies, and double submit.
        ---

        You implement CSRF protection correctly.

## Protection Strategies

### SameSite Cookies (simplest, modern browsers)
```
Set-Cookie: session=abc123; SameSite=Strict; Secure; HttpOnly
```
`Strict` — never sent cross-origin (safest, breaks OAuth redirects)
`Lax` — not sent in cross-origin POST (good default)

### Synchronizer Token Pattern
```python
# On form render: embed token
csrf_token = secrets.token_urlsafe(32)
session['csrf_token'] = csrf_token

# On form submit: validate
if request.form.get('csrf_token') != session.get('csrf_token'):
    abort(403)
```

### Double Submit Cookie
- Same token in cookie AND request header
- Server verifies they match
- Works for stateless APIs (no server-side session required)

## Rules
- CSRF protection required for all state-changing requests (POST, PUT, DELETE).
- SameSite=Lax is often sufficient for SPAs with same-site API.
- API endpoints using Authorization header are not CSRF-vulnerable (browsers don't auto-send custom headers).
