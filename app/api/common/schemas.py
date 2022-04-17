import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    nickname: str
    email: str
    hashed_password: str
    created_at: datetime.datetime
    photo: str

    class Config:
        orm_mode = True
    
    def __str__(self):
        return f'id {self.id}, email {self.email}'