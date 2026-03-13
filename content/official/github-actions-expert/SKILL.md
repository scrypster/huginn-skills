        ---
        name: github-actions-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/github-actions-expert/SKILL.md
        description: Write efficient GitHub Actions workflows: caching, matrices, and reusable workflows.
        ---

        You write efficient, maintainable GitHub Actions workflows.

## Workflow Best Practices
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [20, 22]
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node }}
        cache: npm
    - run: npm ci
    - run: npm test

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    environment: production
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Deploy
      env:
        API_KEY: ${{ secrets.DEPLOY_API_KEY }}
      run: ./deploy.sh
```

## Rules
- Pin action versions to commit SHA for supply chain security.
- Use `needs` to enforce test → deploy ordering.
- Cache dependencies with `cache:` input, not manual `actions/cache`.
- Use `environment:` for production deployments — enables protection rules.
