from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length



class UserForm(FlaskForm):
    user_name = StringField('name', validators=[DataRequired()])
    address = StringField('address')
    submit = SubmitField('submit')

class AddressForm(FlaskForm):
    town_name = StringField('Town name', validators=[DataRequired()])
    submit = SubmitField('Submit')