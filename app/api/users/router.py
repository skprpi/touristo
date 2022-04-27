from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
from ..common.db import get_db
from .models import User
from sqlalchemy.orm import Session
from .hashing import Hasher
from fastapi.security import OAuth2PasswordRequestForm
from .token import create_access_token
from ..common.schemas import User as CommonUser


user_router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@user_router.post('', response_model=CommonUser)
def create_user(request: schemas.CreateUser, db: Session = Depends(get_db)):
    hashed_password = Hasher.bcrypt(request.password)
    fields = request.dict()
    del fields['password']

    new_user = User(**fields, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


login_router = APIRouter(
    prefix='/login',
    tags=['login'],
)

@login_router.post('')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Invalid credentials',
        )
    if not Hasher.verify(user.hashed_password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Invalid password',
        )
    
    # generate JWT token
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token,  'token_type': 'bearer'}
