from datetime import datetime, timedelta
from jose import jwt
from ..common.credentials import CredentialsJWT


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=CredentialsJWT.JWT_EXPIRES_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, CredentialsJWT.JWT_SECRET, algorithm=CredentialsJWT.JWT_ALGORITHM)
    return encoded_jwt
