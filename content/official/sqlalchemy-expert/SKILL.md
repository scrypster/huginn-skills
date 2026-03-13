        ---
        name: sqlalchemy-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/sqlalchemy-expert/SKILL.md
        description: Use SQLAlchemy 2.0 with async sessions, relationships, and efficient query patterns.
        ---

        You use SQLAlchemy 2.0 correctly with async and type safety.

## SQLAlchemy 2.0 Patterns
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

# Query pattern
async def get_user(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```

## Rules
- Use `mapped_column` with type annotations (ORM 2.0 style).
- Use `selectinload` for collections, `joinedload` for single relationships.
- Never use `Session.execute(raw_sql)` — use ORM or `text()` with parameters.
