"""
Task domain model and enums for Phase I Todo CLI.
"""
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class Priority(Enum):
    """Priority levels for tasks."""
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class RecurrenceRule(Enum):
    """Recurrence patterns for tasks."""
    NONE = "NONE"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class SortOption(Enum):
    """Sort options for task lists."""
    DEFAULT = "DEFAULT"  # Creation order (by ID)
    DUE_DATE = "DUE_DATE"  # Chronological, overdue first
    PRIORITY = "PRIORITY"  # High → Medium → Low
    ALPHABETICAL = "ALPHABETICAL"  # Case-insensitive title sort


@dataclass
class Task:
    """
    Task entity representing a todo item.

    Attributes:
        id: Unique sequential identifier (immutable, never reused)
        title: Task title (1-200 characters, required)
        description: Optional detailed description (0-1000 characters)
        completed: Completion status (true/false)
        priority: Task priority level (HIGH, MEDIUM, LOW)
        tags: List of tags for categorization (normalized to lowercase)
        due_date: Optional due date (YYYY-MM-DD format)
        recurrence_rule: Recurrence pattern (NONE, DAILY, WEEKLY, MONTHLY)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    tags: list[str] = field(default_factory=list)
    due_date: Optional[date] = None
    recurrence_rule: RecurrenceRule = RecurrenceRule.NONE

    def is_overdue(self) -> bool:
        """
        Check if the task is overdue.

        Returns:
            True if task has a due date in the past and is not completed, False otherwise.
        """
        if self.due_date is None or self.completed:
            return False
        return self.due_date < date.today()
