from esreads import db, mail, app
from flask import Blueprint
from flask_mail import Message
from flask import current_app
from threading import Thread
from flask_login import current_user

email_blueprint = Blueprint('email', __name__, url_prefix='/email')


@email_blueprint.route('/send', methods=['GET', 'POST'])
def send_mail():
    def send_message(mail, msg, app):
        with app.app_context():
            mail.send(msg)
    msg = Message('Hello again from ESReads', recipients=['esdlite@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    Thread(target=send_message, args=(mail, msg, app)).start()
    return "Sent"
