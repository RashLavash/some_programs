from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddPublicForm(FlaskForm):
    public_title = StringField('Введите название публикации', validators=[DataRequired()])
    public_text = TextAreaField('Содержимое публикации')
    checkbox = BooleanField('Отображать публикацию?')
    submit = SubmitField('Отправить')