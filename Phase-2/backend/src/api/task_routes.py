"""
Task Management Routes - RESTful API Endpoints
Tasks: T023, T029, T035, T041, T046 [US1-US5] Task endpoints
"""
from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_db
from src.models.task import Task, TaskCreate, TaskUpdate, TaskPublic
from src.services.task_service import TaskService
from src.middleware.auth_middleware import get_current_user, enforce_user_isolation
from typing import List, Optional
from pydantic import BaseModel
import time

router = APIRouter(prefix="/api/{user_id}/tasks", tags=["tasks"])


class TaskCompleteResponse(BaseModel):
    """Response model for task completion toggle"""
    task_id: int
    completed: bool
    title: str


class TaskDeleteResponse(BaseModel):
    """Response model for task deletion"""
    status: str
    task_id: int


@router.post("", response_model=TaskPublic, status_code=status.HTTP_201_CREATED)
async def create_task(
    user_id: str,
    task_data: TaskCreate,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new task.
    Task: T023 [US1] with validation per plan.md L92-93

    Args:
        user_id: User ID from URL path
        task_data: Task creation data (title, description)
        current_user: Authenticated user from JWT
        db: Database session

    Returns:
        Created task object

    Raises:
        HTTPException: If user_id doesn't match authenticated user or validation fails
    """
    # Start performance monitoring - T028a
    start_time = time.time()

    # Enforce user isolation per constitution L23-25
    enforce_user_isolation(user_id, current_user)

    # Create task
    try:
        print(f"[DEBUG] Creating task for user {user_id}")
        print(f"[DEBUG] Task data: {task_data}")
        task = await TaskService.create_task(db, user_id, task_data)
        print(f"[DEBUG] Task created successfully: {task.id}")
    except Exception as e:
        print(f"[ERROR] Task creation failed: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        raise

    # Log performance metrics - T028a
    elapsed_time = time.time() - start_time
    print(f"[PERF] Task creation took {elapsed_time:.3f}s for user {user_id}")

    return task


@router.get("", response_model=List[TaskPublic])
async def get_tasks(
    user_id: str,
    status_filter: Optional[str] = Query("all", alias="status", description="Filter by status: all, pending, completed"),
    priority: Optional[str] = Query(None, description="Filter by priority: high, medium, low"),
    tag: Optional[str] = Query(None, description="Filter by tag (e.g., work, home)"),
    search: Optional[str] = Query(None, description="Search keyword in title or description"),
    sort: Optional[str] = Query("created", description="Sort by: created, title, updated, priority"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all tasks for a user with query params.
    Task: T029 [US2], T056 [US6], T057 [US7] with query params (status, priority, tag, search, sort) per plan.md L89-90

    Args:
        user_id: User ID from URL path
        status_filter: Filter by status (all, pending, completed)
        priority: Filter by priority (high, medium, low)
        tag: Filter by tag
        search: Search keyword in title or description
        sort: Sort field (created, title, updated, priority)
        skip: Pagination offset
        limit: Pagination limit
        current_user: Authenticated user from JWT
        db: Database session

    Returns:
        List of task objects

    Raises:
        HTTPException: If user_id doesn't match authenticated user
    """
    # Enforce user isolation
    enforce_user_isolation(user_id, current_user)

    # Get tasks with filters and search
    tasks = await TaskService.get_tasks(
        db, user_id, status=status_filter, priority=priority, tag=tag, search=search, sort=sort, skip=skip, limit=limit
    )

    return tasks


@router.get("/{id}", response_model=TaskPublic)
async def get_task(
    user_id: str,
    id: int,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific task by ID.

    Args:
        user_id: User ID from URL path
        id: Task ID
        current_user: Authenticated user from JWT
        db: Database session

    Returns:
        Task object

    Raises:
        HTTPException: If task not found or access forbidden
    """
    # Enforce user isolation
    enforce_user_isolation(user_id, current_user)

    # Get task
    task = await TaskService.get_task(db, user_id, id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.put("/{id}", response_model=TaskPublic)
async def update_task(
    user_id: str,
    id: int,
    task_data: TaskUpdate,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update task details (title, description).
    Task: T035 [US3]

    Args:
        user_id: User ID from URL path
        id: Task ID
        task_data: Update data
        current_user: Authenticated user from JWT
        db: Database session

    Returns:
        Updated task object

    Raises:
        HTTPException: If task not found or access forbidden
    """
    # Enforce user isolation
    enforce_user_isolation(user_id, current_user)

    # Update task
    task = await TaskService.update_task(db, user_id, id, task_data)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.delete("/{id}", response_model=TaskDeleteResponse)
async def delete_task(
    user_id: str,
    id: int,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a task.
    Task: T041 [US4]

    Args:
        user_id: User ID from URL path
        id: Task ID
        current_user: Authenticated user from JWT
        db: Database session

    Returns:
        Success response with task_id

    Raises:
        HTTPException: If task not found or access forbidden
    """
    # Enforce user isolation
    enforce_user_isolation(user_id, current_user)

    # Delete task
    success = await TaskService.delete_task(db, user_id, id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return TaskDeleteResponse(status="deleted", task_id=id)


@router.patch("/{id}/complete", response_model=TaskCompleteResponse)
async def toggle_task_complete(
    user_id: str,
    id: int,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Toggle task completion status.
    Task: T046 [US5]

    Args:
        user_id: User ID from URL path
        id: Task ID
        current_user: Authenticated user from JWT
        db: Database session

    Returns:
        Task completion status

    Raises:
        HTTPException: If task not found or access forbidden
    """
    # Enforce user isolation
    enforce_user_isolation(user_id, current_user)

    # Toggle completion
    task = await TaskService.toggle_complete(db, user_id, id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return TaskCompleteResponse(
        task_id=task.id,
        completed=task.completed,
        title=task.title
    )

