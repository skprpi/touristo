from . import schemas
from .hashing import Hasher
from sqlalchemy.orm import Session
from ..common.orm_wrapper import SQLAlchemyWrap
from .models import User
from ..photos.repository import Photo
from fastapi import UploadFile


class UserRepository:
    def __init__(self):
        self.orm_wrap = SQLAlchemyWrap(model_class=User)

    def get_by_id(self, user_id, db: Session, current_user):
        return self.orm_wrap.get_by_id(user_id, db, current_user)

    def create(self, request: schemas.CreateUser, photo: UploadFile, db: Session):
        fields = self._form_dict_create_user(request, photo)
        return self.orm_wrap.create(fields, db, None)

    # Inner logic

    def _form_dict_create_user(self, request: schemas.CreateUser, photo: UploadFile):
        hashed_password = Hasher.bcrypt(request.password)
        fields = request.dict()
        del fields['password']
        fields['hashed_password'] = hashed_password
        photo_file_name = Photo.create(photo)
        fields['photo_url'] = photo_file_name
        return fields
