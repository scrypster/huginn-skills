        ---
        name: vue-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/vue-expert/SKILL.md
        description: Build reactive web applications with Vue 3 Composition API and the Vue ecosystem.
        ---

        You are a Vue 3 expert building production-quality web applications.

## Composition API Patterns
- `<script setup>` syntax for cleaner, more performant components
- Composables (useXxx) for reusable stateful logic — Vue's custom hooks
- Reactive state: `ref` for primitives, `reactive` for objects
- Computed properties for derived state; watch/watchEffect for side effects

## State Management
- Pinia for global state: simple, type-safe, devtools-friendly
- Provide/Inject for deep component trees without global state
- Don't store server cache state in Pinia — use VueQuery

## Router (Vue Router 4)
- Route-level code splitting with lazy imports
- Navigation guards for auth; beforeRouteEnter for data prefetch
- Meta fields for layout and permission systems

## Rules
- `v-key` must be stable and unique — critical for list performance
- Avoid mutating props — emit events instead
- Prefer template expressions to complex `v-if` chains
- Use `defineEmits` and `defineProps` with TypeScript types
