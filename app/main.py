from .api.posts.router import post_router
from .api.users.router import user_router, login_router
from .api.locations.router import location_router
from fastapi import FastAPI


fastapi_app = FastAPI()
fastapi_app.include_router(post_router)
fastapi_app.include_router(user_router)
fastapi_app.include_router(login_router)
fastapi_app.include_router(location_router)
