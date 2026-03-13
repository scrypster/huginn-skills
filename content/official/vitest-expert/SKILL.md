        ---
        name: vitest-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/vitest-expert/SKILL.md
        description: Write Vitest tests: mocking, snapshot testing, and browser mode.
        ---

        You write efficient Vitest test suites.

## Vitest Patterns
```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { createPinia, setActivePinia } from 'pinia'

// Mocking
vi.mock('../api/users', () => ({
  fetchUser: vi.fn().mockResolvedValue({ id: 1, name: 'Alice' })
}))

// Store testing
describe('userStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('loads user on mount', async () => {
    const store = useUserStore()
    await store.load(1)
    expect(store.user?.name).toBe('Alice')
  })
})
```

## Rules
- Prefer `vi.mock()` over Jest's `jest.mock()` — same API, Vite-native.
- Use `vi.spyOn` to verify calls while keeping original implementation.
- `describe.concurrent` for independent suites — runs in parallel.
- Browser mode for testing DOM-dependent code without jsdom limitations.
