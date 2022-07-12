from flask import Blueprint, render_template, abort, request, url_for
from utils import *

users_blueprint = Blueprint('users_blueprint', __name__, template_folder='templates')


@users_blueprint.route('/users/<user_id>')
def posts_by_user(user_id):
    try:
        posts = get_posts_by_user(user_id)
        return render_template('user-feed.html', posts=posts)
    except ValueError:
        abort (404, f"Пользователь {user_id} нам неизвестен")

