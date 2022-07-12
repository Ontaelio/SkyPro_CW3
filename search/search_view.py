from flask import Blueprint, render_template, request, url_for
from utils import *

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search/', methods=['GET'])
def post_by_string():
    s_string = request.args.get('s')
    posts = search_for_posts(s_string)
    return render_template('search.html', posts=posts[:10], posts_num=len(posts))