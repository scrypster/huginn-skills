        ---
        name: nuxtjs-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/nuxtjs-expert/SKILL.md
        description: Build Nuxt 3 apps with composables, server routes, and auto-imports.
        ---

        You build well-structured Nuxt 3 applications.

## Nuxt 3 Patterns
```vue
<!-- pages/users/[id].vue -->
<script setup lang="ts">
const route = useRoute()
const { data: user, error } = await useFetch(`/api/users/${route.params.id}`)
if (!user.value) throw createError({ statusCode: 404 })
</script>

<!-- server/api/users/[id].get.ts -->
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  return db.getUser(id)
})
```

## Rules
- Server routes in `server/api/` — never expose direct DB access to client.
- Use `useFetch` with `lazy: true` for non-critical data.
- `useState` for shared client state, not Pinia for simple cases.
- Auto-imports work for `composables/` and `utils/` — no need to import them.
