        ---
        name: react-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/react-expert/SKILL.md
        description: Build React components with hooks, memoization, and clean composition patterns.
        ---

        You build clean, performant React components.

## Hooks Patterns
```tsx
// Custom hook for data fetching
function useUser(id: string) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    fetchUser(id).then(u => {
      if (!cancelled) setUser(u)
      setLoading(false)
    })
    return () => { cancelled = true }
  }, [id])

  return { user, loading }
}
```

## Optimization Rules
- `useMemo` for expensive computations, not for object identity.
- `useCallback` for stable function references passed to memo'd children.
- `React.memo` for components that receive same props often.

## Rules
- Co-locate state with the component that owns it.
- Effects are for synchronization — not lifecycle management.
- Never derive state from props — compute it from canonical state.
