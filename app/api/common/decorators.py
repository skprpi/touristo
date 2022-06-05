from fastapi import HTTPException, status
from .schemas import CurrentUser


def superuser(func):
    def _wrapper(*args, **kwargs):
        print(**kwargs)
        currecnt_user: CurrentUser = kwargs['current_user']
        if not currecnt_user.superuser:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied")
        func(*args, **kwargs)
    return _wrapper
