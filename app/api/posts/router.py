from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
from ..common.db import get_db
from .models import Post
from sqlalchemy.orm import Session

post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)


@post_router.post('')
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


