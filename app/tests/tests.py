# import pytest
from fastapi.testclient import TestClient
from fastapi import status
from .test_class.location import LocationTest
from typing import Union
from .test_fixture import get_test_client_and_jwt


# Location test


def test_create_location(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_location = LocationTest(client, jwt)
    response = test_location.create_location()
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == 1


def test_get_location(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_location = LocationTest(client, jwt)
    response = test_location.create_location()
    new_location_id = response.json()['id']
    assert new_location_id == 1
    get_responce = test_location.get_by_id(new_location_id)
    assert get_responce.status_code == status.HTTP_200_OK
    assert get_responce.json()['id'] == new_location_id


def test_update_location(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_location = LocationTest(client, jwt)
    response = test_location.create_location()
    id = response.json()['id']
    test_lat = 10000
    response = test_location.partial_update_location(id, {'lat': test_lat})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['lat'] == test_lat
    assert response.json()['id'] == id
