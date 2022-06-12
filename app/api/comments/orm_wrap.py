from ..common.orm_wrapper import SQLAlchemyWrap
from . import schemas
from sqlalchemy.orm import Session
from ..common.schemas import CurrentUser
from ..posts.router import post_orm_wrap


class CommentORMWrap(SQLAlchemyWrap):
    def __init__(self, model_class):
        super().__init__(model_class)

    def create(self, post_id: int, request: schemas.CreateComment, db: Session, current_user: CurrentUser):
        post_orm_wrap.get_by_id(post_id, db, current_user)

        fields = request.dict()
        fields['post_id'] = post_id
        fields['user_id'] = current_user.id
        return super().create(fields, db, current_user)
