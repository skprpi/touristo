from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateComment(BaseModel):
    text: str

    class Config:
        orm_mode = True

    def __str__(self):
        return f'text {self.text}'


class Comment(CreateComment):
    id: int
    user_id: int
    post_id: int
    created_at: datetime

    class Config:
        orm_mode = True

    def __str__(self):
        return f'text {self.text}'


class CommentPartialUpdate(BaseModel):
    text: Optional[str]

    class Config:
        orm_mode = True

    def __str__(self):
        return f'text {self.text}'
