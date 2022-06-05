import datetime
from pydantic import BaseModel


class CreateLocation(BaseModel):
    lat: float
    lng: float
    address: str
    title: str
    description: str
    location_type: str
    lighting_type: str
    visiting_type: str

    class Config:
        orm_mode = True

    def __str__(self):
        return f'title {self.title}'


class Location(CreateLocation):
    id: int
    created_at: datetime.datetime
    user_id: int

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, title {self.title}'
