        ---
        name: nginx-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/nginx-expert/SKILL.md
        description: Configure Nginx: reverse proxy, TLS termination, rate limiting, and caching.
        ---

        You configure production Nginx deployments.

## Reverse Proxy Config
```nginx
upstream api {
    least_conn;
    server api1:8080;
    server api2:8080;
    keepalive 32;
}

server {
    listen 443 ssl http2;
    server_name api.example.com;

    ssl_certificate     /etc/ssl/certs/api.crt;
    ssl_certificate_key /etc/ssl/private/api.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:...;

    location /api/ {
        proxy_pass http://api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 5s;
        proxy_read_timeout 60s;
    }

    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    limit_req zone=api burst=20 nodelay;
}
```

## Rules
- Always set `proxy_read_timeout` — default is 60s which may be too long.
- Use `least_conn` for long-lived connections; `round_robin` for short ones.
- GZIP compress all text responses; not binary.
