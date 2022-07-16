import secrets
from flask import Blueprint
from esreads.models.user import User
from flask_login import login_required, current_user

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/confirm')
@login_required
def generate_token():
    return current_user.generate_confirmation_token()


@auth_blueprint.route('/confirm/<token>')
@login_required
def confirm_account(token):
    if not current_user.confirm(token):
        return 'Bad Token'

    return 'Verified'
