from .api.posts.router import post_router
from .api.users.router import user_router, login_router
from fastapi import FastAPI
import uvicorn


fastapi_app = FastAPI()
fastapi_app.include_router(post_router)
fastapi_app.include_router(user_router)
fastapi_app.include_router(login_router)


# if __name__ == '__main__':
#     uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)
