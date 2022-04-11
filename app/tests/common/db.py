from .credentials import Credentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
import pytest

DATABASE_URL = Credentials.get_database_url()
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(bind=engine, echo=True, future=True)

@pytest.fixture(autouse=True)
async def override_get_db() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as connect:
        await connect.run_sync(SQLModel.metadata.drop_all)
        await connect.run_sync(SQLModel.metadata.create_all)
