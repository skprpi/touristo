from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .schemas import CurrentUser


class SQLAlchemyWrap:
    def __init__(self, model_class):
        self.model_class = model_class

    def get_by_id(self, id: int, db: Session, current_user: (CurrentUser | None)):
        instance = db.query(self.model_class).filter(self.model_class.id == id).one_or_none()
        if instance is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No {self.model_class.__name__} with id {id}')
        return instance

    def create(self, request_field_dict: dict, db, current_user: (CurrentUser | None)):
        try:
            new_instance = self.model_class(**request_field_dict)
            db.add(new_instance)
            db.commit()
            db.refresh(new_instance)
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Can not create database instance')
        return new_instance

    def partial_update_by_id(self, id: int, request_field_dict: dict, db: Session, current_user: (CurrentUser | None)):
        try:
            instance = self.get_by_id(id, db, current_user)
            for var, value in request_field_dict.items():
                setattr(instance, var, value) if value else None
            db.add(instance)
            db.commit()
            db.refresh(instance)
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Can not update database instance')
        return instance
