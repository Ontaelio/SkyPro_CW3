import json
from typing import List

from loggers import file_logger


def get_json(fname: str) -> List[dict]:
    """
    get data from a JSON
    :param fname: JSON filename
    :return: list of posts
    """
    try:
        with open(fname, encoding='utf-8') as fin:
            posts = json.load(fin)
    except FileNotFoundError:
        # print('Posts file not found!')
        file_logger.critical(f'JSON file {fname} not found')
        posts = []
    except json.JSONDecodeError:
        # print('Json recoding error')
        file_logger.critical(f'JSON file {fname} decode error')
        posts = []
    return posts


def write_json(posts, fname):
    """
    save data to JSON (for future use in * tasks)
    :param posts: list of posts
    :param fname: JSON filename
    :return:
    """
    try:
        with open(fname, 'w', encoding='utf-8') as fout:
            json.dump(posts, fout, indent=1, ensure_ascii=False)
    except IOError:
        print('IO error')


def get_posts_all() -> List[dict]:
    """
    get all posts in a list of dicts
    :return: a list of dicts
    """
    posts = get_json('data/data.json')
    return posts


def get_posts_by_user(user_name: str) -> List[dict]:
    """
    get all posts written by 'user_name'
    :param user_name: user name
    :return: a list of dicts
    """
    all_posts = get_posts_all()
    user_posts = []
    for post in all_posts:
        if post['poster_name'] == user_name:
            user_posts.append(post)
    if user_posts:
        return user_posts
    raise ValueError


def get_comments_by_post_id(post_id: int) -> List[dict]:
    """
    get all comments to a single post
    :param post_id: id (pk) of a post
    :return: list of dicts (comments) or an empty list. DO NOT raise ValueError here!
    (as we are better off with '0 comments' message)
    """
    all_comments = get_json('data/comments.json')
    user_comments = []
    for comment in all_comments:
        if comment['post_id'] == post_id:
            user_comments.append(comment)
    return user_comments


def comment_counter_string(cnt: int) -> str:
    """
    Create a correctly spelled comment counter string
    :param cnt: num of comments
    :return: string
    """
    if 10 < cnt < 15:
        return f"{cnt} комментариев"
    if cnt % 10 == 1:
        return f"{cnt} комментарий"
    if 1 < cnt % 10 < 5:
        return f"{cnt} комментария"
    return f"{cnt} комментариев"


def search_for_posts(query: str) -> List[dict]:
    """
    find all posts containing str
    :param query: string to search
    :return: a list of posts (or an empty one if no posts found)
    """
    all_posts = get_posts_all()
    found_posts = []
    for post in all_posts:
        if query.lower() in post['content'].lower():
            found_posts.append(post)
    return found_posts


def get_post_by_pk(pk: int) -> dict:
    """
    find a single post by its ID (pk)
    :param pk: ID
    :return: a single post (dict)
    """
    all_posts = get_posts_all()
    for post in all_posts:
        if post['pk'] == pk:
            return post
    raise ValueError


if __name__ == '__main__':
    a = get_posts_by_user('larry')
    b = get_comments_by_post_id(1)
    c = search_for_posts('покаrf')
    d = get_post_by_pk(3)
    print(a)
    print(b)
    print(c)
    print(d)
