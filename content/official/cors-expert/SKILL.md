        ---
        name: cors-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/cors-expert/SKILL.md
        description: Configure CORS correctly: origins, methods, credentials, and preflight handling.
        ---

        You configure CORS correctly and securely.

## CORS Configuration
```python
# Strict production config
CORS_ORIGINS = ["https://app.mysite.com"]
CORS_METHODS = ["GET", "POST", "PUT", "DELETE"]
CORS_HEADERS = ["Content-Type", "Authorization"]
CORS_ALLOW_CREDENTIALS = True  # only with specific origins, never wildcard

# Never in production:
# Access-Control-Allow-Origin: *  with Access-Control-Allow-Credentials: true
```

## Preflight Request Handling
```
OPTIONS /api/users HTTP/1.1
Origin: https://app.mysite.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization

→ 204 No Content
Access-Control-Allow-Origin: https://app.mysite.com
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Authorization
Access-Control-Max-Age: 86400
```

## Rules
- Never use `*` with credentials — browsers will reject it anyway.
- Cache preflight with `Access-Control-Max-Age` to reduce OPTIONS requests.
- Validate `Origin` header server-side — don't rely on browser enforcement alone.
