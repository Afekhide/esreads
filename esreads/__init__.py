from flask import Flask
from secrets import token_hex
from flask_login import login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate

app = Flask(__name__)
login_manager = login_manager.LoginManager(app=app)
login_manager.login_view = 'login'
app.config["SECRET_KEY"] = "2e157cd75237586d1773d19ea9a9fc8f4a466b9a003eef496e81e9b788ff"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/dummy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///esreads.db3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_AUTHENTICATION'] = True
app.config['MAIL_USERNAME'] = "dlite009@gmail.com"
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = "veyhpbwjattmcfhh"
app.config['MAIL_PORT'] = 587

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
mail = Mail(app=app)
from esreads import routes
from esreads.models.post import Post
from esreads.models.role import Role
from esreads.models.user import User
from esreads.blueprints.posts_blueprint import posts_blueprint
from esreads.blueprints.role_blueprint import role_blueprint
from esreads.blueprints.user_blueprint import user_blueprint
from esreads.blueprints.auth_blueprint import auth_blueprint
from esreads.blueprints.email_blueprint import email_blueprint

app.register_blueprint(posts_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(role_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(email_blueprint)

@app.shell_context_processor
def make_context():
    return dict(db=db, user=User, role=Role, post=Post)
