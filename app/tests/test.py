import pytest
import asyncio
from fastapi import status
from httpx import AsyncClient

from ..api.common.db import get_db
from .common.db import override_get_db, init_db
from ..main import app

import asyncio


asyncio.run(init_db())
app.dependency_overrides[get_db] = override_get_db


@pytest.mark.anyio
async def test_post_create():
    # db.database.disconnect()
    async with AsyncClient(app=app, base_url="http://test") as client:
        responce = await client.post(
           '/post',
           json={"text": "111string111", "photo": "111string111"},
        )
    assert responce.status_code == status.HTTP_200_OK
    print(responce.json())
    
