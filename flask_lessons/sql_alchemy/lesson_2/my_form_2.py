from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email



class MyForm(FlaskForm):
    author_name = StringField('Введите свое имя', validators=[DataRequired(), Length(min=8, message='Имя слишком короткое')])
    author_email = EmailField('Введите вашу почту', validators=[DataRequired(), Email()])
    public_title = StringField('Введите название статьи', validators=[Length(min=5, message='Слишком мало символов')])
    public_text = TextAreaField('Содержание статьи')
    date_public = DateTimeLocalField('Дата создания статьи')
    submit_btn = SubmitField('Отправить')

