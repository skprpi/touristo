from . import schemas
from fastapi import APIRouter, Depends, UploadFile, File, status
from ..common.db import get_db
from .models import Post
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from ..common.token_auth import get_current_user
from .orm_wrap import PostORMWrap


post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)

post_orm_wrap = PostORMWrap(model_class=Post)


@post_router.post('/{location_id}', response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(location_id: int,
                request: schemas.CreatePost = Depends(schemas.CreatePost.as_form),
                photo: UploadFile = File(...),
                db: Session = Depends(get_db),
                current_user: CurrentUser = Depends(get_current_user)):
    return post_orm_wrap.create(location_id, request, photo, db, current_user)


@post_router.get('/{post_id}/comments/all', response_model=schemas.PostComments, status_code=status.HTTP_200_OK)
def get_post_comments(post_id: int,
                      db: Session = Depends(get_db),
                      current_user: CurrentUser = Depends(get_current_user)):
    return post_orm_wrap.get_by_id(post_id, db, current_user)


@post_router.get('/{post_id}', response_model=schemas.Post, status_code=status.HTTP_200_OK)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return post_orm_wrap.get_by_id(post_id, db, current_user)


@post_router.patch('/{post_id}', response_model=schemas.Post, status_code=status.HTTP_200_OK)
def update_post(post_id: int, request: schemas.PartialUpdatePost, db: Session = Depends(get_db),
                current_user: CurrentUser = Depends(get_current_user)):
    return post_orm_wrap.partial_update_by_id(post_id, request.dict(), db, current_user)
