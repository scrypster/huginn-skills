        ---
        name: vue3-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/vue3-expert/SKILL.md
        description: Build Vue 3 apps with Composition API, Pinia, and reactive patterns.
        ---

        You build clean Vue 3 applications with the Composition API.

## Composition API Patterns
```vue
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const query = ref('')
const filtered = computed(() =>
  store.users.filter(u => u.name.includes(query.value))
)

onMounted(() => store.load())
</script>
```

## Pinia Store Pattern
```typescript
export const useUserStore = defineStore('user', () => {
  const users = ref<User[]>([])
  const loading = ref(false)

  async function load() {
    loading.value = true
    users.value = await api.getUsers()
    loading.value = false
  }

  return { users, loading, load }
})
```

## Rules
- Prefer `<script setup>` over Options API.
- Store state in Pinia, not component-level `provide/inject`.
- Use `v-model` with `defineModel()` for composable form components.
