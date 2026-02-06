# FastAPI Documentation Standards

## API Documentation Best Practices

### 1. Comprehensive Endpoint Documentation

```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Optional, List

from fastapi import FastAPI, Path, Query, status
from pydantic import BaseModel, Field


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: Initialize resources
    print("Starting up...")
    yield
    # Shutdown: Clean up resources
    print("Shutting down...")


app = FastAPI(
    title="Documented API",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)


class Item(BaseModel):
    """
    Represents an item in the system.

    Attributes:
        name (str): The name of the item (1-100 characters)
        description (Optional[str]): A brief description of the item
        price (float): The price of the item (> 0)
        tax (Optional[float]): Tax amount (>= 0)
    """
    name: str = Field(..., min_length=1, max_length=100, description="Name of the item")
    description: Optional[str] = Field(None, max_length=500, description="Description of the item")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    tax: Optional[float] = Field(None, ge=0, description="Tax amount (optional)")

    model_config = {"extra": "forbid"}  # Forbid extra fields not in model


@app.get(
    "/items/{item_id}",
    response_model=Item,
    summary="Get an item by ID",
    description="""
    Retrieve a specific item by its unique identifier.

    ## Features
    - Returns detailed information about the item
    - Supports optional query parameter for extended info
    - Implements proper error handling for invalid IDs

    ## Response Format
    - `id`: Unique identifier
    - `name`: Item name
    - `description`: Item description
    - `price`: Price value
    - `tax`: Tax amount (if available)
    """,
    response_description="The requested item details",
    tags=["Items"]
)
async def read_item(
    item_id: int = Path(
        ...,
        ge=1,
        description="The unique identifier of the item to retrieve"
    ),
    q: Optional[str] = Query(
        None,
        max_length=50,
        description="Optional query parameter for additional filtering"
    )
) -> Item:
    """
    Get an item by its unique identifier.

    Args:
        item_id (int): The unique identifier of the item (must be > 0)
        q (Optional[str]): Optional query parameter for additional filtering (max 50 chars)

    Returns:
        Item: The requested item with all its properties

    Raises:
        HTTPException: 404 if item not found
    """
    # Implementation here
    pass


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new item",
    description="Add a new item to the system with validation and proper error handling.",
    response_description="The created item with assigned ID",
    tags=["Items"]
)
async def create_item(
    item: Item,
    active_user: bool = Query(True, description="Whether the user is currently active")
) -> Item:
    """
    Create a new item in the system.

    This endpoint creates a new item with the provided details after validating
    the input according to the defined constraints.

    Args:
        item (Item): The item data to create (validated against Item model)
        active_user (bool): Whether the requesting user is active (default: True)

    Returns:
        Item: The created item with its assigned ID

    Example:
        POST /items/
        {
            "name": "New Item",
            "description": "A sample item",
            "price": 29.99,
            "tax": 2.50
        }
    """
    # Implementation here
    pass
```

### 2. Model Documentation with Modern Validation

```python
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional
import re


class UserBase(BaseModel):
    email: str = Field(..., description="Valid email address")
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Password with minimum 8 characters")


class User(UserBase):
    """
    User model representing a system user.

    This model defines the structure and validation rules for user data
    in the system. It includes validation for email format, username
    requirements, and other business rules.

    Attributes:
        id (int): Unique user identifier (auto-generated)
        email (str): Validated email address
        username (str): Unique username (3-50 alphanumeric characters)
        full_name (Optional[str]): User's full name
        created_at (datetime): Account creation timestamp
        is_active (bool): Account activation status
    """
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, description="Account activation status")

    model_config = {"from_attributes": True}  # Enable ORM mode for SQLAlchemy integration


class UserDetailed(User):
    full_name: Optional[str] = Field(None, max_length=100, description="Full name of the user")

    @model_validator(mode='after')
    def validate_username_format(self):
        """
        Validate username format using modern model_validator.

        Ensures username contains only alphanumeric characters and underscores.
        """
        if self.username and not re.match(r'^[a-zA-Z0-9_]+$', self.username):
            raise ValueError('Username must contain only letters, numbers, and underscores')
        return self
```

### 3. Error Documentation with Modern Patterns

```python
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import Dict, Any, Optional


class APIErrorDetail(BaseModel):
    """
    Structure for API error details.

    Provides a consistent format for error responses across the API.
    """
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None


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


@app.get("/protected/{item_id}")
async def get_protected_item(item_id: int):
    """
    Get a protected item with proper error handling.

    This endpoint demonstrates comprehensive error documentation and handling.

    ## Possible Responses:
    - 200: Successfully retrieved item
    - 401: Authentication required
    - 403: Insufficient permissions
    - 404: Item not found
    - 422: Validation error in parameters
    - 500: Internal server error

    ## Security:
    This endpoint requires authentication and authorization.

    Args:
        item_id (int): ID of the item to retrieve (must be > 0)

    Returns:
        Item: The requested item if authorized

    Raises:
        HTTPException: 401 if not authenticated
        HTTPException: 403 if insufficient permissions
        HTTPException: 404 if item doesn't exist
    """
    # Implementation with proper error handling
    if item_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": "INVALID_ID",
                "message": "Item ID must be a positive integer",
                "details": {"received_id": item_id}
            }
        )

    # Additional logic here...
    pass
```

### 4. API Router Documentation with Modern Patterns

```python
from fastapi import APIRouter, Depends, status
from typing import List

# Create documented router with modern patterns
items_router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[],  # Optional global dependencies
    responses={404: {"description": "Item not found"}},
    # Documentation for the entire router
)

@items_router.get("/", response_model=List[Item], description="Retrieve a list of all items in the system")
async def get_items():
    """Get all items with pagination support."""
    pass

@items_router.get("/{item_id}", response_model=Item, description="Get a specific item by its unique identifier")
async def get_item(item_id: int):
    """Get a specific item."""
    pass

@items_router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED, description="Create a new item")
async def create_item(item: Item):
    """Create a new item."""
    pass

# Include router with documentation
app.include_router(
    items_router,
    prefix="/api/v1",
    tags=["items"],
    responses={404: {"description": "Item not found in v1 API"}}
)
```

### 5. Configuration and Settings Documentation with Modern Patterns

```python
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """
    Application settings and configuration.

    This class defines all configurable aspects of the application
    using Pydantic's BaseSettings functionality. Settings can be
    loaded from environment variables, .env files, or defaults.

    ## Environment Variables:
    - `APP_NAME`: Name of the application
    - `DEBUG`: Enable/disable debug mode
    - `DATABASE_URL`: Database connection string
    - `SECRET_KEY`: Secret key for security operations
    - `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
    """

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

@app.get("/config")
async def get_config():
    """
    Get current application configuration.

    This endpoint returns non-sensitive configuration values
    for debugging and monitoring purposes.

    Returns:
        dict: Public configuration values
    """
    return {
        "project_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "debug": settings.DEBUG,
    }
```

### 6. Testing Documentation with Async Support

```python
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app

# For sync testing
client = TestClient(app)

def test_read_main():
    """
    Test the main endpoint.

    ## Test Description:
    Verify that the root endpoint returns the expected response.

    ## Expected Behavior:
    - Status code should be 200
    - Response should contain welcome message
    - Content type should be JSON

    ## Test Steps:
    1. Send GET request to "/"
    2. Verify status code is 200
    3. Verify response content
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

# For async testing
@pytest.mark.asyncio
async def test_create_item_async():
    """
    Test item creation endpoint with async client.

    ## Test Description:
    Verify that items can be created successfully with valid data using async client.

    ## Test Data:
    - name: "Test Item"
    - description: "A test item"
    - price: 10.50
    - tax: 1.00

    ## Expected Behavior:
    - Status code should be 200 or 201
    - Response should contain the created item data
    - ID should be assigned automatically
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/items/",
            json={
                "name": "Test Item",
                "description": "A test item",
                "price": 10.50,
                "tax": 1.00
            }
        )
    assert response.status_code in [200, 201]
    assert response.json()["name"] == "Test Item"
    assert "id" in response.json()
```

### 7. Deployment and Production Documentation

```python
# Production-ready configuration
import logging
from fastapi.logger import logger

# Configure logging for production
gunicorn_logger = logging.getLogger("gunicorn.error")
logger.handlers = gunicorn_logger.handlers
logger.setLevel(gunicorn_logger.level)

# Production middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

# Add security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_ORIGINS
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Documentation for production deployment
PRODUCTION_NOTES = """
# Production Deployment Notes

## Server Configuration
- Use Gunicorn with multiple workers for production
- Enable HTTPS in production environments
- Configure proper logging and monitoring

## Security Considerations
- Never expose SECRET_KEY in source code
- Use environment variables for sensitive data
- Implement rate limiting for public endpoints
- Use proper authentication and authorization
- Keep dependencies updated

## Performance Optimization
- Enable compression for large responses
- Implement caching for frequently accessed data
- Use async operations for I/O bound tasks
- Monitor and optimize database queries

## Monitoring and Logging
- Log important events and errors
- Monitor API usage and performance
- Set up alerts for critical failures
- Track response times and error rates
"""
```

This documentation approach ensures that every aspect of your FastAPI application is properly documented using modern patterns, making it easier for developers to understand, use, and maintain the API.