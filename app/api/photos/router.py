from fastapi import APIRouter, Depends, status
from ..common.schemas import User
from ..common.token_auth import get_current_user
from .repository import Photo
from fastapi.responses import FileResponse


photo_router = APIRouter(
    prefix='/photo',
    tags=['photo'],
)


@photo_router.get('/{photo_url}')
def get_post(photo_url: str, current_user: User = Depends(get_current_user)):
    file_path = Photo.get_full_path(photo_url)
    return FileResponse(file_path, status_code=status.HTTP_200_OK)
