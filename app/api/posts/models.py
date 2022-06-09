from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..common.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    text = Column(String(20000), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    photo_url = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)
    tag = Column(String(30), nullable=True)

    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    user = relationship('User', back_populates='posts')

    location_id = Column(Integer, ForeignKey('location.id'), index=True, nullable=False)
    location = relationship('Location', back_populates='posts')
