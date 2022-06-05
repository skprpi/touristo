from .credentials import Credentials
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..api.common.db import get_db
from ..main import fastapi_app

DATABASE_URL = Credentials.get_database_url()

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

fastapi_app.dependency_overrides[get_db] = override_get_db



