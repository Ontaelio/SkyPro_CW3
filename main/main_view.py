from flask import Blueprint, render_template, url_for
from utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/index.html')
@main_blueprint.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)
