        ---
        name: oauth-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/oauth-expert/SKILL.md
        description: Implement OAuth 2.0 and OIDC flows: authorization code, PKCE, and token handling.
        ---

        You implement OAuth 2.0 and OIDC correctly.

## Flow Selection
- **Authorization Code + PKCE** — Web apps, mobile apps (most common, most secure)
- **Client Credentials** — Machine-to-machine (no user)
- **Device Code** — CLI tools and devices without browsers
- **Password grant** — Deprecated; only for migration

## PKCE Flow
```python
import secrets, hashlib, base64

# Generate PKCE
code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=')
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier).digest()
).rstrip(b'=')

# Authorization URL
url = f"{auth_server}/authorize?response_type=code&client_id={CLIENT_ID}"       f"&code_challenge={code_challenge}&code_challenge_method=S256"       f"&state={secrets.token_urlsafe()}&redirect_uri={REDIRECT}"
```

## Rules
- Always use PKCE even for confidential clients.
- Validate `state` parameter to prevent CSRF.
- Use short authorization code expiry (1-10 minutes).
- Store tokens in httpOnly, SameSite=Strict cookies.
