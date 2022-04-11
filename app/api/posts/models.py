import sqlalchemy
from ..common.db import Base
from datetime import datetime


# posts = sqlalchemy.Table(
#     'posts',
#     Data.Base.metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("text", sqlalchemy.Text),
#     sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.utcnow),
#     sqlalchemy.Column("photo", sqlalchemy.Text),
# )

class Posts(Base):

    __tablename__ = "posts"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True, index=True)
    text = sqlalchemy.Column(sqlalchemy.Text)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow)
    photo = sqlalchemy.Column(sqlalchemy.Text)


