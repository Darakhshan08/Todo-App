# FastAPI Best Practices

## 1. Project Structure

```
project_name/
├── main.py              # Main application entry point
├── requirements.txt     # Project dependencies
├── .env                # Environment variables
├── alembic/            # Database migration files
│   ├── versions/
│   └── env.py
├── api/                # API route handlers
│   └── routers/
│       ├── users.py
│       ├── items.py
│       └── auth.py
├── models/             # Database models
│   ├── user.py
│   └── item.py
├── schemas/            # Pydantic schemas
│   ├── user.py
│   └── item.py
├── database/           # Database session and connection
│   ├── session.py
│   └── base.py
├── core/               # Core application settings
│   └── config.py
├── utils/              # Utility functions
│   └── security.py
└── tests/              # Test files
    ├── conftest.py
    ├── test_main.py
    └── api/
        ├── test_users.py
        └── test_items.py
```

## 2. Async/Await Patterns

### Use async functions for I/O-bound operations
```python
import httpx
import asyncio
from typing import List

@app.get("/external-data/")
async def fetch_external_data():
    """Fetch data from external API asynchronously."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/json", timeout=10.0)
        return response.json()

@app.get("/multiple-requests/")
async def fetch_multiple_requests():
    """Fetch multiple external resources concurrently."""
    async with httpx.AsyncClient() as client:
        tasks = [
            client.get("https://httpbin.org/json"),
            client.get("https://httpbin.org/uuid"),
            client.get("https://httpbin.org/ip")
        ]
        responses = await asyncio.gather(*tasks)
        return [resp.json() for resp in responses]
```

### Use async database operations
```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class UserService:
    @classmethod
    async def get_user_by_id(cls, db: AsyncSession, user_id: int):
        """Get user by ID using async database operations."""
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    @classmethod
    async def create_user(cls, db: AsyncSession, user_data: UserCreate):
        """Create user using async database operations."""
        db_user = User(**user_data.model_dump())
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
```

## 3. Dependency Injection

### Security dependencies
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from typing import Dict

security = HTTPBearer()

async def get_current_user(token: str = Depends(security)) -> Dict:
    """Get current user from JWT token."""
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    return {"user_id": user_id}

@app.get("/protected/")
async def protected_endpoint(current_user: dict = Depends(get_current_user)):
    return {"user_id": current_user["user_id"]}
```

### Database session dependency
```python
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get database session."""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

## 4. Error Handling

### Custom HTTP exceptions
```python
from fastapi import HTTPException, status

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID must be positive",
            headers={"X-Error": "Invalid user ID provided"},
        )
    user = await UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
```

### Global exception handlers
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

### Custom exception classes
```python
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
```

## 5. Response Models and Validation

### Proper response models
```python
from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    id: int

    model_config = {"from_attributes": True}  # Modern way to enable ORM mode

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await UserService.create_user(db, user)
    return db_user
```

### Response model exclusions
```python
@app.get("/users/", response_model=List[User])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    include_sensitive: bool = False,
    db: AsyncSession = Depends(get_db)
):
    users = await UserService.get_users(db, skip=skip, limit=limit)

    if not include_sensitive:
        # Exclude sensitive fields
        return [user.model_dump(exclude={"password"}) for user in users]

    return users
```

## 6. Testing Best Practices

### Unit tests with fixtures
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from main import app
from database.session import Base

@pytest.fixture(scope="module")
def client():
    """Create test client."""
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture(scope="function")
async def db_session():
    """Create database session for testing."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

        # Cleanup
        await session.rollback()
        await engine.dispose()

def test_create_user(client):
    """Test user creation endpoint."""
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123"
    }

    response = client.post("/users/", json=user_data)
    assert response.status_code == 200

    data = response.json()
    assert data["email"] == user_data["email"]
    assert "id" in data
```

### Async tests
```python
import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_async_endpoint():
    """Test async endpoint."""
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

## 7. Security Best Practices

### Password hashing
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)
```

### JWT token handling
```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

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
```

## 8. Configuration and Settings

### Modern settings with validation
```python
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI App"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 5
    DATABASE_POOL_TIMEOUT: int = 30

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000"]

    model_config = {"env_file": ".env"}

settings = Settings()
```

## 9. Performance Optimization

### Use connection pooling
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# For async operations
async_engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=0,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_recycle=3600,
    poolclass=QueuePool,
    echo=settings.DEBUG,
)
```

### Enable compression
```python
from fastapi.middleware.gzip import GZipMiddleware

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000,  # Compress responses larger than 1KB
)
```

### Use caching where appropriate
```python
import aiocache
from aiocache import cached

@cached(ttl=60)  # Cache for 60 seconds
async def get_expensive_data(param: str):
    # Expensive operation here
    return await some_expensive_operation(param)
```

## 10. Production Deployment

### Use lifespan for startup/shutdown
```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: Initialize resources
    print("Starting up...")
    # Initialize database connections, caches, etc.
    yield
    # Shutdown: Clean up resources
    print("Shutting down...")
    # Close connections, flush logs, etc.

app = FastAPI(lifespan=lifespan)
```

### Proper logging configuration
```python
import logging
from fastapi.logger import logger

# Configure logging for production
gunicorn_logger = logging.getLogger("gunicorn.error")
logger.handlers = gunicorn_logger.handlers
logger.setLevel(gunicorn_logger.level)
```

These best practices ensure that your FastAPI applications are secure, performant, maintainable, and production-ready.