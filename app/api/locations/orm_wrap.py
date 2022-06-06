from app.api.common.orm_wrapper import SQLAlchemyWrap
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from . import schemas


class LocationORMWrap(SQLAlchemyWrap):
    def __init__(self, model_class):
        super().__init__(model_class)

    def create(self, request: schemas.CreateLocation, db: Session, current_user: CurrentUser):
        fields = request.dict()
        fields['user_id'] = current_user.id
        return super().create(fields, db, current_user)
