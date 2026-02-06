from contextlib import contextmanager, asynccontextmanager
from typing import AsyncGenerator, Generator

from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.pool import QueuePool
import os


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
    DATABASE_POOL_SIZE: int = int(os.getenv("DATABASE_POOL_SIZE", "5"))
    DATABASE_POOL_TIMEOUT: int = int(os.getenv("DATABASE_POOL_TIMEOUT", "30"))
    DATABASE_POOL_RECYCLE: int = int(os.getenv("DATABASE_POOL_RECYCLE", "3600"))

    model_config = {"env_file": ".env"}


settings = Settings()


# For async operations (recommended for FastAPI)
async_engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Verify connections before use
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=0,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_recycle=settings.DATABASE_POOL_RECYCLE,
    poolclass=QueuePool,
    echo=False,  # Set to True for SQL debugging in development
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# For sync operations (when needed)
sync_engine = create_engine(
    settings.DATABASE_URL.replace("+aiosqlite", ""),
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=0,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_recycle=settings.DATABASE_POOL_RECYCLE,
    poolclass=QueuePool,
    echo=False,
)

# Sync session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


# Create base class for models
class Base(DeclarativeBase):
    metadata = MetaData()


@asynccontextmanager
async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Async dependency to get database session.

    Usage in FastAPI endpoints:
    async def my_endpoint(db: AsyncSession = Depends(get_async_db)):
        # work with db
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@contextmanager
def get_sync_db() -> Generator:
    """
    Sync dependency to get database session.

    Usage in FastAPI endpoints:
    def my_endpoint(db: Session = Depends(get_sync_db)):
        # work with db
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Example model
class Item(Base):
    __tablename__ = "items"

    # id will be added by SQLAlchemy when Base.metadata.create_all() is called
    # Define columns here in actual implementation
    # Example:
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String, index=True, nullable=False)
    # description = Column(String, nullable=True)
    # price = Column(Float, nullable=False)
    # created_at = Column(DateTime, default=datetime.utcnow)