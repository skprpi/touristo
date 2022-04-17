from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
from ..common.db import get_db
from .models import Post
from sqlalchemy.orm import Session
from ..common.schemas import User
from ..common.token_auth import get_current_user

post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)


@post_router.post('')
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


