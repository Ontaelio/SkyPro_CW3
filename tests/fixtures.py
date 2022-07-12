import pytest

@pytest.fixture()
def posts_keys():
    return ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')


@pytest.fixture()
def comment_keys():
    return ("post_id", "commenter_name", "comment", "pk")


@pytest.fixture()
def search_word():
    return ('где')


@pytest.fixture()
def user_name():
    return ('johnny')

