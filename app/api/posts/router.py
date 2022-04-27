from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, File
from ..common.db import get_db
from .models import Post
from sqlalchemy.orm import Session
from ..common.schemas import User
from ..common.token_auth import get_current_user
import shutil
import uuid
import sys

post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)


@post_router.post('')
def create_post(request: schemas.CreatePost = Depends(schemas.CreatePost.as_form), photo: UploadFile = File(...), db: Session = Depends(get_db)):
    photo_file_name = str(uuid.uuid4())
    with open(f'app/staticfile/{photo_file_name}', 'wb') as buffer:
        shutil.copyfileobj(photo.file, buffer)
    new_post = Post(**request.dict(), photo_url = photo_file_name)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# @post_router.get('/all', response_model=schemas.Post)
# def get_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No posts with id {post_id}')
#     return post


@post_router.get('/{post_id}', response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No posts with id {post_id}')
    return post



