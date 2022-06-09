from .api.posts.router import post_router
from .api.users.router import user_router, login_router
from .api.locations.router import location_router
from fastapi import FastAPI
from .api.common.db import Base, engine

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

fastapi_app = FastAPI()
fastapi_app.include_router(post_router)
fastapi_app.include_router(user_router)
fastapi_app.include_router(login_router)
fastapi_app.include_router(location_router)
