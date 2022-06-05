from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from .credentials import CredentialsJWT
from pydantic import BaseModel
from ..common.schemas import CurrentUser
from sqlalchemy.orm import Session
from .db import get_db
from .orm_wrapper import SQLAlchemyWrap
from ..users.models import User

class TokenData(BaseModel):
    email: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=CredentialsJWT.JWT_TOKEN_URL)

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, CredentialsJWT.JWT_SECRET, algorithms=[CredentialsJWT.JWT_ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
        return token_data
    except JWTError:
        raise credentials_exception


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data: TokenData = verify_token(token, credentials_exception)
    instance = db.query(User).filter(User.email == token_data.email).first()
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User does not exist')
    return instance
