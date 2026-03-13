        ---
        name: angular-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/angular-expert/SKILL.md
        description: Build Angular applications with signals, standalone components, and RxJS patterns.
        ---

        You build modern Angular applications.

## Signal Patterns (Angular 17+)
```typescript
@Component({
  standalone: true,
  template: `
    <div>{{ user().name }}</div>
    <button (click)="reload()">Reload</button>
  `
})
export class UserComponent {
  private userService = inject(UserService)
  user = toSignal(this.userService.getUser$(), { requireSync: true })

  // Computed signal
  greeting = computed(() => `Hello, ${this.user().name}!`)
}
```

## Rules
- Prefer `inject()` over constructor injection for new code.
- Use signals for local state; services for shared state.
- Use `async` pipe or `toSignal` — never manually `subscribe` in components.
- Standalone components reduce bundle size — prefer over NgModules.
