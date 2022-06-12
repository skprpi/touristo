import datetime
from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional

from ..common.schemas import CurrentUser
from ..locations.schemas import Location
from ..comments.schemas import Comment


class PostComments(BaseModel):
    comments: List[Comment]

    class Config:
        orm_mode = True

    def __str__(self):
        return 'Not implemented'


class PostWithoutLocation(BaseModel):
    id: int
    text: str
    created_at: datetime.datetime
    photo_url: str
    price: int
    tag: str
    user: CurrentUser

    class Config:
        orm_mode = True


class Post(PostWithoutLocation):
    location: Location

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, text {self.text}'


class PartialUpdatePost(BaseModel):
    price: Optional[int]
    tag: Optional[str]
    text: Optional[str]

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, text {self.text}'


class CreatePost(BaseModel):
    price: str
    tag: str
    text: str

    class Config:
        orm_mode = True

    @classmethod
    def as_form(cls, text: str = Form(...), price: int = Form(...), tag: str = Form(...)) -> 'CreatePost':
        return cls(text=text, price=price, tag=tag)
