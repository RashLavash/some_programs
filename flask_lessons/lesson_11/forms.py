from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired



class UserForm(FlaskForm):
    user_name = StringField('name', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    login_name = StringField('name', validators=[DataRequired()])
    login_password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Авторизоваться')
