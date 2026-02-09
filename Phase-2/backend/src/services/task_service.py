"""
Task Service - Business logic for task operations
Task: T024, T030, T036, T042, T047 [US1-US5] Task service implementation
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from src.models.task import Task, TaskCreate, TaskUpdate
from typing import List, Optional
from datetime import datetime


class TaskService:
    """Service layer for task operations with user isolation"""

    @staticmethod
    async def create_task(
        db: AsyncSession, user_id: str, task_data: TaskCreate
    ) -> Task:
        """
        Create a new task for the user.

        Args:
            db: Database session
            user_id: User ID from authenticated session
            task_data: Task creation data

        Returns:
            Created task object
        """
        now = datetime.utcnow()

        # Convert timezone-aware datetime to naive datetime for PostgreSQL
        due_date_naive = None
        if task_data.due_date:
            due_date_naive = task_data.due_date.replace(tzinfo=None) if task_data.due_date.tzinfo else task_data.due_date

        task = Task(
            user_id=user_id,
            title=task_data.title,
            description=task_data.description,
            completed=False,
            priority=task_data.priority,
            tags=task_data.tags if task_data.tags else [],
            due_date=due_date_naive,
            recurring=task_data.recurring,
            created_at=now,
            updated_at=now,
        )

        db.add(task)
        await db.commit()
        await db.refresh(task)

        return task

    @staticmethod
    async def get_tasks(
        db: AsyncSession,
        user_id: str,
        status: Optional[str] = "all",
        priority: Optional[str] = None,
        tag: Optional[str] = None,
        search: Optional[str] = None,
        sort: Optional[str] = "created",
        skip: int = 0,
        limit: int = 100,
    ) -> List[Task]:
        """
        Get all tasks for a user with filtering, searching, and sorting.

        Args:
            db: Database session
            user_id: User ID (enforces user isolation)
            status: Filter by status ("all", "pending", "completed")
            priority: Filter by priority ("high", "medium", "low")
            tag: Filter by tag (e.g., "work", "home")
            search: Search keyword in title or description
            sort: Sort by field ("created", "title", "updated", "priority")
            skip: Number of records to skip (pagination)
            limit: Maximum number of records to return

        Returns:
            List of task objects
        """
        query = select(Task).where(Task.user_id == user_id)

        # Filter by status
        if status == "pending":
            query = query.where(Task.completed == False)
        elif status == "completed":
            query = query.where(Task.completed == True)

        # Filter by priority
        if priority:
            query = query.where(Task.priority == priority)

        # Filter by tag (check if tag is in tags array)
        if tag:
            # Use JSON contains operator for PostgreSQL
            from sqlalchemy.dialects.postgresql import ARRAY
            query = query.where(Task.tags.contains([tag]))

        # Search in title or description
        if search:
            search_pattern = f"%{search}%"
            from sqlalchemy import or_
            query = query.where(
                or_(
                    Task.title.ilike(search_pattern),
                    Task.description.ilike(search_pattern)
                )
            )

        # Sort
        if sort == "title":
            query = query.order_by(Task.title)
        elif sort == "updated":
            query = query.order_by(Task.updated_at.desc())
        elif sort == "priority":
            # High -> Medium -> Low
            from sqlalchemy import case
            priority_order = case(
                (Task.priority == "high", 1),
                (Task.priority == "medium", 2),
                (Task.priority == "low", 3),
                else_=4
            )
            query = query.order_by(priority_order)
        else:  # default: created
            query = query.order_by(Task.created_at.desc())

        # Pagination
        query = query.offset(skip).limit(limit)

        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_task(
        db: AsyncSession, user_id: str, task_id: int
    ) -> Optional[Task]:
        """
        Get a specific task by ID (with user isolation).

        Args:
            db: Database session
            user_id: User ID (enforces user isolation)
            task_id: Task ID

        Returns:
            Task object or None if not found
        """
        query = select(Task).where(
            and_(Task.id == task_id, Task.user_id == user_id)
        )
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @staticmethod
    async def update_task(
        db: AsyncSession, user_id: str, task_id: int, task_data: TaskUpdate
    ) -> Optional[Task]:
        """
        Update task details (title, description).

        Args:
            db: Database session
            user_id: User ID (enforces user isolation)
            task_id: Task ID
            task_data: Update data

        Returns:
            Updated task object or None if not found
        """
        task = await TaskService.get_task(db, user_id, task_id)

        if not task:
            return None

        # Update only provided fields
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.completed is not None:
            task.completed = task_data.completed
        if task_data.priority is not None:
            task.priority = task_data.priority
        if task_data.tags is not None:
            task.tags = task_data.tags
        if task_data.due_date is not None:
            # Convert timezone-aware datetime to naive datetime for PostgreSQL
            task.due_date = task_data.due_date.replace(tzinfo=None) if task_data.due_date.tzinfo else task_data.due_date
        if task_data.recurring is not None:
            task.recurring = task_data.recurring

        task.updated_at = datetime.utcnow()

        await db.commit()
        await db.refresh(task)

        return task

    @staticmethod
    async def delete_task(
        db: AsyncSession, user_id: str, task_id: int
    ) -> bool:
        """
        Delete a task.

        Args:
            db: Database session
            user_id: User ID (enforces user isolation)
            task_id: Task ID

        Returns:
            True if deleted, False if not found
        """
        task = await TaskService.get_task(db, user_id, task_id)

        if not task:
            return False

        await db.delete(task)
        await db.commit()

        return True

    @staticmethod
    async def toggle_complete(
        db: AsyncSession, user_id: str, task_id: int
    ) -> Optional[Task]:
        """
        Toggle task completion status.

        Args:
            db: Database session
            user_id: User ID (enforces user isolation)
            task_id: Task ID

        Returns:
            Updated task object or None if not found
        """
        task = await TaskService.get_task(db, user_id, task_id)

        if not task:
            return None

        task.completed = not task.completed
        task.updated_at = datetime.utcnow()

        await db.commit()
        await db.refresh(task)

        return task
