from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, DateTimeLocalField, SubmitField, RadioField
from wtforms.validators import DataRequired

class PostsForm(FlaskForm):
    author_name = StringField("Введите ваше имя", validators=[DataRequired()])
    author_surname = StringField("Введите вашу фамилию", validators=[DataRequired()])
    author_lastname = StringField("Введите ваше отчество", validators=[DataRequired()])
    author_age = IntegerField("Введите ваш возраст")
    author_gender = RadioField("Мужской", id="author_gender")
    author_gender = RadioField("Женский", id="author_gender")
    date_time = DateTimeLocalField("Дата появления на сайте")
    submit = SubmitField("Отправить")
    