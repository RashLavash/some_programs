from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email



class MyHomeForm(FlaskForm):
    public_title = StringField('Название для публикации', validators=[Length(min=8, message="Слишком мало символов")])
    author_name = StringField('Введите имя автора', validators=[DataRequired(), Length(min=5, max=50, message="Минимальное количество допустимых символов 20, максимальное 50")])
    author_email = EmailField('Введите email автора', validators=[Email()])
    date_public = DateTimeLocalField('Укажите дату создания публикации')
    public_text = TextAreaField('Текст вашей публикации')
    submit = SubmitField('Отправить')


