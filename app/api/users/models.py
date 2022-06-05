from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean
from ..common.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String(80), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    nickname = Column(String(30), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    photo = Column(Text, nullable=False)
    superuser = Column(Boolean, default=False, nullable=False)
