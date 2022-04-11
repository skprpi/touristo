from . import schemas
from fastapi import APIRouter, HTTPException, status, Depends
from .models import Posts
from ..common.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select


post_router = APIRouter(
    prefix='/post',
    tags=['post'],
)


@post_router.post('', response_model=schemas.Post)
async def create_post(post: schemas.CreatePost, session: AsyncSession = Depends(get_db)):
    new_post = Posts(text=post.text, photo=post.photo)
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post


@post_router.get('/{post_id}', response_model=schemas.Post)
async def get_post_by_id(post_id: int, session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(Posts).where(Posts.id == post_id))
    return result.scalars().first()
