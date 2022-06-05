from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
from ..common.db import get_db
from .models import User
from sqlalchemy.orm import Session
from .hashing import Hasher
from fastapi.security import OAuth2PasswordRequestForm
from .token import create_access_token
from ..common.schemas import User as CommonUser
from ..common.token_auth import get_current_user
from . repository import UserRepository


user_router = APIRouter(
    prefix='/user',
    tags=['user'],
)


user_repository = UserRepository()


@user_router.post('', response_model=CommonUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.CreateUser, db: Session = Depends(get_db)):
    return user_repository.create(request, db)


@user_router.get('/{user_id}', response_model=CommonUser, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_repository.get_by_id(user_id, db, current_user)


login_router = APIRouter(
    prefix='/login',
    tags=['login'],
)


@login_router.post('', status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid credentials',
        )
    if not Hasher.verify(user.hashed_password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid password',
        )
    # generate JWT token
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token,  'token_type': 'Bearer'}
