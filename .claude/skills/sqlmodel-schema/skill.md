---
name: sqlmodel-schema
title: SQLModel Schema Design
version: 1.0.0
category: Database
tags: [database, sql, orm, schema, fastapi, python]
author: Claude Code
description: Comprehensive SQLModel schema design skill for building production-ready database models that integrate seamlessly with FastAPI
---

# SQLModel Schema Design Skill

This skill provides comprehensive guidance for designing database schemas using SQLModel, combining the best of SQLAlchemy and Pydantic. It covers everything from basic model definitions to advanced relationships and production patterns that integrate seamlessly with FastAPI.

## Table of Contents
1. [Basic Model Definition](#basic-model-definition)
2. [Field Types and Validation](#field-types-and-validation)
3. [Relationships](#relationships)
4. [CRUD Operations](#crud-operations)
5. [Advanced Relationships](#advanced-relationships)
6. [Indexes and Constraints](#indexes-and-constraints)
7. [Integration with FastAPI](#integration-with-fastapi)
8. [Async Operations](#async-operations)
9. [Production Patterns](#production-patterns)

## Basic Model Definition

### Simple Model with Primary Key
```python
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True, index=True)
    age: Optional[int] = Field(default=None, ge=0, le=150)
```

### Model with Validation
```python
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import validator

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=100, index=True)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(gt=0)
    stock_quantity: int = Field(ge=0)
    is_active: bool = Field(default=True)
```

## Field Types and Validation

### Common Field Types
```python
from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
import uuid

class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: uuid.UUID = Field(default_factory=uuid.uuid4, unique=True)

    # Text fields
    title: str = Field(min_length=1, max_length=200, index=True)
    content: str = Field(sa_column_kwargs={"server_default": ""})
    slug: str = Field(regex=r"^[a-z0-9-]+$")  # URL-friendly

    # Numeric fields
    views: int = Field(default=0, ge=0)
    rating: float = Field(default=0.0, ge=0.0, le=5.0)

    # Date/time fields
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Boolean field
    is_published: bool = Field(default=False)
```

### Field Constraints and Indexes
```python
from sqlmodel import SQLModel, Field
from typing import Optional

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Unique constraint
    order_number: str = Field(unique=True, index=True)

    # Indexed for faster queries
    customer_id: int = Field(index=True)

    # Foreign key (defined separately)
    status: str = Field(default="pending", sa_column_kwargs={
        "server_default": "pending"
    })

    # Decimal with precision
    total_amount: float = Field(gt=0)

    # Indexed for filtering
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
```

## Relationships

### One-to-Many Relationship
```python
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    # One-to-many: Team has many Heroes
    heroes: List["Hero"] = Relationship(back_populates="team")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    # Foreign key to Team
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

    # Many-to-one: Hero belongs to one Team
    team: Optional[Team] = Relationship(back_populates="heroes")
```

### Self-Referencing Relationship
```python
class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None

    # Self-referencing: Category can have a parent category
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")
    parent: Optional["Category"] = Relationship(back_populates="children",
                                             sa_relationship_kwargs={"remote_side": "Category.id"})
    children: List["Category"] = Relationship(back_populates="parent")
```

## CRUD Operations

### Basic CRUD Endpoints
```python
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional, List

# Define models
class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class HeroCreate(HeroBase):
    pass

class HeroPublic(HeroBase):
    id: int

class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None

# Database setup
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# CRUD endpoints
@app.post("/heroes/", response_model=HeroPublic)
def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

@app.get("/heroes/", response_model=List[HeroPublic])
def read_heroes(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

@app.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@app.patch("/heroes/{hero_id}", response_model=HeroPublic)
def update_hero(
    *,
    session: Session = Depends(get_session),
    hero_id: int,
    hero: HeroUpdate
):
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    db_hero.sqlmodel_update(hero_data)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

@app.delete("/heroes/{hero_id}")
def delete_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
```

## Advanced Relationships

### Many-to-Many Relationship with Link Table
```python
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: Optional[int] = Field(default=None, foreign_key="hero.id", primary_key=True)
    is_training: bool = False  # Extra field in the relationship

    team: "Team" = Relationship(back_populates="hero_links")
    hero: "Hero" = Relationship(back_populates="team_links")

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    hero_links: List[HeroTeamLink] = Relationship(back_populates="team")
    # Access heroes through the link table
    heroes: List["Hero"] = Relationship(
        back_populates="teams",
        link_model=HeroTeamLink
    )

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_links: List[HeroTeamLink] = Relationship(back_populates="hero")
    # Access teams through the link table
    teams: List["Team"] = Relationship(
        back_populates="heroes",
        link_model=HeroTeamLink
    )
```

### Relationship with Cascade Delete
```python
from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    # Cascade delete: when category is deleted, all products are deleted too
    products: List["Product"] = Relationship(
        back_populates="category",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    category_id: Optional[int] = Field(default=None, foreign_key="category.id", ondelete="CASCADE")
    category: Optional[Category] = Relationship(back_populates="products")
```

## Indexes and Constraints

### Advanced Indexing and Constraints
```python
from sqlmodel import SQLModel, Field, create_engine
from sqlalchemy import UniqueConstraint, CheckConstraint
from typing import Optional

class User(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("email", "username", name="uq_user_email_username"),
        CheckConstraint("age >= 13", name="ck_user_age_min"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, min_length=3, max_length=50)
    email: str = Field(index=True, unique=True)
    age: int = Field(ge=13, le=120)

    # Composite index
    first_name: str = Field(sa_column_kwargs={"index": True})
    last_name: str = Field(sa_column_kwargs={"index": True})

    # Full-text search index (PostgreSQL)
    bio: Optional[str] = Field(
        sa_column_kwargs={
            "server_default": "",
            "comment": "Full text search column"
        }
    )
```

## Integration with FastAPI

### Complete FastAPI Integration Example
```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator, List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession as SQLAlchemyAsyncSession

# Models with different layers
class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str

class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    heroes: List["Hero"] = Relationship(back_populates="team")

class TeamCreate(TeamBase):
    pass

class TeamPublic(TeamBase):
    id: int

class TeamUpdate(SQLModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    team: Optional[Team] = Relationship(back_populates="heroes")

class HeroCreate(HeroBase):
    pass

class HeroPublic(HeroBase):
    id: int

class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None

# Database setup
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# Session dependency
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session

# Lifespan for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# API endpoints
@app.post("/heroes/", response_model=HeroPublic)
async def create_hero(
    *,
    session: AsyncSession = Depends(get_async_session),
    hero: HeroCreate
):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    await session.commit()
    await session.refresh(db_hero)
    return db_hero

@app.get("/heroes/", response_model=List[HeroPublic])
async def read_heroes(
    *,
    session: AsyncSession = Depends(get_async_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    heroes = await session.exec(select(Hero).offset(offset).limit(limit))
    return heroes.all()

@app.get("/heroes/{hero_id}", response_model=HeroPublic)
async def read_hero(
    *,
    session: AsyncSession = Depends(get_async_session),
    hero_id: int
):
    hero = await session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero
```

## Async Operations

### Async Session Management
```python
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from contextlib import asynccontextmanager
from typing import AsyncGenerator

class DatabaseManager:
    def __init__(self, database_url: str):
        self.engine: AsyncEngine = create_async_engine(database_url)

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with AsyncSession(self.engine) as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

# Usage in FastAPI
db_manager = DatabaseManager("sqlite+aiosqlite:///./test.db")

async def get_db_session():
    async with db_manager.get_session() as session:
        yield session
```

### Async Queries
```python
from sqlmodel import select
from sqlalchemy import func

# Async count query
async def count_heroes(session: AsyncSession) -> int:
    statement = select(func.count()).select_from(Hero)
    result = await session.exec(statement)
    return result.one()

# Async filtered query
async def get_heroes_by_team(session: AsyncSession, team_id: int) -> List[Hero]:
    statement = select(Hero).where(Hero.team_id == team_id)
    result = await session.exec(statement)
    return result.all()

# Async join query
async def get_heroes_with_teams(session: AsyncSession) -> List[Hero]:
    statement = select(Hero).join(Team).where(Team.name.contains("Avengers"))
    result = await session.exec(statement)
    return result.all()
```

## Production Patterns

### Repository Pattern
```python
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T', bound=SQLModel)

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def create(self, session: AsyncSession, obj: T) -> T:
        pass

    @abstractmethod
    async def get_by_id(self, session: AsyncSession, id: int) -> Optional[T]:
        pass

    @abstractmethod
    async def get_all(self, session: AsyncSession, skip: int = 0, limit: int = 100) -> List[T]:
        pass

    @abstractmethod
    async def update(self, session: AsyncSession, id: int, obj: T) -> Optional[T]:
        pass

    @abstractmethod
    async def delete(self, session: AsyncSession, id: int) -> bool:
        pass

class HeroRepository(BaseRepository[Hero]):
    async def create(self, session: AsyncSession, hero: Hero) -> Hero:
        session.add(hero)
        await session.commit()
        await session.refresh(hero)
        return hero

    async def get_by_id(self, session: AsyncSession, id: int) -> Optional[Hero]:
        return await session.get(Hero, id)

    async def get_all(self, session: AsyncSession, skip: int = 0, limit: int = 100) -> List[Hero]:
        statement = select(Hero).offset(skip).limit(limit)
        result = await session.exec(statement)
        return result.all()

    async def update(self, session: AsyncSession, id: int, hero_update: HeroUpdate) -> Optional[Hero]:
        hero = await session.get(Hero, id)
        if hero:
            hero_data = hero_update.model_dump(exclude_unset=True)
            hero.sqlmodel_update(hero_data)
            await session.commit()
            await session.refresh(hero)
        return hero

    async def delete(self, session: AsyncSession, id: int) -> bool:
        hero = await session.get(Hero, id)
        if hero:
            await session.delete(hero)
            await session.commit()
            return True
        return False
```

### Service Layer Pattern
```python
class HeroService:
    def __init__(self, repository: HeroRepository):
        self.repository = repository

    async def create_hero(self, session: AsyncSession, hero_create: HeroCreate) -> HeroPublic:
        # Business logic validation
        if hero_create.age is not None and hero_create.age < 0:
            raise ValueError("Age cannot be negative")

        hero = Hero.model_validate(hero_create)
        created_hero = await self.repository.create(session, hero)
        return HeroPublic.model_validate(created_hero)

    async def get_hero_by_id(self, session: AsyncSession, hero_id: int) -> Optional[HeroPublic]:
        hero = await self.repository.get_by_id(session, hero_id)
        if hero:
            return HeroPublic.model_validate(hero)
        return None

    async def assign_hero_to_team(self, session: AsyncSession, hero_id: int, team_id: int) -> HeroPublic:
        hero = await self.repository.get_by_id(session, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")

        team = await session.get(Team, team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")

        hero.team_id = team_id
        await session.commit()
        await session.refresh(hero)

        return HeroPublic.model_validate(hero)
```

This skill provides a comprehensive foundation for designing SQLModel schemas that integrate seamlessly with FastAPI, from basic models to advanced production patterns.