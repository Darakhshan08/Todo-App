---
name: fastapi-framework
title: FastAPI Framework Development
version: 2.0.0
category: Web Development
tags: [web, api, python, fastapi, async]
author: Claude Code
description: Comprehensive FastAPI development skill covering everything from hello world to production APIs with modern async patterns
---

# FastAPI Framework Development Skill (Version 2.0)

This skill provides comprehensive guidance for building modern, production-ready applications with FastAPI, incorporating async patterns, security best practices, and scalable architecture.

## Table of Contents
1. [Hello World Application](#hello-world-application)
2. [Routing](#routing)
3. [Path and Query Parameters](#path-and-query-parameters)
4. [Request and Response Models](#request-and-response-models)
5. [Dependency Injection](#dependency-injection)
6. [Middleware](#middleware)
7. [Testing](#testing)
8. [Async/Await Patterns](#asyncawait-patterns)
9. [APIRouter Organization](#apirouter-organization)
10. [Error Handling](#error-handling)
11. [Production Deployment](#production-deployment)
12. [Environment Configuration](#environment-configuration)
13. [Security Best Practices](#security-best-practices)

## Hello World Application

### Basic Setup with Modern Patterns
```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
import uvicorn


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
    title="FastAPI Production Template",
    description="A comprehensive, production-ready template for FastAPI projects",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",  # Enable interactive API documentation
    redoc_url="/redoc",  # Enable ReDoc documentation
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI Production Template!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

### Running the Application
```bash
pip install "fastapi[all]"
uvicorn main:app --reload
```

## Routing

FastAPI supports all standard HTTP methods with automatic validation, documentation, and async support.

### GET Routes with Documentation
```python
from fastapi import FastAPI, status
from typing import Optional

app = FastAPI()

@app.get("/",
         response_model=dict,
         summary="Health check endpoint",
         description="Basic health check to confirm API is running")
async def read_root() -> dict:
    """
    Basic health check endpoint.

    Returns a welcome message to confirm the API is running.
    """
    return {"message": "Hello World"}

@app.get("/users/{user_id}",
         summary="Get user by ID",
         description="Retrieve a specific user by their unique identifier")
async def get_user(
    user_id: int,
    include_posts: bool = False
) -> dict:
    """
    Get a user by their ID.

    Args:
        user_id: The unique identifier of the user to retrieve
        include_posts: Whether to include user's posts in the response

    Returns:
        User information with optional posts
    """
    return {"user_id": user_id, "include_posts": include_posts}
```

### POST Routes with Validation
```python
from pydantic import BaseModel, Field
from typing import Optional

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the item")
    description: Optional[str] = Field(None, max_length=500, description="Description of the item")
    price: float = Field(..., gt=0, description="Price must be greater than zero")

@app.post("/items/",
          response_model=ItemCreate,
          status_code=status.HTTP_201_CREATED,
          summary="Create a new item")
async def create_item(item: ItemCreate) -> ItemCreate:
    """
    Create a new item in the system.

    Args:
        item: The item data to create (validated against Item model)

    Returns:
        The created item with its assigned ID
    """
    return item
```

### Other HTTP Methods
```python
@app.put("/items/{item_id}", summary="Update an existing item")
async def update_item(item_id: int, item: ItemCreate):
    return {"item_id": item_id, **item.model_dump()}

@app.patch("/items/{item_id}", summary="Partially update an item")
async def patch_item(item_id: int, item: ItemCreate):
    return {"item_id": item_id, "updated_fields": item.model_dump(exclude_unset=True)}

@app.delete("/items/{item_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete an item")
async def delete_item(item_id: int):
    """
    Delete an item by its ID.

    Args:
        item_id: The unique identifier of the item to delete
    """
    return {}  # Return empty response for 204 status

@app.head("/items/{item_id}", summary="Get item headers only")
async def get_item_headers(item_id: int):
    return {}

@app.options("/items/{item_id}", summary="Get allowed methods")
async def get_item_options(item_id: int):
    return {}
```

## Path and Query Parameters

### Path Parameters with Validation
```python
from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(..., ge=1, description="The unique identifier of the user to retrieve")
):
    return {"user_id": user_id}

@app.get("/files/{file_path:path}")
async def read_file(
    file_path: str = Path(..., description="Path parameter to catch the rest of the path")
):
    return {"file_path": file_path}
```

### Query Parameters with Validation
```python
from typing import Optional, List

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, max_length=100, description="Search query parameter"),
    skip: int = Query(0, ge=0, description="Number of items to skip for pagination"),
    limit: int = Query(100, le=1000, description="Maximum number of items to return"),
    sort: Optional[str] = Query("asc", regex=r"^(asc|desc)$", description="Sort order")
):
    return {"q": q, "skip": skip, "limit": limit, "sort": sort}

# Multiple values for query parameter
@app.get("/items/multiple/")
async def read_multiple_items(
    tags: List[str] = Query([], description="Multiple tags to filter by")
):
    return {"tags": tags}
```

### Request Body Parameters with Validation
```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    tax: Optional[float] = Field(None, ge=0)

@app.post("/items/")
async def create_item(item: Item):
    return item

# Multiple parameters: path, query, and body
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    q: Optional[str] = Query(None, description="Additional query parameter")
):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
```

## Request and Response Models

### Pydantic Models with Modern Validation
```python
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: str = Field(..., description="Valid email address")
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Password with minimum 8 characters")

class User(UserBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, description="Account activation status")

    model_config = {"from_attributes": True}  # Modern way to enable ORM mode

class Item(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Item title")
    description: Optional[str] = Field(None, max_length=500, description="Item description")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    category: str = Field(..., pattern=r"^[a-zA-Z]+$", description="Category with letters only")

    @model_validator(mode='after')
    def validate_price_category(self):
        """Custom validation using model_validator (modern approach)"""
        if self.price > 1000 and self.category.lower() == 'basic':
            raise ValueError('Basic category items cannot exceed $1000')
        return self
```

### Response Models with Exclusion Options
```python
from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.post("/users/",
          response_model=User,
          response_model_exclude_unset=True,  # Exclude fields not explicitly set
          summary="Create a new user")
async def create_user(user: UserCreate) -> User:
    # Simulate DB creation
    db_user = User(
        id=1,
        email=user.email,
        username=user.username,
        created_at=datetime.utcnow()
    )
    return db_user

@app.get("/users/",
         response_model=List[User],
         response_model_exclude={"password"},  # Exclude sensitive fields
         summary="Get all users")
async def get_users(skip: int = 0, limit: int = 100) -> List[User]:
    # Return list of users
    return []
```

### Response Model Properties
```python
from typing import Union

class BaseItem(BaseModel):
    name: str
    description: str

class CarItem(BaseItem):
    type: str = "car"

class PlaneItem(BaseItem):
    type: str = "plane"
    max_altitude: float

@app.get("/items/{item_id}",
         response_model=Union[CarItem, PlaneItem],
         summary="Get item with dynamic response type")
async def read_item(item_id: str) -> Union[CarItem, PlaneItem]:
    # Return different types based on item_id
    if item_id.startswith("car"):
        return CarItem(name="My Car", description="A nice car", type="car")
    else:
        return PlaneItem(name="My Plane", description="A nice plane", max_altitude=10000)
```

## Dependency Injection

### Simple Dependencies
```python
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(
    q: str = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=1000)
):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

### Security Dependencies with Modern Patterns
```python
from fastapi.security import HTTPBearer
from fastapi import HTTPException, status, Security

security = HTTPBearer()

async def get_current_user(token: str = Security(security)) -> dict:
    """Modern security dependency using Security() for OAuth2 scenarios"""
    # Validate token (in real implementation, use proper JWT validation)
    if token.credentials != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": "admin", "id": 1}

@app.get("/protected/")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return current_user
```

### Database Dependencies with Async Support
```python
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Async dependency to get database session"""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

@app.get("/items/")
async def read_items(db: AsyncSession = Depends(get_db)):
    # Use async database operations
    pass
```

### Sub-dependencies
```python
async def query_extractor(q: str = Query(None)) -> str:
    return q

async def query_or_body(commons: str = Depends(query_extractor), b: str = Query(None)) -> str:
    if b:
        return b
    return commons

@app.get("/items/")
async def read_query(query_or_body: str = Depends(query_or_body)):
    return {"q_or_body": query_or_body}
```

## Middleware

### Custom Middleware with Async Support
```python
import time
from fastapi import Request
from typing import Callable

@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable):
    """Modern middleware using @app.middleware decorator"""
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### CORS Middleware
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Specify exact origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Trusted Host Middleware
```python
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "*.example.com"]  # Specify allowed hosts
)
```

## Testing

### Basic Test Setup with Async Support
```python
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
import asyncio

# For sync testing
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Foo", "price": 50.5, "description": "A test item"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Foo"

# For async testing
@pytest.mark.asyncio
async def test_create_item_async():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/items/", json={"name": "Foo", "price": 50.5})
    assert response.status_code == 200
```

### Advanced Testing with Fixtures
```python
@pytest.fixture(scope="module")
def test_client():
    """Create test client as a fixture"""
    with TestClient(app) as client:
        yield client

def test_update_item(test_client):
    response = test_client.put(
        "/items/1",
        json={"name": "Bar", "price": 10.5, "description": "Updated item"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Bar"

def test_validation_error(test_client):
    response = test_client.post(
        "/items/",
        json={"name": "Foo", "price": -5}  # Invalid price
    )
    assert response.status_code == 422  # Validation error

@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
```

## Async/Await Patterns

### Async Endpoints with External Services
```python
import asyncio
import httpx
from typing import List

@app.get("/async-items/", summary="Get items asynchronously")
async def get_async_items() -> List[dict]:
    """Simulate async operation with delay"""
    await asyncio.sleep(0.1)  # Simulate async operation
    return [
        {"id": 1, "name": "Item 1", "price": 10.99},
        {"id": 2, "name": "Item 2", "price": 15.99}
    ]

@app.get("/fetch-data/", summary="Fetch external data asynchronously")
async def fetch_external_data():
    """Fetch data from external API asynchronously"""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/json", timeout=10.0)
        return response.json()
```

### Background Tasks
```python
from fastapi import BackgroundTasks
import asyncio

async def write_notification(email: str, message: str = ""):
    """Async background task"""
    async with aiofiles.open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message} at {datetime.now()}\n"
        await email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks,
    message: str = Query("Default notification message")
):
    """Send notification in the background"""
    background_tasks.add_task(write_notification, email, message=message)
    return {"message": "Notification will be sent in the background"}
```

## APIRouter Organization

### Main App Structure with Modern Patterns
```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from api.routers import users, items, orders
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: Initialize resources
    print("Starting up...")
    yield
    # Shutdown: Clean up resources
    print("Shutting down...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# Include routers with prefixes
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(items.router, prefix="/api/v1", tags=["items"])
app.include_router(orders.router, prefix="/api/v1", tags=["orders"])

@app.get("/")
async def read_root():
    return {"message": "Main API endpoint"}
```

### Router Files with Modern Patterns

users.py:
```python
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import User, UserCreate
from database.session import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User], summary="Get all users")
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
) -> List[User]:
    """Get a list of users with pagination."""
    users = await User.get_multi(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User, summary="Get user by ID")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)) -> User:
    """Get a specific user by their unique identifier."""
    user = await User.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.post("/",
             response_model=User,
             status_code=status.HTTP_201_CREATED,
             summary="Create a new user")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)) -> User:
    """Create a new user in the system."""
    db_user = await User.create(db, obj_in=user)
    return db_user
```

## Error Handling

### Custom HTTP Exceptions with Modern Status Codes
```python
from fastapi import HTTPException, status, FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID must be positive",
            headers={"X-Error": "Invalid user ID provided"},
        )
    if user_id > 1000000:  # Assuming max user ID is 1M
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"user_id": user_id}
```

### Global Exception Handlers
```python
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc: StarletteHTTPException):
    """Handle HTTP exceptions with custom response format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "error_code": exc.status_code}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    """Handle request validation errors with detailed information."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": exc.errors(),
            "error_code": "VALIDATION_ERROR"
        }
    )
```

### Custom Exception Classes
```python
from fastapi.responses import JSONResponse

class BusinessLogicException(Exception):
    """Custom exception for business logic errors."""
    def __init__(self, message: str, error_code: str = "BUSINESS_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

@app.exception_handler(BusinessLogicException)
async def business_logic_exception_handler(request, exc: BusinessLogicException):
    """Handle business logic exceptions."""
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.message,
            "error_code": exc.error_code
        }
    )

@app.get("/business-operation/{operation_id}")
async def business_operation(operation_id: str):
    if operation_id == "invalid":
        raise BusinessLogicException(
            message="Invalid operation requested",
            error_code="INVALID_OPERATION"
        )
    return {"operation_id": operation_id, "status": "success"}
```

## Production Deployment

### Environment Configuration with Modern Settings
```python
from typing import List
from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Production App"
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

    model_config = {"env_file": ".env"}


settings = Settings()
```

### Gunicorn Configuration for Production
gunicorn.conf.py:
```python
import multiprocessing
import os

# Server socket
bind = os.getenv("BIND", "0.0.0.0:8000")
backlog = 2048

# Worker processes
workers = int(os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1))
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to help prevent memory leaks
max_requests = 1000
max_requests_jitter = 100

# Logging
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("LOG_LEVEL", "info")
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "fastapi_production"

# Preloading app
preload_app = True

# Thread support
threads = 1
```

### Dockerfile for Production
```dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "main:app", "--config", "gunicorn.conf.py"]
```

### Requirements File for Production
requirements.txt:
```
fastapi==0.115.0
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
gunicorn==23.0.0
```

### Health Check Endpoint
```python
from datetime import datetime

@app.get("/health", summary="Health check endpoint")
async def health_check():
    """Health check endpoint to verify the service is operational."""
    return {
        "status": "healthy",
        "service": "FastAPI Production App",
        "version": settings.VERSION,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/ready", summary="Readiness check endpoint")
async def readiness_check():
    """Readiness check to verify the service is ready to accept traffic."""
    # Add checks for database connectivity, etc.
    return {"status": "ready"}
```

## Environment Configuration

### Modern Settings Management
```python
from pydantic_settings import BaseSettings
from typing import List, Optional
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


class Settings(BaseSettings):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    # Application
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = False
    VERSION: str = "1.0.0"

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 5
    DATABASE_POOL_TIMEOUT: int = 30
    DATABASE_POOL_RECYCLE: int = 3600

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = []

    model_config = {"env_file": ".env", "case_sensitive": True}


settings = Settings()
```

### Example .env File
```bash
# Application Settings
ENVIRONMENT=development
APP_NAME=My FastAPI Application
DEBUG=1
VERSION=1.0.0

# Security
SECRET_KEY=change-this-to-a-secure-random-key-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname

# CORS
BACKEND_CORS_ORIGINS=http://localhost,http://localhost:3000
```

## Security Best Practices

### JWT Token Authentication
```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Security scheme
oauth2_scheme = HTTPBearer()


async def get_current_user(token: str = Security(oauth2_scheme)) -> dict:
    """Get the current user from the JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"username": username}
```

This updated skill provides a comprehensive foundation for developing modern, production-ready FastAPI applications with async patterns, security best practices, and scalable architecture.