import datetime
from pydantic import BaseModel
from fastapi import Form


class Post(BaseModel):
    id: int
    text: str
    created_at: datetime.datetime
    photo_url: str

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, text {self.text}'


class CreatePost(BaseModel):
    text: str

    class Config:
        orm_mode = True

    @classmethod
    def as_form(cls, text: str = Form(...)) -> 'CreatePost':
        return cls(text=text)
