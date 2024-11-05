from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

async def commit_and_refresh(db: AsyncSession, db_object):
    try:
        db.add(db_object)
        await db.commit()
        await db.refresh(db_object)
    except SQLAlchemyError as e:
        await db.rollback()
        raise e