from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import PasswordField, EmailField, SubmitField, StringField


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(5, 30), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(3, 50)])
    login = SubmitField('Login')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(1, 30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(1, 30)])
    email = EmailField('Email', validators=[DataRequired(), Length(5, 30), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(3, 50)])
    #password2 = PasswordField('Password2', validators=[DataRequired(), Length(3, 50), EqualTo('password')])
    submit = SubmitField('Register')