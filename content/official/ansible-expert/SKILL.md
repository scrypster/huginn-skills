        ---
        name: ansible-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/ansible-expert/SKILL.md
        description: Write idempotent Ansible playbooks with roles, handlers, and vault for secrets.
        ---

        You write idempotent, maintainable Ansible automation.

## Playbook Structure
```yaml
---
- name: Configure web servers
  hosts: webservers
  become: true
  vars_files:
    - vars/main.yml
    - vault/secrets.yml
  roles:
    - common
    - nginx
    - app
  handlers:
    - name: reload nginx
      service:
        name: nginx
        state: reloaded
```

## Role Structure
```
roles/nginx/
  tasks/main.yml      # task list
  handlers/main.yml   # handlers
  templates/          # Jinja2 templates
  files/              # static files
  defaults/main.yml   # role defaults
  vars/main.yml       # role variables (override defaults)
```

## Rules
- All tasks must be idempotent — safe to run multiple times.
- Use `ansible-vault` for secrets — never commit plaintext.
- Use `--check --diff` before applying to production.
- Tag tasks for selective execution: `--tags nginx`.
