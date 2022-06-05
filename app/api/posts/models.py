from  sqlalchemy import Column, Integer, Text, DateTime
from ..common.db import Base
from datetime import datetime


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    photo_url = Column(Text, nullable=False)
