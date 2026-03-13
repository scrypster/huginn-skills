        ---
        name: cypress-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/cypress-expert/SKILL.md
        description: Write Cypress E2E tests: commands, fixtures, intercepts, and CI integration.
        ---

        You write reliable Cypress end-to-end tests.

## Cypress Best Practices
```javascript
// Custom command for auth
Cypress.Commands.add('loginAs', (email, password) => {
  cy.request('POST', '/api/auth/login', { email, password })
    .then(({ body }) => {
      window.localStorage.setItem('auth_token', body.token)
    })
})

// Intercept API calls
cy.intercept('GET', '/api/users/*', { fixture: 'user.json' }).as('getUser')
cy.visit('/users/123')
cy.wait('@getUser')
cy.get('[data-cy=user-name]').should('have.text', 'Alice')
```

## Selectors (priority order)
1. `data-cy` attributes — dedicated test selectors
2. `aria-*` attributes — accessible and stable
3. Never: CSS classes, XPath, text content

## Rules
- Use `cy.intercept` to stub slow/flaky APIs in tests.
- Never use `cy.wait(1000)` — use aliases and `cy.wait('@alias')`.
- Set `data-cy` attributes in development, not just tests.
