from fastapi import FastAPI
import uvicorn
from api.posts.router import post_router
from api.common import db
import asyncio

app = FastAPI()
app.include_router(post_router)

# @app.on_event("startup")
# def on_startup():
#     db.startup_handler(app)

# @app.on_event("shutdown")
# def on_shutdown():
#     db.shutdown_handler(app)

if __name__ == '__main__':
    app.add_event_handler("startup", db.startup_handler(app))
    app.add_event_handler("shutdown", db.shutdown_handler(app))
    uvicorn.run(app, host="localhost", port=8000)
