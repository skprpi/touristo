from . import schemas
from fastapi import APIRouter, Depends, status
from ..common.db import get_db
from .models import Comment
from .orm_wrap import CommentORMWrap
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from ..common.token_auth import get_current_user


comment_router = APIRouter(
    prefix='/comment',
    tags=['comment'],
)
comment_orm_wrap = CommentORMWrap(Comment)


@comment_router.post('/{post_id}', response_model=schemas.Comment, status_code=status.HTTP_201_CREATED)
def create_comment(post_id: int, request: schemas.CreateComment, db: Session = Depends(get_db),
                   current_user: CurrentUser = Depends(get_current_user)):
    return comment_orm_wrap.create(post_id, request, db, current_user)


@comment_router.get('/{comment_id}', response_model=schemas.Comment, status_code=status.HTTP_200_OK)
def get_comment(comment_id: int, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return comment_orm_wrap.get_by_id(comment_id, db, current_user)


@comment_router.patch('/{comment_id}', response_model=schemas.Comment, status_code=status.HTTP_200_OK)
def update_comment(comment_id: int, request: schemas.CommentPartialUpdate, db: Session = Depends(get_db),
                   current_user: CurrentUser = Depends(get_current_user)):
    return comment_orm_wrap.partial_update_by_id(comment_id, request.dict(), db, current_user)
