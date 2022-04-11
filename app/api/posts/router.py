from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
from .models import posts
from ..common.db import get_db, database
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from datetime import datetime



post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)


@post_router.post('')
async def create_post(post: schemas.CreatePost):
    query = posts.insert()
    values = {**post.dict(), 'created_at': datetime.utcnow()}
    post_id = await database.execute(query=query, values=values)
    return {'id': post_id}


@post_router.get('/{post_id}')#, response_model=schemas.Post)
async def get_post_by_id(post_id: int):
    # posts.c.id for special column
    query = posts.select().where(posts.c.id == post_id)
    result = await database.fetch_one(query=query)
    return result
