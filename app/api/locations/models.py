from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..common.db import Base
from datetime import datetime


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    address = Column(String(200), nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    location_type = Column(String(30), nullable=False)
    lighting_type = Column(String(30), nullable=False)
    visiting_type = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    user = relationship('User', back_populates='locations')
    posts = relationship('Post', back_populates='location')
