from ..tests_db import fastapi_app
from fastapi.testclient import TestClient


class LocationTest:
    def __init__(self, client: TestClient, jwt: str) -> None:
        self.client = client
        self.jwt = jwt
        self.CONST_GET_BY_ID_FUNC_NAME = 'get_location'
        self.CONST_CREATE_FUNC_NAME = 'create_location'
        self.CONST_UPDATE_FUNC_NAME = 'update_location'

    def get_by_id(self, id):
        return self.client.get(
            fastapi_app.url_path_for(self.CONST_GET_BY_ID_FUNC_NAME, location_id=id),
            headers={
                'Authorization': self.jwt,
            }
        )

    def create(self):
        response = self.client.post(
            fastapi_app.url_path_for(self.CONST_CREATE_FUNC_NAME),
            json={
                'lat': 0.0,
                'lng': 0.0,
                'address': 'address',
                'title': 'title',
                'description': 'description',
                'location_type': 'location_type',
                'lighting_type': 'lighting_type',
                'visiting_type': 'visiting_type',
            },
            headers={
                'Authorization': self.jwt,
            }
        )
        return response

    def partial_update(self, id, update_json):
        response = self.client.patch(
            fastapi_app.url_path_for(self.CONST_UPDATE_FUNC_NAME, location_id=id),
            json=update_json,
            headers={
                'Authorization': self.jwt,
            }
        )
        return response
