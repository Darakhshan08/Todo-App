"""
FastAPI Backend for Full-Stack Todo Application
Phase 2 Implementation - Main Application Entry Point
"""
from contextlib import asynccontextmanager
from typing import AsyncGenerator
import traceback

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.db import init_db, close_db
import os


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager for startup and shutdown events."""
    # Startup: Initialize database
    print("Starting up FastAPI backend...")
    await init_db()
    print("Database initialized")
    yield
    # Shutdown: Close database connections
    print("Shutting down FastAPI backend...")
    await close_db()
    print("Database connections closed")


app = FastAPI(
    title="Todo Application API",
    description="Full-stack web application backend with JWT authentication and user isolation",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


# Global exception handler to catch all unhandled errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch all unhandled exceptions and log them"""
    print(f"\n{'='*80}")
    print(f"UNHANDLED EXCEPTION in {request.method} {request.url.path}")
    print(f"Exception Type: {type(exc).__name__}")
    print(f"Exception Message: {str(exc)}")
    print(f"Traceback:")
    traceback.print_exc()
    print(f"{'='*80}\n")

    return JSONResponse(
        status_code=500,
        content={
            "detail": f"Internal Server Error: {type(exc).__name__}: {str(exc)}",
            "type": type(exc).__name__,
            "message": str(exc)
        }
    )


# CORS configuration - Allow Next.js frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3000",
        "http://localhost:8080",  # For HTML test page
    ],
    allow_credentials=True,  # Allow credentials with specific origins
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    """Root endpoint - health check."""
    return {
        "message": "Todo Application API",
        "status": "operational",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint to verify the service is operational."""
    return {
        "status": "healthy",
        "service": "Todo Application API",
        "version": "1.0.0"
    }


# API routes registration
from src.api import auth_routes, task_routes
app.include_router(auth_routes.router)
app.include_router(task_routes.router)


