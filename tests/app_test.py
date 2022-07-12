import pytest

from app import app

from tests.fixtures import *


def test_api_all():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_api_is_dict():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json[0], dict)


def test_api_has_keys(posts_keys):
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    trr = response.json[0]
    assert all(key in trr.keys() for key in posts_keys)


def test_api_has_keys_post(posts_keys):
    response = app.test_client().get('/api/posts/2')
    assert response.status_code == 200
    trr = response.json
    assert all(key in trr.keys() for key in posts_keys)


def test_api_is_dict_post():
    response = app.test_client().get('/api/posts/3')
    assert response.status_code == 200
    assert isinstance(response.json, dict)


