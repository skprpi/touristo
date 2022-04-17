from sys import maxsize
from  sqlalchemy import Column, Integer, Text, DateTime, String
from ..common.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String(80))
    hashed_password = Column(Text)
    nickname = Column(String(30), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    photo = Column(Text)
