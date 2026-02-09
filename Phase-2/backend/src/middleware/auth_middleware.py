"""
JWT Authentication Middleware for FastAPI
Verifies Better Auth JWT tokens and enforces user isolation
"""
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from typing import Optional
import os

# Security configuration
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "your-secret-key-change-in-production")
ALGORITHM = "HS256"

security = HTTPBearer()


async def verify_jwt_token(
    credentials: HTTPAuthorizationCredentials = Security(security)
) -> dict:
    """
    Verify JWT token from Authorization header.

    Args:
        credentials: HTTP Bearer token from Authorization header

    Returns:
        dict: Decoded token payload with user information

    Raises:
        HTTPException: If token is invalid or missing
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: Optional[str] = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {
            "user_id": user_id,
            "email": payload.get("email"),
            "name": payload.get("name"),
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security)
) -> dict:
    """
    Dependency to get current authenticated user.
    Enforces JWT authentication on all protected endpoints.

    Usage:
        @app.get("/api/{user_id}/tasks")
        async def get_tasks(
            user_id: str,
            current_user: dict = Depends(get_current_user)
        ):
            # Verify user_id matches authenticated user
            if current_user["user_id"] != user_id:
                raise HTTPException(status_code=403, detail="Access forbidden")
            ...
    """
    return await verify_jwt_token(credentials)


def enforce_user_isolation(user_id: str, current_user: dict) -> None:
    """
    Enforce user isolation by verifying user_id in URL matches authenticated user.

    Args:
        user_id: User ID from URL path parameter
        current_user: Authenticated user from JWT token

    Raises:
        HTTPException: If user_id doesn't match authenticated user
    """
    if current_user["user_id"] != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Cannot access another user's data"
        )
