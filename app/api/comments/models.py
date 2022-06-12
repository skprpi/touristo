from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..common.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), index=True, nullable=False)
    post = relationship('Post', back_populates='comments')
    text = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
