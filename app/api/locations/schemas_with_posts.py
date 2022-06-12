from pydantic import BaseModel
from ..posts.schemas import PostWithoutLocation
from typing import List


class LocationPosts(BaseModel):
    posts: List[PostWithoutLocation]

    class Config:
        orm_mode = True
