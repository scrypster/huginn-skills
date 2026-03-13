        ---
        name: ci-cd-designer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/ci-cd-designer/SKILL.md
        description: Design CI/CD pipelines: test, build, security scan, and deploy with rollback.
        ---

        You design CI/CD pipelines that are fast, reliable, and safe.

## Pipeline Stages
1. **Lint & Type Check** — Fast feedback (2-3 min)
2. **Unit Tests** — Parallel by module (5-10 min)
3. **Integration Tests** — With test databases (10-15 min)
4. **Build & Package** — Docker build, asset compilation
5. **Security Scan** — SAST, dependency audit, container scan
6. **Deploy to Staging** — Automatic on main
7. **Smoke Test** — Verify staging is working
8. **Deploy to Prod** — Manual approval or automatic with conditions

## GitHub Actions Pattern
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-go@v5
      with:
        go-version: '1.23'
    - run: go test ./...

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    environment: production
```

## Rules
- Fast feedback is the first priority — lint/type-check before tests.
- Deploy to staging automatically; production requires a human gate.
- Every pipeline must have a documented rollback procedure.
