from . import schemas
from . import schemas_with_posts
from fastapi import APIRouter, Depends, status
from ..common.db import get_db
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from ..common.token_auth import get_current_user
from .orm_wrap import LocationORMWrap
from .models import Location


location_router = APIRouter(
    prefix='/location',
    tags=['location'],
)


location_orm = LocationORMWrap(Location)


@location_router.post('', response_model=schemas.Location, status_code=status.HTTP_201_CREATED)
def create_location(request: schemas.CreateLocation,
                    db: Session = Depends(get_db),
                    current_user: CurrentUser = Depends(get_current_user)):
    return location_orm.create(request, db, current_user)


@location_router.get('/{location_id}/posts/all', response_model=schemas_with_posts.LocationPosts,
                     status_code=status.HTTP_200_OK)
def get_location_posts(location_id: int,
                       db: Session = Depends(get_db),
                       current_user: CurrentUser = Depends(get_current_user)):
    return location_orm.get_by_id(location_id, db, current_user)


@location_router.get('/{location_id}', response_model=schemas.Location, status_code=status.HTTP_200_OK)
def get_location(location_id: int,
                 db: Session = Depends(get_db),
                 current_user: CurrentUser = Depends(get_current_user)):
    return location_orm.get_by_id(location_id, db, current_user)


@location_router.patch('/{location_id}', response_model=schemas.Location, status_code=status.HTTP_200_OK)
def update_location(location_id: int,
                    request: schemas.PartialUpdateLocation,
                    db: Session = Depends(get_db),
                    current_user: CurrentUser = Depends(get_current_user)):
    return location_orm.partial_update_by_id(location_id, request.dict(), db, current_user)
