#!/usr/bin/env python3
"""Reset database tables - drops and recreates all tables"""
import asyncio
from src.db.database import engine
from sqlmodel import SQLModel

# Import all models to register them
from src.models.user import User
from src.models.task import Task


async def reset_database():
    """Drop and recreate all database tables"""
    print("Dropping all tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    print("Creating all tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    print("✅ Database reset complete!")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(reset_database())
