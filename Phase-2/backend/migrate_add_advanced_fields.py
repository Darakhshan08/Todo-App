"""
Migration: Add due_date and recurring fields to tasks table
"""
import asyncio
import os
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://neondb_owner:npg_qtVWPar34Osk@ep-round-sound-a1p5ziix-pooler.ap-southeast-1.aws.neon.tech/neondb?ssl=require"
)

async def migrate():
    engine = create_async_engine(DATABASE_URL)

    async with engine.begin() as conn:
        print("Starting migration to add advanced fields...")

        # Add due_date column
        print("1. Adding due_date column...")
        await conn.execute(text("""
            ALTER TABLE tasks
            ADD COLUMN IF NOT EXISTS due_date TIMESTAMP
        """))

        # Add recurring column
        print("2. Adding recurring column...")
        await conn.execute(text("""
            ALTER TABLE tasks
            ADD COLUMN IF NOT EXISTS recurring VARCHAR(20)
        """))

        print("Migration completed successfully!")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(migrate())
