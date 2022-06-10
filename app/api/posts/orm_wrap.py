from ..common.orm_wrapper import SQLAlchemyWrap
from . import schemas
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from fastapi import UploadFile
from ..locations.router import location_orm
from ..photos.repository import Photo


class PostORMWrap(SQLAlchemyWrap):
    def __init__(self, model_class):
        super().__init__(model_class)

    def create(self, location_id: int, request: schemas.CreatePost, photo: UploadFile,
               db: Session, current_user: CurrentUser):
        fields = self._form_dict_create_post_file_name(request, photo)
        fields['user_id'] = current_user.id
        fields['user'] = current_user
        location = location_orm.get_by_id(location_id, db, current_user)
        fields['location_id'] = location_id
        fields['location'] = location
        return super().create(fields, db, current_user)

    def _form_dict_create_post_file_name(self, request: schemas.CreatePost, photo: UploadFile):
        photo_file_name = Photo.create(photo)
        fields = request.dict()
        fields['photo_url'] = photo_file_name
        return fields
