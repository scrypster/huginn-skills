        ---
        name: docker-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/docker-expert/SKILL.md
        description: Write optimized Dockerfiles: layer caching, multi-stage builds, and security.
        ---

        You write optimized, secure Dockerfiles.

## Multi-Stage Build Pattern
```dockerfile
# Build stage
FROM golang:1.23-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o server .

# Run stage (minimal)
FROM gcr.io/distroless/static-debian12
WORKDIR /app
COPY --from=builder /app/server .
EXPOSE 8080
USER nonroot:nonroot
ENTRYPOINT ["./server"]
```

## Layer Caching Rules
- Copy dependency files first, then install, then copy source
- Don't invalidate cache with `COPY . .` before `RUN npm install`
- Use `.dockerignore` to exclude node_modules, .git, etc.

## Security Rules
- Never run as root — use `USER nonroot` or named user
- Use distroless or minimal base images
- Never bake secrets into images — use secrets at runtime
