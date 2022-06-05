import pytest
from typing import Union
from .tests_db import engine, fastapi_app
from ..api.common.db import Base
from fastapi import status
from fastapi.testclient import TestClient


@pytest.fixture()
def get_test_client_and_jwt() -> Union[TestClient, str]:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    client = TestClient(fastapi_app)
    test_user_email = 'test_user@mail.ru'
    test_user_password = 'test_user_password'
    response = client.post(
        fastapi_app.url_path_for('create_user'),
        json={
            'nickname': 'test_user',
            'email': test_user_email,
            'password': test_user_password,
            'photo': 'test_photo',
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    jwt_responce = client.post(
        fastapi_app.url_path_for('login'),
        data={
            'username': test_user_email,
            'password': test_user_password,
        }
    )
    jwt_json = jwt_responce.json()
    assert jwt_json['token_type'] != ''
    assert jwt_json['access_token'] != ''
    return client, f"{jwt_json['token_type']} {jwt_json['access_token']}"
