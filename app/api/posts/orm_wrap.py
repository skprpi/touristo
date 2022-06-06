from ..common.orm_wrapper import SQLAlchemyWrap
from . import schemas
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from fastapi import UploadFile
import shutil
import uuid


class PostORMWrap(SQLAlchemyWrap):
    def __init__(self, model_class):
        super().__init__(model_class)

    def create(self, request: schemas.CreatePost, photo: UploadFile, db: Session, current_user: CurrentUser):
        fields, photo_file_name = self._form_dict_create_post_file_name(request)
        self._create_photo_file(photo_file_name, photo)
        return super().create(fields, db, current_user)

    def _generate_image_file_name(self):
        return str(uuid.uuid4())

    def _create_photo_file(self, photo_file_name: str, photo: UploadFile):
        with open(f'app/staticfile/{photo_file_name}', 'wb') as buffer:
            shutil.copyfileobj(photo.file, buffer)

    def _form_dict_create_post_file_name(self, request: schemas.CreatePost):
        photo_file_name = self._generate_image_file_name()
        fields = request.dict()
        fields['photo_url'] = photo_file_name
        return fields, photo_file_name
