from ..tests_db import fastapi_app
from fastapi.testclient import TestClient
import os


class PostTest:
    def __init__(self, client: TestClient, jwt: str) -> None:
        self.client = client
        self.jwt = jwt
        self.CONST_GET_BY_ID_FUNC_NAME = 'get_post'
        self.CONST_CREATE_FUNC_NAME = 'create_post'
        self.CONST_UPDATE_FUNC_NAME = 'update_post'

    def get_by_id(self, id):
        return self.client.get(
            fastapi_app.url_path_for(self.CONST_GET_BY_ID_FUNC_NAME, post_id=id),
            headers={
                'Authorization': self.jwt,
            }
        )

    def create(self, location_id):
        filepath = f'{os.path.dirname(os.path.abspath(__file__))}/data/testfile.jpeg'
        file = open(filepath, 'rb')
        response = self.client.post(
            fastapi_app.url_path_for(self.CONST_CREATE_FUNC_NAME, location_id=location_id),
            data={
                'location_id': location_id,
                'text': 'some text',
                'price': 100,
                'tag': 'cat',
            },
            files={
                'photo': ('photo', file, 'image/jpeg'),
            },
            headers={
                'Authorization': self.jwt,
            },
        )
        return response

    def update(self, id, update_json):
        response = self.client.patch(
            fastapi_app.url_path_for(self.CONST_UPDATE_FUNC_NAME, post_id=id),
            json=update_json,
            headers={
                'Authorization': self.jwt,
            }
        )
        return response
