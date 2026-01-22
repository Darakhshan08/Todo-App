"""
Task business logic service for Phase I Todo CLI.
"""
from src.models.task import Task, Priority, RecurrenceRule, SortOption
from src.store.task_store import TaskStore
from src.services.validation_service import ValidationService
from datetime import date
from typing import Optional


class TaskService:
    """
    Business logic for task operations.

    Coordinates between validation, domain models, and data storage.
    """

    def __init__(self, task_store: TaskStore):
        """
        Initialize TaskService.

        Args:
            task_store: TaskStore instance for persistence
        """
        self.task_store = task_store
        self.validator = ValidationService()

    def create_task(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        tags: list[str] | None = None,
        due_date: date | None = None,
        recurrence_rule: RecurrenceRule = RecurrenceRule.NONE,
    ) -> tuple[Task | None, str]:
        """
        Create a new task.

        Args:
            title: Task title (required)
            description: Task description (optional)
            priority: Priority level (default: MEDIUM)
            tags: List of tags (default: empty list)
            due_date: Due date (optional)
            recurrence_rule: Recurrence pattern (default: NONE)

        Returns:
            Tuple of (Task object, error_message)
            - (Task, "") if successful
            - (None, "error message") if validation fails
        """
        # Validate title
        is_valid, error = self.validator.validate_title(title)
        if not is_valid:
            return None, error

        # Validate description
        is_valid, error = self.validator.validate_description(description)
        if not is_valid:
            return None, error

        # Create task
        task_id = self.task_store.get_next_id()
        task = Task(
            id=task_id,
            title=title.strip(),
            description=description.strip(),
            completed=False,
            priority=priority,
            tags=tags or [],
            due_date=due_date,
            recurrence_rule=recurrence_rule,
        )

        # Add to store
        self.task_store.add(task)
        return task, ""

    def get_all_tasks(self) -> list[Task]:
        """
        Get all tasks.

        Returns:
            List of all tasks in creation order
        """
        return self.task_store.get_all()

    def get_task(self, task_id: int) -> Task | None:
        """
        Get a task by ID.

        Args:
            task_id: Task identifier

        Returns:
            Task object if found, None otherwise
        """
        return self.task_store.get(task_id)

    def complete_task(self, task_id: int) -> tuple[bool, str | Task]:
        """
        Mark a task as completed and handle recurring tasks.

        Args:
            task_id: Task identifier

        Returns:
            Tuple of (success, error_message_or_new_task)
            - (True, "") if successful (non-recurring)
            - (True, new_task) if successful and created recurring instance
            - (False, "error message") if task not found
        """
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        task.completed = True

        # Handle recurring tasks
        new_task = self.handle_recurring_completion(task)
        if new_task:
            return True, new_task
        else:
            return True, ""

    def incomplete_task(self, task_id: int) -> tuple[bool, str]:
        """
        Mark a task as incomplete.

        Args:
            task_id: Task identifier

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if task not found
        """
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        task.completed = False
        return True, ""

    def toggle_completion(self, task_id: int) -> tuple[bool, str]:
        """
        Toggle task completion status.

        Args:
            task_id: Task identifier

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if task not found
        """
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        task.completed = not task.completed
        return True, ""

    def update_task_title(self, task_id: int, new_title: str) -> tuple[bool, str]:
        """
        Update task title.

        Args:
            task_id: Task identifier
            new_title: New title value

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if validation fails or task not found
        """
        # Validate title
        is_valid, error = self.validator.validate_title(new_title)
        if not is_valid:
            return False, error

        # Get task
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Update title
        task.title = new_title.strip()
        return True, ""

    def update_task_description(self, task_id: int, new_description: str) -> tuple[bool, str]:
        """
        Update task description.

        Args:
            task_id: Task identifier
            new_description: New description value

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if validation fails or task not found
        """
        # Validate description
        is_valid, error = self.validator.validate_description(new_description)
        if not is_valid:
            return False, error

        # Get task
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Update description
        task.description = new_description.strip()
        return True, ""

    def update_task_priority(self, task_id: int, new_priority: Priority) -> tuple[bool, str]:
        """
        Update task priority.

        Args:
            task_id: Task identifier
            new_priority: New priority level (HIGH, MEDIUM, or LOW)

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if validation fails or task not found
        """
        # Validate priority
        is_valid, error = self.validator.validate_priority(new_priority.value)
        if not is_valid:
            return False, error

        # Get task
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Update priority
        task.priority = new_priority
        return True, ""

    def update_task_tags(self, task_id: int, new_tags: list[str]) -> tuple[bool, str]:
        """
        Update task tags.

        Args:
            task_id: Task identifier
            new_tags: List of tag strings (will be normalized to lowercase)

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if validation fails or task not found
        """
        # Validate tags
        is_valid, error = self.validator.validate_tags(new_tags)
        if not is_valid:
            return False, error

        # Get task
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Update tags (normalize to lowercase)
        task.tags = [tag.strip().lower() for tag in new_tags if tag.strip()]
        return True, ""

    def update_task_due_date(self, task_id: int, new_due_date: date | None) -> tuple[bool, str]:
        """
        Update task due date.

        Args:
            task_id: Task identifier
            new_due_date: New due date (or None to clear)

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if validation fails or task not found
        """
        # Validate due date if provided
        if new_due_date:
            is_valid, error = self.validator.validate_date(new_due_date.strftime("%Y-%m-%d"))
            if not is_valid:
                return False, error

        # Get task
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Update due date
        task.due_date = new_due_date
        return True, ""

    def update_task_recurrence(self, task_id: int, new_recurrence: RecurrenceRule) -> tuple[bool, str]:
        """
        Update task recurrence rule.

        Args:
            task_id: Task identifier
            new_recurrence: New recurrence rule

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if validation fails or task not found
        """
        # Validate recurrence
        is_valid, error = self.validator.validate_recurrence(new_recurrence.value)
        if not is_valid:
            return False, error

        # Get task
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Update recurrence
        task.recurrence_rule = new_recurrence
        return True, ""

    def handle_recurring_completion(self, task: Task) -> Optional[Task]:
        """
        Handle completion of a recurring task by creating a new instance.

        Args:
            task: The completed task

        Returns:
            New task instance if recurring, None otherwise
        """
        if task.recurrence_rule == RecurrenceRule.NONE or not task.due_date:
            return None

        # Calculate next due date
        from src.utils.date_utils import calculate_next_occurrence
        next_due_date = calculate_next_occurrence(task.due_date, task.recurrence_rule)

        # Create new task instance
        new_task, error = self.create_task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            tags=task.tags,
            due_date=next_due_date,
            recurrence_rule=task.recurrence_rule
        )

        return new_task if not error else None

    def search_tasks(self, keyword: str) -> list[Task]:
        """
        Search tasks by keyword in title and description (case-insensitive).

        Args:
            keyword: Search term to match

        Returns:
            List of tasks containing the keyword in title or description
        """
        if not keyword:
            return self.get_all_tasks()

        keyword_lower = keyword.lower()
        all_tasks = self.get_all_tasks()

        return [
            task for task in all_tasks
            if keyword_lower in task.title.lower()
            or keyword_lower in task.description.lower()
        ]

    def filter_by_status(self, completed: bool) -> list[Task]:
        """
        Filter tasks by completion status.

        Args:
            completed: True for completed tasks, False for pending tasks

        Returns:
            List of tasks with the specified completion status
        """
        all_tasks = self.get_all_tasks()
        return [task for task in all_tasks if task.completed == completed]

    def filter_by_priority(self, priority: Priority) -> list[Task]:
        """
        Filter tasks by priority level.

        Args:
            priority: Priority level to filter by

        Returns:
            List of tasks with the specified priority
        """
        all_tasks = self.get_all_tasks()
        return [task for task in all_tasks if task.priority == priority]

    def filter_by_tag(self, tag: str) -> list[Task]:
        """
        Filter tasks by tag (case-insensitive).

        Args:
            tag: Tag to search for

        Returns:
            List of tasks containing the specified tag
        """
        if not tag:
            return []

        tag_lower = tag.lower()
        all_tasks = self.get_all_tasks()

        return [
            task for task in all_tasks
            if tag_lower in [t.lower() for t in task.tags]
        ]

    def sort_tasks(self, sort_by: SortOption, tasks: list[Task] | None = None) -> list[Task]:
        """
        Sort tasks by specified criterion.

        Args:
            sort_by: Sort option (DEFAULT, DUE_DATE, PRIORITY, ALPHABETICAL)
            tasks: Optional list of tasks to sort (defaults to all tasks)

        Returns:
            Sorted list of tasks (non-destructive, original store unchanged)
        """
        if tasks is None:
            tasks = self.get_all_tasks()

        if sort_by == SortOption.DEFAULT:
            # Default: creation order (by ID)
            return sorted(tasks, key=lambda t: t.id)

        elif sort_by == SortOption.DUE_DATE:
            # Sort by due date: overdue first, then chronological, None at end
            def due_date_key(task: Task):
                if task.due_date is None:
                    return (2, date.max)  # No due date: sort to end
                elif task.is_overdue():
                    return (0, task.due_date)  # Overdue: sort to beginning
                else:
                    return (1, task.due_date)  # Future: middle, chronological

            return sorted(tasks, key=due_date_key)

        elif sort_by == SortOption.PRIORITY:
            # Sort by priority: High → Medium → Low
            priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}
            return sorted(tasks, key=lambda t: priority_order.get(t.priority, 1))

        elif sort_by == SortOption.ALPHABETICAL:
            # Sort alphabetically by title (case-insensitive)
            return sorted(tasks, key=lambda t: t.title.lower())

        else:
            # Unknown sort option: return as-is
            return tasks

    def delete_task(self, task_id: int) -> tuple[bool, str]:
        """
        Delete a task.

        Args:
            task_id: Task identifier

        Returns:
            Tuple of (success, error_message)
            - (True, "") if successful
            - (False, "error message") if task not found
        """
        # Check task exists
        task = self.task_store.get(task_id)
        if not task:
            return False, f"Task with ID {task_id} not found"

        # Delete from store
        success = self.task_store.delete(task_id)
        if success:
            return True, ""
        else:
            return False, f"Failed to delete task {task_id}"
