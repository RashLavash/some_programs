from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('name', validators=[DataRequired(), Length(max=10, message='Слишком много символов')])
    text = TextAreaField('text', validators=[DataRequired(), Length(max=100, message='Слишком много символов')])
    author = StringField('author')
    submit = SubmitField('submit')


class UserForm(FlaskForm):
    user_name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])
    address = StringField('address')
    submit = SubmitField('submit')