        ---
        name: definition-of-done
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/definition-of-done/SKILL.md
        description: Create team-specific Definitions of Done that prevent scope creep and ensure quality.
        ---

        You help teams create clear, enforceable Definitions of Done.

## DoD Template
```markdown
## Definition of Done

A user story / feature is DONE when:

### Code Quality
- [ ] Code reviewed and approved by ≥1 peer
- [ ] No new linting errors or warnings
- [ ] All tests pass (unit + integration)
- [ ] Test coverage ≥ <threshold>%

### Functionality
- [ ] Acceptance criteria met (all scenarios pass)
- [ ] Edge cases handled
- [ ] Error states handled gracefully

### Documentation
- [ ] API changes documented
- [ ] README updated if needed

### Deployment
- [ ] Deployed to staging
- [ ] Smoke test passing in staging
```

## Rules
- Every checklist item must be verifiable — not "good code" but "passes linter."
- Include environment-specific criteria (staging deploy, feature flag, etc.)
- Review DoD with the team — buy-in matters more than completeness.
