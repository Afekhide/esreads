from flask.blueprints import Blueprint
from esreads.schemas import users_schema, user_schema
from esreads.models.user import User
from esreads import db

user_blueprint = Blueprint('users', __name__, url_prefix='/api/users')


@user_blueprint.route('/')
def all_users():
    users = User.query.limit(101).all()
    print('called users/all...')
    return users_schema.dumps(users, many=True)


@user_blueprint.route('/<string:email>')
def get_user(email):
    user = User.query.filter_by(email=email).first()
    return user_schema.dump(user)


@user_blueprint.route('/passwords/rehash/<int:id>')
def rehash_all(id):
    user = User.query.filter_by(id=id).first()
    from werkzeug.security import generate_password_hash
    print(f'{user.password}     =>      ', end='')
    user.password = generate_password_hash(password=user.password)
    print(user.password)

    db.session.commit()
    return 'all passwords hashed successfully...'
