from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length



class PostForm(FlaskForm):
    title = StringField('name', validators=[DataRequired(), Length(max=10, message='Слишком много символов')])
    text = TextAreaField('text', validators=[DataRequired(), Length(max=100, message='Слишком много символов')])
    author = StringField('author')
    submit = SubmitField('submit')