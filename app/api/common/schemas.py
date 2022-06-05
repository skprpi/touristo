import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    nickname: str
    email: str
    created_at: datetime.datetime
    photo: str

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, email {self.email}'


class CurrentUser(User):
    superuser: bool

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, email {self.email}'
