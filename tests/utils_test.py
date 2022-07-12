import pytest

from utils import *

from tests.fixtures import *


def test_get_posts_all_type():
    response = get_posts_all()
    assert isinstance(response, list)


def test_get_posts_all_single_keys(posts_keys):
    response = get_posts_all()
    trr = response[0]
    assert all(key in trr.keys() for key in posts_keys)


def test_get_posts_by_user_id(user_name):
    response = get_posts_by_user(user_name)
    assert response[0]['poster_name'] == user_name


def test_get_comments_by_post_id_pk():
    response = get_comments_by_post_id(1)
    assert all(comment['post_id'] == 1 for comment in response)


def test_comment_counter_string_0():
    response = comment_counter_string(0)
    assert response == '0 комментариев'


def test_comment_counter_string_11():
    response = comment_counter_string(11)
    assert response == '11 комментариев'


def test_comment_counter_string_21():
    response = comment_counter_string(21)
    assert response == '21 комментарий'


def test_comment_counter_string_32():
    response = comment_counter_string(32)
    assert response == '32 комментария'


def test_search_for_posts_is_a_post():
    response = search_for_posts('а')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def test_search_for_posts_is_correct(search_word):
    response = search_for_posts(search_word)
    assert all(search_word in post['content'] for post in response)


def test_get_post_by_pk_pk():
    response = get_post_by_pk(2)
    assert response['pk'] == 2


