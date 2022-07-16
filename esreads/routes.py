from esreads import app
from esreads import db
import flask_login
import utils
from flask_login import login_required, current_user, logout_user
from flask import render_template, redirect, request
from flask import url_for, session, flash
from esreads.models.user import User
from esreads.models.role import Role
from esreads.models.forms import LoginForm, RegistrationForm


@app.route('/index')
@app.route('/home')
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/register', methods=['GET', 'POST'])
@app.route("/signup", methods=['GET', 'POST'])
def register_user():
    regForm = RegistrationForm()
    if regForm.validate_on_submit():
        first_name = regForm.first_name.data
        last_name = regForm.last_name.data
        email = regForm.email.data
        password = regForm.password.data
        # if user already found for that email
        if User.query.filter_by(email=email).first():
            flash(f'Account already exists for {email}', category='error')
            return redirect(url_for('.register_user'))
        while User.query.filter_by(api_key=(api_key := utils.generate_api_key())).first() is not None:
            print(f"api_key: {api_key} already taken...")
            api_key = utils.generate_api_key()

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, api_key=api_key)
        db.session.add(new_user)
        db.session.commit()
        flask_login.login_user(new_user, remember=False)
        return redirect('/profile')
    return render_template('signup.html', form=regForm)


@app.errorhandler(404)
def handle_404(e):
    err_code = 404
    return render_template('error.html', err_message='That URL is invalid', err_code=err_code), 404


@app.route('/signout')
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')


@app.route('/write', methods=['GET'])
@login_required
def write_page():
    return render_template('write.html')


@app.route('/signin', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash(f"Invalid credentials", category='error')
            return redirect(url_for('.login'))

        flask_login.login_user(user, remember=False)
        flask_login.login_fresh()
        _next = request.args.get('next')
        if _next is None or (not _next.startswith('/')):
            return redirect(url_for('.index'))
        print(_next)
        return redirect(_next)

    return render_template('login.html', form=form)


