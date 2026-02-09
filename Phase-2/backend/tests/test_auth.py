"""
Automated tests for authentication flows
Task: T079 [Phase 12] Critical user flow tests
"""
import pytest
from httpx import AsyncClient
from fastapi import status

# Test data
TEST_USER = {
    "email": "test@example.com",
    "name": "Test User",
    "password": "TestPassword123!"
}

@pytest.mark.asyncio
async def test_user_signup(client: AsyncClient):
    """Test user registration flow"""
    response = await client.post(
        "/api/auth/signup",
        json=TEST_USER
    )

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    # Verify response structure
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == TEST_USER["email"]
    assert data["user"]["name"] == TEST_USER["name"]
    assert "id" in data["user"]

    # Verify password is not in response
    assert "password" not in data["user"]
    assert "password_hash" not in data["user"]


@pytest.mark.asyncio
async def test_user_signup_duplicate_email(client: AsyncClient):
    """Test signup with existing email fails"""
    # First signup
    await client.post("/api/auth/signup", json=TEST_USER)

    # Duplicate signup
    response = await client.post("/api/auth/signup", json=TEST_USER)

    assert response.status_code == status.HTTP_409_CONFLICT


@pytest.mark.asyncio
async def test_user_login(client: AsyncClient):
    """Test user login flow"""
    # First create user
    await client.post("/api/auth/signup", json=TEST_USER)

    # Login
    response = await client.post(
        "/api/auth/login",
        json={
            "email": TEST_USER["email"],
            "password": TEST_USER["password"]
        }
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "token" in data
    assert "user" in data


@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient):
    """Test login with wrong password fails"""
    # Create user
    await client.post("/api/auth/signup", json=TEST_USER)

    # Login with wrong password
    response = await client.post(
        "/api/auth/login",
        json={
            "email": TEST_USER["email"],
            "password": "WrongPassword123!"
        }
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_login_nonexistent_user(client: AsyncClient):
    """Test login with non-existent user fails"""
    response = await client.post(
        "/api/auth/login",
        json={
            "email": "nonexistent@example.com",
            "password": "SomePassword123!"
        }
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
