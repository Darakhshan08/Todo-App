#!/usr/bin/env python3
"""
FastAPI Project Generator Script
Creates a new FastAPI project with modern, production-ready structure
"""

import os
import sys
from pathlib import Path

def create_project_structure(project_name):
    """Create the basic project structure"""
    project_path = Path(project_name)

    # Create main project directory
    project_path.mkdir(exist_ok=True)

    # Create subdirectories
    (project_path / "api").mkdir(exist_ok=True)
    (project_path / "api" / "routers").mkdir(exist_ok=True)
    (project_path / "models").mkdir(exist_ok=True)
    (project_path / "schemas").mkdir(exist_ok=True)
    (project_path / "database").mkdir(exist_ok=True)
    (project_path / "core").mkdir(exist_ok=True)
    (project_path / "utils").mkdir(exist_ok=True)
    (project_path / "tests").mkdir(exist_ok=True)

    # Create main application file with modern patterns
    main_content = '''from contextlib import asynccontextmanager
from typing import AsyncGenerator
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from api.routers import items, users
from core.config import settings
from database.session import lifespan


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: Initialize resources
    print("Starting up...")
    # Here you could initialize database connections, caches, etc.
    yield
    # Shutdown: Clean up resources
    print("Shutting down...")
    # Close connections, flush logs, etc.


app = FastAPI(
    title="FastAPI Production Project",
    description="A comprehensive, production-ready FastAPI project template",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Trusted Host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

# Include routers
app.include_router(items.router, prefix="/api/v1", tags=["items"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI Production Project!"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI Production Project",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info" if settings.DEBUG else "warning"
    )
'''
    with open(project_path / "main.py", "w") as f:
        f.write(main_content)

    # Create configuration file
    config_content = '''from typing import List
from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Production Project"
    VERSION: str = "1.0.0"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = bool(int(os.getenv("DEBUG", "0")))

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./sql_app.db")
    DATABASE_POOL_SIZE: int = int(os.getenv("DATABASE_POOL_SIZE", "5"))
    DATABASE_POOL_TIMEOUT: int = int(os.getenv("DATABASE_POOL_TIMEOUT", "30"))
    DATABASE_POOL_RECYCLE: int = int(os.getenv("DATABASE_POOL_RECYCLE", "3600"))

    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",  # Example for React dev server
        "http://127.0.0.1:3000",
    ]

    # Trusted Hosts
    ALLOWED_HOSTS: List[str] = ["*"]  # In production, specify exact hosts

    model_config = {"env_file": ".env"}


settings = Settings()
'''
    with open(project_path / "core" / "config.py", "w") as f:
        f.write(config_content)

    # Create database session file
    db_session_content = '''from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from core.config import settings


# Async engine for FastAPI
async_engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=0,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_recycle=settings.DATABASE_POOL_RECYCLE,
    poolclass=QueuePool,
    echo=settings.DEBUG,  # Only enable SQL logging in debug mode
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@asynccontextmanager
async def lifespan() -> AsyncGenerator[None, None]:
    """Database lifespan context manager."""
    # Startup: Initialize database connections
    print("Initializing database connections...")
    yield
    # Shutdown: Clean up database connections
    print("Closing database connections...")
    await async_engine.dispose()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Async dependency to get database session.

    Usage in FastAPI endpoints:
    async def my_endpoint(db: AsyncSession = Depends(get_db)):
        # work with db
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
'''
    with open(project_path / "database" / "session.py", "w") as f:
        f.write(db_session_content)

    # Create requirements file with updated packages
    requirements_content = '''fastapi==0.115.0
uvicorn[standard]==0.32.0
pydantic==2.10.0
pydantic-settings==2.6.1
sqlalchemy==2.0.36
asyncpg==0.30.0  # PostgreSQL async driver
aiosqlite==0.20.0  # SQLite async driver
alembic==1.13.3  # Database migrations
python-multipart==0.0.20
passlib[bcrypt]==1.7.4
python-jose[cryptography]==3.3.0
python-dotenv==1.0.1
pytest==8.3.3
httpx==0.27.2
pytest-asyncio==0.24.0
'''
    with open(project_path / "requirements.txt", "w") as f:
        f.write(requirements_content)

    # Create .env file
    env_content = '''# Application Settings
DEBUG=1
HOST=0.0.0.0
PORT=8000

# Security
SECRET_KEY=super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=sqlite+aiosqlite:///./sql_app.db
DATABASE_POOL_SIZE=5
DATABASE_POOL_TIMEOUT=30
DATABASE_POOL_RECYCLE=3600

# CORS
ALLOWED_ORIGINS=http://localhost,http://localhost:3000,http://127.0.0.1:3000
ALLOWED_HOSTS=*

# Logging
LOG_LEVEL=info
'''
    with open(project_path / ".env", "w") as f:
        f.write(env_content)

    # Create basic router files
    items_router_content = '''from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.item import Item, ItemCreate, ItemUpdate
from database.session import get_db
from models.item import Item as ItemModel

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[Item])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    items = await ItemModel.get_multi(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await ItemModel.get(db, item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return item

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = await ItemModel.create(db, obj_in=item)
    return db_item

@router.put("/{item_id}", response_model=Item)
async def update_item(
    item_id: int,
    item: ItemUpdate,
    db: AsyncSession = Depends(get_db)
):
    db_item = await ItemModel.get(db, item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    updated_item = await ItemModel.update(db, db_obj=db_item, obj_in=item)
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await ItemModel.get(db, item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    await ItemModel.remove(db, id=item_id)
'''
    with open(project_path / "api" / "routers" / "items.py", "w") as f:
        f.write(items_router_content)

    # Create a basic model file
    model_content = '''from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

from database.base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

    @classmethod
    async def get_multi(
        cls,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100
    ) -> List["Item"]:
        """Get multiple items with pagination."""
        result = await db.execute(
            select(cls).offset(skip).limit(limit)
        )
        return result.scalars().all()

    @classmethod
    async def get(cls, db: AsyncSession, id: int) -> Optional["Item"]:
        """Get an item by ID."""
        result = await db.execute(select(cls).where(cls.id == id))
        return result.scalar_one_or_none()

    @classmethod
    async def create(cls, db: AsyncSession, obj_in) -> "Item":
        """Create a new item."""
        db_obj = cls(**obj_in.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @classmethod
    async def update(
        cls,
        db: AsyncSession,
        db_obj: "Item",
        obj_in
    ) -> "Item":
        """Update an existing item."""
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @classmethod
    async def remove(cls, db: AsyncSession, id: int) -> bool:
        """Remove an item by ID."""
        obj = await cls.get(db, id)
        if obj:
            await db.delete(obj)
            await db.commit()
            return True
        return False
'''
    with open(project_path / "models" / "item.py", "w") as f:
        f.write(model_content)

    # Create a basic schema file
    schema_content = '''from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
'''
    with open(project_path / "schemas" / "item.py", "w") as f:
        f.write(schema_content)

    # Create basic test file
    test_content = '''import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_create_item():
    # This would require a more complex setup with database mocking
    # For now, just a placeholder test
    pass
'''
    with open(project_path / "tests" / "test_main.py", "w") as f:
        f.write(test_content)

    print(f"FastAPI project '{project_name}' has been created successfully!")
    print("\nProject structure:")
    print(f"├── {project_name}/")
    print("    ├── main.py                 # Main application entry point")
    print("    ├── requirements.txt        # Project dependencies")
    print("    ├── .env                   # Environment variables")
    print("    ├── api/")
    print("    │   └── routers/")
    print("    │       └── items.py       # API route handlers")
    print("    ├── models/                # Database models")
    print("    │   └── item.py           # Example model")
    print("    ├── schemas/               # Pydantic schemas")
    print("    │   └── item.py           # Example schemas")
    print("    ├── core/")
    print("    │   └── config.py         # Application configuration")
    print("    ├── database/")
    print("    │   └── session.py        # Database session management")
    print("    └── tests/                 # Test files")
    print("        └── test_main.py      # Example tests")
    print("\nTo get started:")
    print(f"1. cd {project_name}")
    print("2. pip install -r requirements.txt")
    print("3. uvicorn main:app --reload")


def main():
    if len(sys.argv) != 2:
        print("Usage: python create_fastapi_project.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_project_structure(project_name)

if __name__ == "__main__":
    main()