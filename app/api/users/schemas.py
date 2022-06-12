from pydantic import BaseModel
from fastapi import Form


class CreateUser(BaseModel):
    nickname: str
    email: str
    password: str

    class Config:
        orm_mode = True

    @classmethod
    def as_form(cls, nickname: str = Form(...), email: str = Form(...), password: str = Form(...)) -> 'CreateUser':
        return cls(nickname=nickname, email=email, password=password)
