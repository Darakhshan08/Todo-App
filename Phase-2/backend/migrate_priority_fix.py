"""
Migration script to fix priority field type mismatch
Drops the ENUM type and recreates priority as VARCHAR
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
        print("Starting migration...")

        # Step 1: Drop tasks table (will cascade drop the FK constraint)
        print("1. Dropping tasks table...")
        await conn.execute(text("DROP TABLE IF EXISTS tasks CASCADE"))

        # Step 2: Drop the ENUM type
        print("2. Dropping priority ENUM type...")
        await conn.execute(text("DROP TYPE IF EXISTS priority CASCADE"))

        # Step 3: Recreate tasks table with VARCHAR priority
        print("3. Creating tasks table with VARCHAR priority...")
        await conn.execute(text("""
            CREATE TABLE tasks (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR NOT NULL REFERENCES users(id),
                title VARCHAR(200) NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL DEFAULT FALSE,
                priority VARCHAR(20) NOT NULL DEFAULT 'medium',
                tags JSON NOT NULL DEFAULT '[]',
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        """))

        # Step 4: Create index on user_id for performance
        print("4. Creating index on user_id...")
        await conn.execute(text("CREATE INDEX idx_tasks_user_id ON tasks(user_id)"))

        print("Migration completed successfully!")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(migrate())
