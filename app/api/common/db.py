from importlib.metadata import metadata
from .credentials import Credentials
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from sqlmodel import SQLModel
from fastapi import FastAPI
import databases, sqlalchemy


def get_db() -> databases.Database:
    return databases.Database(DATABASE_URL)



DATABASE_URL = Credentials.get_database_url()
database = get_db()
Base = declarative_base()
metadata = Base.metadata
# metadata = sqlalchemy.MetaData()

def startup_handler(app: FastAPI):
    async def startup():
        await database.connect()
    return startup


def shutdown_handler(app: FastAPI):
    async def shutdown():
        await database.disconnect()
    return shutdown

# async def init_db():
#     async with engine.begin() as connect:
#         await connect.run_sync(SQLModel.metadata.create_all)
