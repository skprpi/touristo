from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean
from sqlalchemy.orm import relationship
from ..common.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String(80), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    nickname = Column(String(30), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    photo = Column(Text, nullable=False)
    superuser = Column(Boolean, default=False, nullable=False)

    locations = relationship('Location', back_populates='user')
    posts = relationship('Post', back_populates='user')
