from flask import Flask
from flask import render_template, redirect, url_for

from flask_wtf import CSRFProtect

from flask_sqlalchemy import SQLAlchemy

import os

from dotenv import load_dotenv

from add_publics import AddPublicForm
from add_users import AddUsersForm

load_dotenv()

SECRET_KEY = os.getenv('MY_SECRET_KEY')

NAV_LIST = [
    {"name": "Главная", "url": "/"},
    {"name": "Добавить публикацию", "url": "/add_publics"},
    {"name": "Добавить пользователя", "url": "/add_users"},
    {"name": "Публикации", "url": "/publics"},
    {"name": "Пользователи", "url": "/users"}
]

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///publics.db'

csrf = CSRFProtect(app)

db = SQLAlchemy(app)


class Publics(db.Model):
    __tablename__ = 'publics'
    id = db.Column(db.Integer, primary_key=True)
    public_title = db.Column(db.String, unique=True, nullable=False)
    public_text = db.Column(db.Text, nullable=False)
    public_agreement = db.Column(db.Boolean, nullable=False)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    user_age = db.Column(db.Integer())




@app.route('/')
def home():
    return render_template('home.html', nav_list=NAV_LIST)


@app.route('/users')
def users():

    users = Users.query.all()

    return render_template('users.html', nav_list=NAV_LIST, users=users)


@app.route('/publics')
def publics():

    publics = Publics.query.filter(Publics.public_agreement.is_(True)).all()

    return render_template('publics.html', nav_list=NAV_LIST, publics=publics)


@app.route('/add_publics', methods=['GET', 'POST'])
def add_publics():

    add_public_form = AddPublicForm()

    if add_public_form.validate_on_submit():
        public_title = add_public_form.public_title.data
        public_text = add_public_form.public_text.data
        public_agreement = add_public_form.checkbox.data

        add_public = Publics(
            public_title=public_title,
            public_text=public_text,
            public_agreement=public_agreement
            )
        
        try:
            db.session.add(add_public)
            db.session.commit()

            return redirect(url_for('home'))
        
        except Exception as error:
            print('Произошла ошибка пи попытке сохранить данные в таблицу publics')
            return error
    return render_template('add_publics.html', nav_list=NAV_LIST, form=add_public_form)
            

@app.route('/add_users', methods=['GET', 'POST'])
def add_users():

    add_users_form = AddUsersForm()

    if add_users_form.validate_on_submit():
        user_name = add_users_form.user_name.data
        user_age = add_users_form.user_age.data

        add_user = Users(user_name=user_name, user_age=user_age)

        try:
            db.session.add(add_user)
            db.session.commit()

            return redirect(url_for('home'))
        
        except:
            return 'Произошла ошибка пи попытке сохранить данные в таблицу users'
    
    return render_template('add_users.html', nav_list=NAV_LIST, form=add_users_form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)