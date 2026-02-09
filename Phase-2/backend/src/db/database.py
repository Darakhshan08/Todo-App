"""
Database connection and session management for Neon PostgreSQL
"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlmodel import SQLModel
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database URL from environment
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://user:password@localhost:5432/tododb"
)

# Remove unsupported query parameters for asyncpg
# asyncpg doesn't support sslmode and channel_binding in URL
if "sslmode=" in DATABASE_URL or "channel_binding=" in DATABASE_URL:
    # Split URL and query string
    if "?" in DATABASE_URL:
        base_url, query = DATABASE_URL.split("?", 1)
        # Remove sslmode and channel_binding from query params
        params = [p for p in query.split("&") if not p.startswith(("sslmode=", "channel_binding="))]
        DATABASE_URL = base_url + ("?" + "&".join(params) if params else "")

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    future=True,
    pool_size=5,
    max_overflow=10,
    connect_args={"ssl": "require"} if "neon.tech" in DATABASE_URL else {},
)

# Create async session factory
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Base class for all database models"""
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get database session.

    Usage:
        @app.get("/items/")
        async def read_items(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db() -> None:
    """Initialize database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def close_db() -> None:
    """Close database connection"""
    await engine.dispose()
