        ---
        name: vault-secrets-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/vault-secrets-expert/SKILL.md
        description: Manage secrets with Vault: dynamic credentials, leases, and auth methods.
        ---

        You configure HashiCorp Vault for production secrets management.

## Auth Methods
```bash
# Kubernetes auth (for pods)
vault auth enable kubernetes
vault write auth/kubernetes/config     kubernetes_host=https://$K8S_HOST

vault write auth/kubernetes/role/api     bound_service_account_names=api     bound_service_account_namespaces=production     policies=api-policy
```

## Dynamic Database Credentials
```bash
vault secrets enable database
vault write database/config/postgres     plugin_name=postgresql-database-plugin     connection_url="postgresql://{{username}}:{{password}}@db:5432/app"

vault write database/roles/api     db_name=postgres     creation_statements="CREATE ROLE ..."     default_ttl=1h
```

## Rules
- Use dynamic credentials where possible — they auto-expire.
- Audit all secret access — Vault's audit log is required in production.
- Rotate static secrets (root DB password) regularly.
- Use short-lived leases and let apps renew, not long-lived credentials.
