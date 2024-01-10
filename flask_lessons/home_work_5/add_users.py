from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddUsersForm(FlaskForm):
    user_name = StringField('Введите ваше имя', validators=[DataRequired()])
    user_age = IntegerField('Введите ваш возраст')
    submit = SubmitField('Отправить')

