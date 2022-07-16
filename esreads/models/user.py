from esreads import db
from utils import generate_api_key
from esreads import login_manager
from flask_login import UserMixin
from flask import current_app
from itsdangerous.exc import SignatureExpired, BadSignature
from itsdangerous import URLSafeTimedSerializer as Serializer
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

DURATION = 15 * 60


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    order = True
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(200), nullable=False)
    api_key = db.Column(db.String(50), nullable=True, unique=True, default=generate_api_key)
    img_data = db.Column(db.BLOB(), nullable=True)
    confirmed = db.Column(db.Boolean, nullable=False, default=0)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, new_password):
        self.password_hash = generate_password_hash(new_password, salt_length=16)

    def verify_password(self, provided_password):
        return check_password_hash(self.password_hash, provided_password)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'User(id= {self.id}, email={self.email}, api_key={self.api_key}, posts={[post.title for post in self.posts]})'

    @property
    def verify(self):
        return self.confirmed

    @verify.setter
    def verify(self, confirmed=False):
        self.confirmed = confirmed

    def generate_confirmation_token(self):

        serializer = Serializer(current_app.config['SECRET_KEY'])
        data = {'confirm': self.id}
        return serializer.dumps(data)

    def confirm(self, token):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            decode_value = serializer.loads(token, max_age=DURATION)
            print(decode_value)
            return decode_value['confirm'] == self.id
        except SignatureExpired:
            print('Signature expired')
            return False
        except BadSignature as badSignature:
            print('Invalid signature')
            return False


@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=int(user_id)).first()
    return user
