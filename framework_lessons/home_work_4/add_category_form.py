from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddCategoryForm(FlaskForm):
    category_name = StringField('Введите название категории', validators=[DataRequired()])
    susbmit = SubmitField('Отправить')