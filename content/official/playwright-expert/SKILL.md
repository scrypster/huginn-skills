        ---
        name: playwright-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/playwright-expert/SKILL.md
        description: Write Playwright tests: page objects, parallel runs, traces, and API testing.
        ---

        You write reliable Playwright tests.

## Page Object Model
```typescript
class LoginPage {
  constructor(private page: Page) {}

  async login(email: string, password: string) {
    await this.page.getByLabel('Email').fill(email)
    await this.page.getByLabel('Password').fill(password)
    await this.page.getByRole('button', { name: 'Login' }).click()
    await this.page.waitForURL('/dashboard')
  }
}

// Test
test('successful login', async ({ page }) => {
  const login = new LoginPage(page)
  await login.login('alice@example.com', 'password')
  await expect(page.getByText('Welcome, Alice')).toBeVisible()
})
```

## Rules
- Use `getByRole`, `getByLabel`, `getByText` — not CSS selectors.
- Use `storageState` to reuse auth across tests — avoid re-logging in.
- Capture traces on failure: `use: { trace: 'on-first-retry' }`.
- Run tests in parallel with worker processes — Playwright is designed for it.
