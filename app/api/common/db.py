from .credentials import Credentials
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from sqlmodel import SQLModel

DATABASE_URL = Credentials.get_database_url()
engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
async_session = sessionmaker(bind=engine, echo=True, future=True)

async def get_db() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as connect:
        await connect.run_sync(SQLModel.metadata.create_all)
