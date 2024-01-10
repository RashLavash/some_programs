from flask import render_template, redirect, url_for

from config import app, db
from models import Posts
from forms import PostsForm


NAV_LIST = [
    {"name": "Главная", "url": "/"},
    {"name": "Добавить статью", "url": "/add_post"},
    {"name": "Авторы", "url": "/add_post/authors"},
]


@app.route('/')
def index():
    return render_template('home.html', nav_list=NAV_LIST)


@app.route('/add_post')
def add_post():
    form = PostsForm()

    if form.validate_on_submit():
        author_name = form.author_name.data
        author_surname = form.author_surname.data
        author_lastname = form.author_lastname.data
        author_age = form.author_age.data
        author_gender = form.author_gender.data
        date_time = form.date_time.data

        add_info_for_db = Posts


        # Надо создать модель постов, шаблоны .htmд и создать бд 
        # и добей свой app.py

    return render_template('add_post.html', form=form)