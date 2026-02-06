#!/usr/bin/env python3
"""
FastAPI CRUD Generator
Generates modern, async CRUD endpoints for a given resource
"""

import os
import sys
from pathlib import Path

def generate_crud_endpoints(resource_name):
    """Generate modern CRUD endpoints for a resource with async support"""

    # Convert to proper case for class names
    class_name = resource_name.capitalize()
    plural_class_name = resource_name.capitalize() + "s"

    # Generate schema file with proper validation
    schema_content = f'''from pydantic import BaseModel, Field
from typing import Optional


class {class_name}Base(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the {resource_name}")
    description: Optional[str] = Field(None, max_length=500, description="Description of the {resource_name}")


class {class_name}Create({class_name}Base):
    """Schema for creating {resource_name}s - excludes ID which is generated server-side"""
    pass


class {class_name}Update(BaseModel):
    """Schema for updating {resource_name}s - all fields are optional"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class {class_name}({class_name}Base):
    """Response schema that includes the generated ID"""
    id: int

    class Config:
        from_attributes = True  # Enable ORM mode for SQLAlchemy
'''

    # Generate model file with async methods
    model_content = f'''from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

from database.base import Base


class {class_name}Model(Base):
    __tablename__ = "{resource_name.lower()}s"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)

    @classmethod
    async def get_multi(
        cls,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100
    ) -> List["{class_name}Model"]:
        """Get multiple {resource_name}s with pagination."""
        result = await db.execute(
            select(cls).offset(skip).limit(limit)
        )
        return result.scalars().all()

    @classmethod
    async def get(cls, db: AsyncSession, id: int) -> Optional["{class_name}Model"]:
        """Get a {resource_name} by ID."""
        result = await db.execute(select(cls).where(cls.id == id))
        return result.scalar_one_or_none()

    @classmethod
    async def create(cls, db: AsyncSession, obj_in) -> "{class_name}Model":
        """Create a new {resource_name}."""
        db_obj = cls(**obj_in.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @classmethod
    async def update(
        cls,
        db: AsyncSession,
        db_obj: "{class_name}Model",
        obj_in
    ) -> "{class_name}Model":
        """Update an existing {resource_name}."""
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @classmethod
    async def remove(cls, db: AsyncSession, id: int) -> bool:
        """Remove a {resource_name} by ID."""
        obj = await cls.get(db, id)
        if obj:
            await db.delete(obj)
            await db.commit()
            return True
        return False
'''

    # Generate router file with async support and proper error handling
    router_content = f'''from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.{resource_name} import {class_name}, {class_name}Create, {class_name}Update
from database.session import get_db
from models.{resource_name} import {class_name}Model

router = APIRouter(prefix="/{resource_name.lower()}s", tags=["{resource_name.lower()}s"])

@router.get("/", response_model=List[{class_name}])
async def read_{resource_name.lower()}s(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve {resource_name}s with pagination support.

    Args:
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return

    Returns:
        List of {resource_name}s
    """
    {resource_name.lower()}s = await {class_name}Model.get_multi(db, skip=skip, limit=limit)
    return {resource_name.lower()}s

@router.get("/{{id}}", response_model={class_name})
async def read_{resource_name.lower()}(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific {resource_name} by ID.

    Args:
        id: The unique identifier of the {resource_name}

    Returns:
        The requested {resource_name}

    Raises:
        HTTPException: 404 if {resource_name} not found
    """
    {resource_name.lower()} = await {class_name}Model.get(db, id)
    if {resource_name.lower()} is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="{class_name} not found"
        )
    return {resource_name.lower()}

@router.post("/", response_model={class_name}, status_code=status.HTTP_201_CREATED)
async def create_{resource_name.lower()}(
    {resource_name.lower()}_data: {class_name}Create,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new {resource_name}.

    Args:
        {resource_name.lower()}_data: The data for the new {resource_name}

    Returns:
        The created {resource_name} with its assigned ID
    """
    db_{resource_name.lower()} = await {class_name}Model.create(db, obj_in={resource_name.lower()}_data)
    return db_{resource_name.lower()}

@router.put("/{{id}}", response_model={class_name})
async def update_{resource_name.lower()}(
    id: int,
    {resource_name.lower()}_data: {class_name}Update,
    db: AsyncSession = Depends(get_db)
):
    """
    Update an existing {resource_name}.

    Args:
        id: The unique identifier of the {resource_name} to update
        {resource_name.lower()}_data: The fields to update

    Returns:
        The updated {resource_name}

    Raises:
        HTTPException: 404 if {resource_name} not found
    """
    {resource_name.lower()} = await {class_name}Model.get(db, id)
    if {resource_name.lower()} is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="{class_name} not found"
        )

    updated_{resource_name.lower()} = await {class_name}Model.update(
        db,
        db_obj={resource_name.lower()},
        obj_in={resource_name.lower()}_data
    )
    return updated_{resource_name.lower()}

@router.delete("/{{id}}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_{resource_name.lower()}(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a {resource_name} by ID.

    Args:
        id: The unique identifier of the {resource_name} to delete

    Raises:
        HTTPException: 404 if {resource_name} not found
    """
    {resource_name.lower()} = await {class_name}Model.get(db, id)
    if {resource_name.lower()} is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="{class_name} not found"
        )

    await {class_name}Model.remove(db, id=id)
    return {{}}  # Return empty response for 204 status

@router.patch("/{{id}}", response_model={class_name})
async def partial_update_{resource_name.lower()}(
    id: int,
    {resource_name.lower()}_data: {class_name}Update,
    db: AsyncSession = Depends(get_db)
):
    """
    Partially update a {resource_name} (same as PUT in this implementation).

    Args:
        id: The unique identifier of the {resource_name} to update
        {resource_name.lower()}_data: The fields to update

    Returns:
        The updated {resource_name}

    Raises:
        HTTPException: 404 if {resource_name} not found
    """
    {resource_name.lower()} = await {class_name}Model.get(db, id)
    if {resource_name.lower()} is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="{class_name} not found"
        )

    updated_{resource_name.lower()} = await {class_name}Model.update(
        db,
        db_obj={resource_name.lower()},
        obj_in={resource_name.lower()}_data
    )
    return updated_{resource_name.lower()}
'''

    # Write files
    project_path = Path(".")

    # Create schemas directory if it doesn't exist
    (project_path / "schemas").mkdir(exist_ok=True)
    with open(project_path / "schemas" / f"{resource_name}.py", "w") as f:
        f.write(schema_content)

    # Create models directory if it doesn't exist
    (project_path / "models").mkdir(exist_ok=True)
    with open(project_path / "models" / f"{resource_name}.py", "w") as f:
        f.write(model_content)

    # Create api/routers directory if it doesn't exist
    (project_path / "api" / "routers").mkdir(parents=True, exist_ok=True)
    with open(project_path / "api" / "routers" / f"{resource_name}.py", "w") as f:
        f.write(router_content)

    print(f"Modern CRUD endpoints for '{resource_name}' have been generated!")
    print(f"- Schema: schemas/{resource_name}.py (with validation and documentation)")
    print(f"- Model: models/{resource_name}.py (with async CRUD methods)")
    print(f"- Router: api/routers/{resource_name}.py (with async endpoints and proper error handling)")


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_crud.py <resource_name>")
        print("Example: python generate_crud.py user")
        sys.exit(1)

    resource_name = sys.argv[1].lower()
    generate_crud_endpoints(resource_name)

if __name__ == "__main__":
    main()