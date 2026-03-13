        ---
        name: ruby-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/ruby-expert/SKILL.md
        description: Write idiomatic Ruby: blocks, procs, modules, and meaningful DSLs.
        ---

        You write idiomatic, clean Ruby.

## Ruby Patterns
```ruby
# Enumerable
active_users = users.select(&:active?).map(&:name).sort

# Keyword arguments
def create_user(name:, email:, role: :member)
  User.new(name:, email:, role:)
end

# Modules for composition
module Auditable
  def self.included(base)
    base.before_save :record_change
  end

  private
  def record_change
    AuditLog.create!(record: self, user: Current.user)
  end
end

class Post < ApplicationRecord
  include Auditable
end
```

## Rules
- Use `attr_reader` / `attr_accessor` instead of explicit getters.
- Prefer `map`, `select`, `reject`, `reduce` over manual loops.
- Raise specific exception classes — not bare `raise "error"`.
