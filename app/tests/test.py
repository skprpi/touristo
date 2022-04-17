import pytest

from .db import client, fastapi_app

# from ..main import app

def test_create_post():
    # db.database.disconnect()
    response = client.post(
        fastapi_app.url_path_for('create_post'),
        json={'text': 'testing text', 'photo': 'test photo'},
    )
    print(response.json())
    assert response.json() == '1'

    
