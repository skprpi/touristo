from api.posts.router import post_router
from fastapi import FastAPI
import uvicorn


fastapi_app = FastAPI()
fastapi_app.include_router(post_router)


if __name__ == '__main__':
    uvicorn.run(fastapi_app, host="localhost", port=8000)
