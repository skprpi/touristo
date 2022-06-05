from app.api.common.orm_wrapper import SQLAlchemyWrap
from sqlalchemy.orm import Session
from .models import Location
from ..common.schemas import CurrentUser
from . import schemas


class LocationRepository:
    def __init__(self):
        self.orm_wrap = SQLAlchemyWrap(model_class=Location)

    def get_by_id(self, location_id, db: Session, current_user: CurrentUser):
        return self.orm_wrap.get_by_id(location_id, db, current_user)

    def create(self, request: schemas.CreateLocation, db: Session, current_user: CurrentUser):
        fields = request.dict()
        fields['user_id'] = current_user.id
        return self.orm_wrap.create(fields, db, current_user)
