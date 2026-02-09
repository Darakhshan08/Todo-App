"""
Automated tests for task management flows
Task: T079 [Phase 12] Critical user flow tests
"""
import pytest
from httpx import AsyncClient
from fastapi import status

# Test data
TEST_USER = {
    "email": "tasktest@example.com",
    "name": "Task Tester",
    "password": "TaskTest123!"
}

TEST_TASK = {
    "title": "Test Task",
    "description": "This is a test task",
    "priority": "high",
    "tags": ["test", "automated"]
}


@pytest.fixture
async def authenticated_client(client: AsyncClient):
    """Create authenticated client with user and token"""
    # Create user
    signup_response = await client.post("/api/auth/signup", json=TEST_USER)
    data = signup_response.json()

    token = data["token"]
    user_id = data["user"]["id"]

    # Add auth header to client
    client.headers["Authorization"] = f"Bearer {token}"

    return client, user_id


@pytest.mark.asyncio
async def test_create_task(authenticated_client):
    """Test task creation"""
    client, user_id = await authenticated_client

    response = await client.post(
        f"/api/{user_id}/tasks",
        json=TEST_TASK
    )

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    assert data["title"] == TEST_TASK["title"]
    assert data["description"] == TEST_TASK["description"]
    assert data["priority"] == TEST_TASK["priority"]
    assert data["tags"] == TEST_TASK["tags"]
    assert data["completed"] == False
    assert "id" in data


@pytest.mark.asyncio
async def test_get_tasks(authenticated_client):
    """Test listing tasks"""
    client, user_id = await authenticated_client

    # Create a task
    await client.post(f"/api/{user_id}/tasks", json=TEST_TASK)

    # Get tasks
    response = await client.get(f"/api/{user_id}/tasks")

    assert response.status_code == status.HTTP_200_OK
    tasks = response.json()

    assert len(tasks) > 0
    assert tasks[0]["title"] == TEST_TASK["title"]


@pytest.mark.asyncio
async def test_update_task(authenticated_client):
    """Test updating task"""
    client, user_id = await authenticated_client

    # Create task
    create_response = await client.post(f"/api/{user_id}/tasks", json=TEST_TASK)
    task_id = create_response.json()["id"]

    # Update task
    updated_data = {
        "title": "Updated Task",
        "priority": "low"
    }

    response = await client.put(
        f"/api/{user_id}/tasks/{task_id}",
        json=updated_data
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["title"] == "Updated Task"
    assert data["priority"] == "low"


@pytest.mark.asyncio
async def test_complete_task(authenticated_client):
    """Test marking task as complete"""
    client, user_id = await authenticated_client

    # Create task
    create_response = await client.post(f"/api/{user_id}/tasks", json=TEST_TASK)
    task_id = create_response.json()["id"]

    # Mark complete
    response = await client.patch(f"/api/{user_id}/tasks/{task_id}/complete")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["completed"] == True


@pytest.mark.asyncio
async def test_delete_task(authenticated_client):
    """Test deleting task"""
    client, user_id = await authenticated_client

    # Create task
    create_response = await client.post(f"/api/{user_id}/tasks", json=TEST_TASK)
    task_id = create_response.json()["id"]

    # Delete task
    response = await client.delete(f"/api/{user_id}/tasks/{task_id}")

    assert response.status_code == status.HTTP_200_OK

    # Verify task is deleted
    get_response = await client.get(f"/api/{user_id}/tasks")
    tasks = get_response.json()

    task_ids = [task["id"] for task in tasks]
    assert task_id not in task_ids


@pytest.mark.asyncio
async def test_user_isolation(client: AsyncClient):
    """Test that users can only see their own tasks"""
    # Create user 1
    user1_response = await client.post("/api/auth/signup", json={
        "email": "user1@example.com",
        "name": "User 1",
        "password": "Password123!"
    })
    user1_data = user1_response.json()
    user1_id = user1_data["user"]["id"]
    user1_token = user1_data["token"]

    # Create user 2
    user2_response = await client.post("/api/auth/signup", json={
        "email": "user2@example.com",
        "name": "User 2",
        "password": "Password123!"
    })
    user2_data = user2_response.json()
    user2_id = user2_data["user"]["id"]
    user2_token = user2_data["token"]

    # User 1 creates a task
    client.headers["Authorization"] = f"Bearer {user1_token}"
    await client.post(f"/api/{user1_id}/tasks", json=TEST_TASK)

    # User 2 tries to access User 1's tasks
    client.headers["Authorization"] = f"Bearer {user2_token}"
    response = await client.get(f"/api/{user1_id}/tasks")

    # Should be forbidden
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_search_filter_tasks(authenticated_client):
    """Test search and filter functionality"""
    client, user_id = await authenticated_client

    # Create multiple tasks
    tasks_to_create = [
        {"title": "Work Task", "priority": "high", "tags": ["work"]},
        {"title": "Home Task", "priority": "low", "tags": ["home"]},
        {"title": "Urgent Work", "priority": "high", "tags": ["work", "urgent"]},
    ]

    for task_data in tasks_to_create:
        await client.post(f"/api/{user_id}/tasks", json=task_data)

    # Search by keyword
    response = await client.get(f"/api/{user_id}/tasks?search=Work")
    tasks = response.json()
    assert len(tasks) == 2

    # Filter by priority
    response = await client.get(f"/api/{user_id}/tasks?priority=high")
    tasks = response.json()
    assert len(tasks) == 2

    # Filter by tag
    response = await client.get(f"/api/{user_id}/tasks?tag=urgent")
    tasks = response.json()
    assert len(tasks) == 1
    assert "urgent" in tasks[0]["tags"]


@pytest.mark.asyncio
async def test_unauthorized_access(client: AsyncClient):
    """Test that endpoints require authentication"""
    # Try to access without token
    response = await client.get("/api/some-user-id/tasks")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
