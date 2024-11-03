from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.db import Base, engine
from app.models.product import Product

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)