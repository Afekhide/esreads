from flask import request, session, redirect
from flask import jsonify
from flask.blueprints import Blueprint
from esreads.schemas import posts_schema
from esreads.models.post import Post

posts_blueprint = Blueprint('posts', __name__, url_prefix='/api/posts')


@posts_blueprint.route('/')
def all_posts():
    posts = Post.query.all()
    print('called posts/all...')
    return posts_schema.dumps(posts, many=True)


@posts_blueprint.route('/', methods=['POST'])
def create_post():
    data = request.json
    print(data)
    if 'ESREADS-API-KEY' not in request.headers:
        return jsonify({'errors': [{'desc': 'ESREADS-API-KEY header not found'}]})
    api_key = request.headers['ESREADS-API-KEY']
    return jsonify({'success': [{'desc': 'post created successfully'}]})
