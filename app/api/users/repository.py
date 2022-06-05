from app.api.common.decorators import superuser
from . import schemas
from .hashing import Hasher
from sqlalchemy.orm import Session
from ..common.orm_wrapper import SQLAlchemyWrap
from .models import User





class UserRepository:
    def __init__(self):
        self.orm_wrap = SQLAlchemyWrap(model_class=User)
    
    def get_by_id(self, user_id, db: Session, current_user):
        return self.orm_wrap.get_by_id(user_id, db, current_user)

    def create(self, request: schemas.CreateUser, db: Session):
        fields = self._form_dict_create_user(request)
        return self.orm_wrap.create(fields, db, None)

    # Inner logic

    def _form_dict_create_user(self, request: schemas.CreateUser):
        hashed_password = Hasher.bcrypt(request.password)
        fields = request.dict()
        del fields['password']
        fields['hashed_password'] = hashed_password
        return fields

