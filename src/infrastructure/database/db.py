from sqlalchemy.ext import asyncio
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engine: asyncio.AsyncEngine = asyncio.create_async_engine(
    settings.url,
)

new_session = asyncio.async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db_session():
    async with new_session() as session:
        yield session


class Base(DeclarativeBase):
    pass
