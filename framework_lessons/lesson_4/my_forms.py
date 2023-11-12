# pip install flask-wtf

import os

from flask import Flask
from flask import render_template, redirect, url_for

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('MY_SECRET_KEY')


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=10, message='Слишком много символов')])
    text = TextAreaField('text', validators=[DataRequired(), Length(max=100, message='Слишком много символов')])
    submit = SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        print(name, text)
        # return redirect('/success')
        return redirect(url_for('success'))

    return render_template('home.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)