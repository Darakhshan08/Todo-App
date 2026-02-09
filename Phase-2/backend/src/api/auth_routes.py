"""
Authentication Routes - Better Auth Integration
Task: T022 [US1] Authentication routes per plan.md
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from src.models.user import User, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.db.database import get_db
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
import os

router = APIRouter(prefix="/api/auth", tags=["authentication"])

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Configuration
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days


class SignupRequest(BaseModel):
    """Request model for user signup"""
    email: EmailStr
    password: str
    name: str


class LoginRequest(BaseModel):
    """Request model for user login"""
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    """Response model for authentication"""
    token: str
    user: dict


def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """Create JWT access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/signup", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def signup(request: SignupRequest, db: AsyncSession = Depends(get_db)):
    """
    User registration endpoint.

    Creates a new user account and returns JWT token.

    Args:
        request: Signup data (email, password, name)
        db: Database session

    Returns:
        AuthResponse with JWT token and user data

    Raises:
        HTTPException: If email already exists
    """
    from sqlalchemy import select

    # Check if user already exists
    result = await db.execute(select(User).where(User.email == request.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    import uuid
    from datetime import datetime

    hashed_password = hash_password(request.password)

    new_user = User(
        id=str(uuid.uuid4()),  # Explicitly generate UUID
        email=request.email,
        name=request.name,
        password_hash=hashed_password,
        created_at=datetime.utcnow()  # Explicitly set timestamp
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # Create JWT token
    access_token = create_access_token(
        data={
            "sub": new_user.id,
            "email": new_user.email,
            "name": new_user.name
        }
    )

    return AuthResponse(
        token=access_token,
        user={
            "id": new_user.id,
            "email": new_user.email,
            "name": new_user.name
        }
    )


@router.post("/login", response_model=AuthResponse)
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    """
    User login endpoint.

    Authenticates user and returns JWT token.

    Args:
        request: Login data (email, password)
        db: Database session

    Returns:
        AuthResponse with JWT token and user data

    Raises:
        HTTPException: If credentials are invalid
    """
    from sqlalchemy import select

    # Find user by email
    result = await db.execute(select(User).where(User.email == request.email))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create JWT token
    access_token = create_access_token(
        data={
            "sub": user.id,
            "email": user.email,
            "name": user.name
        }
    )

    return AuthResponse(
        token=access_token,
        user={
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    )


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout():
    """
    User logout endpoint.

    Note: Since we're using stateless JWT tokens, logout is handled client-side
    by removing the token from storage. This endpoint exists for API completeness.

    Returns:
        Success message
    """
    return {"message": "Logged out successfully"}
