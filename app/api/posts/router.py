from . import schemas
from fastapi import APIRouter, Depends, UploadFile, File
from ..common.db import get_db
from .models import Post
from sqlalchemy.orm import Session
from ..common.schemas import User
from ..common.token_auth import get_current_user
from . repository import form_dict_create_post_file_name, create_photo_file
from ..common.orm_wrapper import SQLAlchemyWrap


post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)

post_orm_wrap = SQLAlchemyWrap(model_class=Post)


@post_router.post('')
def create_post(request: schemas.CreatePost = Depends(schemas.CreatePost.as_form),
                photo: UploadFile = File(...),
                db: Session = Depends(get_db)):
    fields, photo_file_name = form_dict_create_post_file_name(request)
    create_photo_file(photo_file_name, photo)
    return post_orm_wrap.create(fields, db, None)


@post_router.get('/{post_id}', response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return post_orm_wrap.get_by_id(post_id, db, None)
