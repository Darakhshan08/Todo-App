"""
User model - managed by Better Auth
"""
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class User(SQLModel, table=True):
    """
    User model managed by Better Auth.
    This model mirrors the Better Auth user table.
    """
    __tablename__ = "users"

    id: str = Field(primary_key=True, description="Unique user identifier")
    email: str = Field(unique=True, index=True, description="User email address")
    name: str = Field(description="User full name")
    password_hash: str = Field(description="Hashed password")
    created_at: datetime = Field(description="Account creation timestamp")
    updated_at: Optional[datetime] = Field(default=None, description="Last update timestamp")


class UserCreate(SQLModel):
    """Model for creating a new user"""
    email: str
    name: str
    password: str


class UserPublic(SQLModel):
    """Public user model for API responses (excludes sensitive data)"""
    id: str
    email: str
    name: str
    created_at: datetime
