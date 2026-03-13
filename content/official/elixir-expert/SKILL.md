        ---
        name: elixir-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/elixir-expert/SKILL.md
        description: Write idiomatic Elixir: pattern matching, GenServer, pipelines, and LiveView.
        ---

        You write idiomatic Elixir and Phoenix applications.

## Elixir Patterns
```elixir
# Pattern matching + pipe
def process_order(%Order{status: :pending} = order) do
  order
  |> validate()
  |> charge_payment()
  |> fulfill()
  |> notify_user()
end

def process_order(%Order{status: status}),
  do: {:error, "Cannot process order in #{status} state"}

# GenServer
defmodule Counter do
  use GenServer

  def start_link(init), do: GenServer.start_link(__MODULE__, init, name: __MODULE__)
  def increment(), do: GenServer.cast(__MODULE__, :increment)

  def handle_cast(:increment, count), do: {:noreply, count + 1}
end
```

## Rules
- Pattern match on function heads instead of if/case where possible.
- Use `with` for multi-step happy paths with early error returns.
- Supervise all long-lived processes — let it crash, but supervise the crash.
