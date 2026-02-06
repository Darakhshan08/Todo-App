from contextlib import asynccontextmanager
from typing import AsyncGenerator, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field
import uvicorn


# Initialize security
security = HTTPBearer()


# Example Pydantic models with updated validation
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the item")
    description: Optional[str] = Field(None, max_length=500, description="Description of the item")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    tax: Optional[float] = Field(None, ge=0, description="Tax amount (optional)")

    model_config = {"extra": "forbid"}  # Forbid extra fields not in model


class ItemCreate(Item):
    """Model for creating items - excludes ID which is generated server-side"""
    pass


class ItemUpdate(BaseModel):
    """Model for updating items - all fields are optional"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    tax: Optional[float] = Field(None, ge=0)

    model_config = {"extra": "forbid"}


class ItemResponse(Item):
    """Response model that includes the generated ID"""
    id: int


# In-memory storage for demo
items_db = []


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
    # Additional configuration for production
    docs_url="/docs",  # Enable interactive API documentation
    redoc_url="/redoc",  # Enable ReDoc documentation
)


@app.get("/", response_model=dict, summary="Health check endpoint")
async def read_root() -> dict:
    """
    Basic health check endpoint.

    Returns a welcome message to confirm the API is running.
    """
    return {"message": "Welcome to FastAPI Production Template!"}


@app.get("/items/{item_id}",
         response_model=ItemResponse,
         summary="Get an item by ID",
         description="Retrieve a specific item by its unique identifier.")
async def read_item(item_id: int, q: Optional[str] = None) -> ItemResponse:
    """
    Get an item by its unique identifier.

    - **item_id**: The unique identifier of the item to retrieve (must be > 0)
    - **q**: Optional query parameter for additional filtering

    Returns the requested item with all its properties.

    Raises:
        HTTPException: 404 if item not found
    """
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )

    item_data = items_db[item_id].copy()
    if q:
        item_data["description"] = q

    return ItemResponse(id=item_id, **item_data)


@app.post("/items/",
          response_model=ItemResponse,
          status_code=status.HTTP_201_CREATED,
          summary="Create a new item",
          description="Add a new item to the system with validation and proper error handling.")
async def create_item(item: ItemCreate) -> ItemResponse:
    """
    Create a new item in the system.

    This endpoint creates a new item with the provided details after validating
    the input according to the defined constraints.

    Args:
        item: The item data to create (validated against Item model)

    Returns:
        ItemResponse: The created item with its assigned ID
    """
    item_dict = item.model_dump()
    items_db.append(item_dict)
    new_id = len(items_db) - 1
    return ItemResponse(id=new_id, **item_dict)


@app.put("/items/{item_id}",
         response_model=ItemResponse,
         summary="Update an existing item",
         description="Update an existing item with the provided data.")
async def update_item(item_id: int, item_update: ItemUpdate) -> ItemResponse:
    """
    Update an existing item partially.

    This endpoint updates an existing item with the provided data.
    Only the fields provided in the request will be updated.

    Args:
        item_id: The unique identifier of the item to update
        item_update: The fields to update (only specified fields will be changed)

    Returns:
        ItemResponse: The updated item with all its properties

    Raises:
        HTTPException: 404 if item not found
    """
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )

    stored_item = items_db[item_id]
    # Update only the fields that were provided in the request
    update_data = item_update.model_dump(exclude_unset=True)
    stored_item.update(update_data)

    return ItemResponse(id=item_id, **stored_item)


@app.delete("/items/{item_id}",
            summary="Delete an item",
            description="Remove an item from the system by its ID.")
async def delete_item(item_id: int) -> dict:
    """
    Delete an item by its unique identifier.

    Args:
        item_id: The unique identifier of the item to delete

    Returns:
        dict: Confirmation message

    Raises:
        HTTPException: 404 if item not found
    """
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )

    items_db.pop(item_id)
    return {"message": f"Item {item_id} deleted successfully"}


@app.get("/health",
         summary="Health check endpoint",
         description="Simple endpoint to check if the service is running.")
async def health_check() -> dict:
    """
    Health check endpoint to verify the service is operational.

    Returns basic health status information.
    """
    return {
        "status": "healthy",
        "service": "FastAPI Template",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)