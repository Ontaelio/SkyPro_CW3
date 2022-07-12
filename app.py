from flask import Flask, jsonify, abort, request, render_template, send_from_directory

from main.main_view import main_blueprint
from post.post_view import post_blueprint
from search.search_view import search_blueprint
from users.users_view import users_blueprint
from utils import *
from loggers import api_logger

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    if e.description[:3] == 'The':
        e.description = 'Страница не найдена'
    return e, 404


@app.errorhandler(500)
def server_error(e):
    return 'Что-то пошло не так на сервере', 500


@app.route('/api/posts', methods=['GET'])
def api_get_all():
    posts = get_posts_all()
    api_logger.info(f"Запрос /api/posts")
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def api_get_post(post_id):
    post = get_post_by_pk(post_id)
    api_logger.info(f"Запрос /api/posts/{post_id}")
    return jsonify(post)


if __name__ == '__main__':
    app.run()
