from flask import Blueprint, render_template, abort
from utils import *

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    if post_id < 1:
        abort(400, 'Invalid post id')
    try:
        if post := get_post_by_pk(post_id):
            comments = get_comments_by_post_id(post_id)
            comment_counter = comment_counter_string(len(comments))
            return render_template('post.html', post=post, comments=comments, cntr_str=comment_counter)
    except ValueError:
        abort(404, f"Поста {post_id} не существует")