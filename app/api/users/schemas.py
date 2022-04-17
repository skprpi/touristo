from pydantic import BaseModel


class CreateUser(BaseModel):
    nickname: str
    email: str
    password: str
    photo: str

    class Config:
        orm_mode = True
