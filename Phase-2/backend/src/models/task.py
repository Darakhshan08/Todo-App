"""
Task model for todo items
"""
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import JSON
from datetime import datetime
from typing import Optional, List
from pydantic import field_validator


class TaskBase(SQLModel):
    """Base task model with common fields"""
    title: str = Field(
        min_length=1,
        max_length=200,
        description="Task title (required, 1-200 characters)"
    )
    description: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="Task description (optional, max 1000 characters)"
    )
    completed: bool = Field(default=False, description="Task completion status")
    priority: str = Field(default="medium", description="Task priority level (high, medium, low)")
    tags: List[str] = Field(default_factory=list, sa_column=Column(JSON), description="Task tags (e.g., work, home)")
    due_date: Optional[datetime] = Field(default=None, description="Task due date and time")
    recurring: Optional[str] = Field(default=None, description="Recurring pattern (daily, weekly, monthly)")

    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v: str) -> str:
        """Validate priority is one of the allowed values"""
        allowed = ["high", "medium", "low"]
        if v not in allowed:
            raise ValueError(f"Priority must be one of {allowed}, got: {v}")
        return v

    @field_validator('recurring')
    @classmethod
    def validate_recurring(cls, v: Optional[str]) -> Optional[str]:
        """Validate recurring pattern"""
        if v is not None:
            allowed = ["daily", "weekly", "monthly", "yearly"]
            if v not in allowed:
                raise ValueError(f"Recurring must be one of {allowed}, got: {v}")
        return v


class Task(TaskBase, table=True):
    """
    Task database model with user isolation.
    Each task belongs to a single user.
    """
    __tablename__ = "tasks"

    id: int = Field(default=None, primary_key=True, description="Unique task identifier")
    user_id: str = Field(foreign_key="users.id", index=True, description="Owner user ID")
    created_at: datetime = Field(description="Creation timestamp")
    updated_at: datetime = Field(description="Last update timestamp")


class TaskCreate(TaskBase):
    """Model for creating a new task"""
    pass


class TaskUpdate(SQLModel):
    """Model for updating a task (all fields optional)"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None
    priority: Optional[str] = None
    tags: Optional[List[str]] = None
    due_date: Optional[datetime] = None
    recurring: Optional[str] = None

    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v: Optional[str]) -> Optional[str]:
        """Validate priority is one of the allowed values"""
        if v is not None:
            allowed = ["high", "medium", "low"]
            if v not in allowed:
                raise ValueError(f"Priority must be one of {allowed}, got: {v}")
        return v

    @field_validator('recurring')
    @classmethod
    def validate_recurring(cls, v: Optional[str]) -> Optional[str]:
        """Validate recurring pattern"""
        if v is not None:
            allowed = ["daily", "weekly", "monthly", "yearly"]
            if v not in allowed:
                raise ValueError(f"Recurring must be one of {allowed}, got: {v}")
        return v


class TaskPublic(TaskBase):
    """Public task model for API responses"""
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime


class TaskList(SQLModel):
    """Model for paginated task list response"""
    tasks: list[TaskPublic]
    total: int
    page: int
    page_size: int
