        ---
        name: svelte-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/svelte-expert/SKILL.md
        description: Build Svelte/SvelteKit applications with runes, stores, and server-side loading.
        ---

        You build clean Svelte and SvelteKit applications.

## SvelteKit Patterns
```svelte
<!-- +page.server.ts -->
export async function load({ params }) {
  const user = await db.getUser(params.id)
  if (!user) error(404, 'User not found')
  return { user }
}

<!-- +page.svelte (Svelte 5 runes) -->
<script lang="ts">
  let { data } = $props()
  let count = $state(0)
  let doubled = $derived(count * 2)
</script>

<h1>{data.user.name}</h1>
<p>{count} × 2 = {doubled}</p>
<button onclick={() => count++}>+</button>
```

## Rules
- Use `$props()`, `$state()`, `$derived()` runes in Svelte 5.
- `+page.server.ts` for data fetching and form actions — not client-side API calls.
- Svelte stores for cross-component state, props for parent-child.
