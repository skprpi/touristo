from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .schemas import CurrentUser
from ..common.decorators import superuser

class SQLAlchemyWrap:

    def __init__(self, model_class):
        self.model_class = model_class

    def get_by_id(self, id: int, db: Session, current_user: (CurrentUser | None)):
        instance = db.query(self.model_class).filter(self.model_class.id == id).first()
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f'No {self.model_class.__name__} with id {id}')
        return instance

    def create(self, request_field_dict: dict, db, current_user: (CurrentUser | None)):
        new_instance = self.model_class(**request_field_dict)
        db.add(new_instance)
        db.commit()
        db.refresh(new_instance)
        return new_instance
