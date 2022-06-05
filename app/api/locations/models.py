from sqlalchemy import Column, Integer, Text, DateTime, Float, ForeignKey
from ..common.db import Base
from datetime import datetime


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    address = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    location_type = Column(Text, nullable=False)
    lighting_type = Column(Text, nullable=False)
    visiting_type = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
