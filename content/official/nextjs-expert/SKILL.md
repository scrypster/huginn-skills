        ---
        name: nextjs-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/nextjs-expert/SKILL.md
        description: Build Next.js 14+ apps with App Router, Server Components, and edge functions.
        ---

        You build Next.js 14+ applications with the App Router.

## App Router Patterns
```tsx
// Server Component (default)
export default async function UserPage({ params }: { params: { id: string } }) {
  const user = await db.getUser(params.id)  // direct DB access
  if (!user) notFound()
  return <UserProfile user={user} />
}

// Client Component (explicit)
"use client"
export function LikeButton({ postId }: { postId: string }) {
  const [liked, setLiked] = useState(false)
  ...
}

// Server Action
async function createPost(formData: FormData) {
  "use server"
  const title = formData.get("title") as string
  await db.createPost({ title, userId: await getSession() })
  revalidatePath("/posts")
}
```

## Rules
- Default to Server Components — add `"use client"` only when needed.
- Use Server Actions for mutations, not API routes.
- Use `generateMetadata` for dynamic SEO, not `<Head>`.
