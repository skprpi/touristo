import datetime
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    text: str
    created_at: datetime.datetime
    photo: str

    class Config:
        orm_mode = True
    
    def __str__(self):
        return f'id {self.id}, text {self.text}'


class CreatePost(BaseModel):
    text: str
    photo: str

    class Config:
        orm_mode = True
