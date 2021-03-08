from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length,EqualTo 


class RegistFrom(FlaskForm):
    username = StringField("username",validators=[DataRequired(),Length(min=3, max=20)])
    password = PasswordField("password",validators=[DataRequired(),Length(min=8)])
    check_pass = PasswordField("check_pass", validators=[DataRequired(),EqualTo('password')])

    Register = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("username",validators=[DataRequired(),Length(min=5, max=20)])
    password = PasswordField("password",validators=[DataRequired(),Length(min=8)])

    Login = SubmitField("Login")


class PostForm(FlaskForm):

    content = TextAreaField("content",validators=[DataRequired(),Length(max=500)])
    
    submit = SubmitField("submit")