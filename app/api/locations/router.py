from . import schemas
from fastapi import APIRouter, Depends, status
from ..common.db import get_db
from .models import Location
from sqlalchemy.orm import Session
from ..common.orm_wrapper import SQLAlchemyWrap
from ..common.schemas import CurrentUser
from ..common.token_auth import get_current_user
from .repository import LocationRepository

location_router = APIRouter(
    prefix='/location',
    tags=['location'],
)

location_repository = LocationRepository()


@location_router.post('', response_model=schemas.Location, status_code=status.HTTP_201_CREATED)
def create_location(request: schemas.CreateLocation, db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user)):
    return location_repository.create(request, db, current_user)


@location_router.get('/{location_id}', response_model=schemas.Location, status_code=status.HTTP_200_OK)
def get_location(location_id: int, db: Session = Depends(get_db), current_user: CurrentUser = Depends(get_current_user)):
    return location_repository.get_by_id(location_id, db, current_user)

