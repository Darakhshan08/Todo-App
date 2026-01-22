"""
In-memory task storage for Phase I Todo CLI.
"""
from typing import Optional
from src.models.task import Task


class TaskStore:
    """
    In-memory task storage using dictionary.

    Manages task persistence within a single session.
    All data is lost when the application exits.

    Attributes:
        _tasks: Dictionary mapping task ID to Task objects
        _next_id: Counter for generating sequential task IDs
    """

    def __init__(self):
        """Initialize empty task store with ID counter starting at 1."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        """
        Add a task to the store.

        Args:
            task: Task object to store

        Returns:
            The stored task object

        Raises:
            ValueError: If task with given ID already exists
        """
        if task.id in self._tasks:
            raise ValueError(f"Task with ID {task.id} already exists")
        self._tasks[task.id] = task
        return task

    def get(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by ID.

        Args:
            task_id: Unique task identifier

        Returns:
            Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def delete(self, task_id: int) -> bool:
        """
        Delete a task from the store.

        Args:
            task_id: Unique task identifier

        Returns:
            True if task was deleted, False if task not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def get_all(self) -> list[Task]:
        """
        Retrieve all tasks.

        Returns:
            List of all tasks in creation order (sorted by ID)
        """
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_next_id(self) -> int:
        """
        Get the next available task ID and increment counter.

        Returns:
            Next sequential task ID
        """
        task_id = self._next_id
        self._next_id += 1
        return task_id
