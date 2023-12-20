from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired



class UserForm(FlaskForm):
    user_name = StringField('name', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    address = StringField('address')
    submit = SubmitField('submit')

class AddressForm(FlaskForm):
    town_name = StringField('Town name', validators=[DataRequired()])
    submit = SubmitField('Submit')