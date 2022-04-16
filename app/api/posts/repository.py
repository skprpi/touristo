from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
# from .models import posts
# from ..common.db import database
from sqlalchemy import select
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


# async def create_post(post: schemas.CreatePost):
#     query = posts.insert()
#     values = {**post.dict(), 'created_at': datetime.utcnow()}
#     post_id = await database.execute(query=query, values=values)
#     return {'id': post_id}


# async def get_post_all():
#     query = posts.select()
#     return await database.fetch_all(query=query)

# async def get_post_by_id(post_id: int):
#     query = posts.select().where(posts.c.id == post_id)
#     return await database.fetch_one(query=query)
