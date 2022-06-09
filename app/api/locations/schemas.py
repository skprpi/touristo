import datetime
from pydantic import BaseModel
from typing import Optional
from ..common.schemas import CurrentUser


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


class PartialUpdateLocation(BaseModel):
    lat: Optional[float] = None
    lng: Optional[float] = None
    address: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    location_type: Optional[str] = None
    lighting_type: Optional[str] = None
    visiting_type: Optional[str] = None

    class Config:
        orm_mode = True

    def __str__(self):
        return f'title {self.title}'


class Location(CreateLocation):
    id: int
    created_at: datetime.datetime
    user_id: int
    user: CurrentUser

    class Config:
        orm_mode = True

    def __str__(self):
        return f'id {self.id}, title {self.title}'
