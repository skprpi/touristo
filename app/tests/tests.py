# import pytest
from fastapi.testclient import TestClient
from fastapi import status
from .test_class.location import LocationTest
from .test_class.post import PostTest
from typing import Union
from .test_fixture import get_test_client_and_jwt


# Post test
def get_new_location_id(client, jwt):
    test_location = LocationTest(client, jwt)
    result = test_location.create()
    return result.json()['id']


def test_create_post(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_post = PostTest(client, jwt)
    location_id = get_new_location_id(client, jwt)
    expected_location_id = 1
    assert location_id == expected_location_id
    response = test_post.create(location_id)
    expected_new_id = 1
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == expected_new_id


def test_get_post(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_post = PostTest(client, jwt)
    location_id = get_new_location_id(client, jwt)
    expected_location_id = 1
    assert location_id == expected_location_id
    create_response = test_post.create(location_id)
    id = create_response.json()['id']
    assert id == 1
    response = test_post.get_by_id(id)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['id'] == id


def test_update_post(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_post = PostTest(client, jwt)
    location_id = get_new_location_id(client, jwt)
    expected_location_id = 1
    assert location_id == expected_location_id
    create_response = test_post.create(location_id)
    id = create_response.json()['id']
    assert id == 1
    new_text = 'Other text'
    response = test_post.update(id, {'text': new_text})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['id'] == id
    assert response.json()['text'] == new_text


# Location test


def test_create_location(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_location = LocationTest(client, jwt)
    response = test_location.create()
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == 1


def test_get_location(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_location = LocationTest(client, jwt)
    response = test_location.create()
    new_location_id = response.json()['id']
    assert new_location_id == 1
    get_responce = test_location.get_by_id(new_location_id)
    assert get_responce.status_code == status.HTTP_200_OK
    assert get_responce.json()['id'] == new_location_id


def test_update_location(get_test_client_and_jwt: Union[TestClient, str]):
    client, jwt = get_test_client_and_jwt
    test_location = LocationTest(client, jwt)
    response = test_location.create()
    id = response.json()['id']
    test_lat = 10000
    response = test_location.partial_update(id, {'lat': test_lat})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['lat'] == test_lat
    assert response.json()['id'] == id
