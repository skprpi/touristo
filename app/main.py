from fastapi import FastAPI
import uvicorn
from .api.posts.router import post_router
from .api.common import db
import asyncio

app = FastAPI()
app.include_router(post_router)

@app.on_event("startup")
async def on_startup():
    await db.init_db()

if __name__ == '__main__':
    print('Done')
    uvicorn.run(app, host="localhost", port=8000)
