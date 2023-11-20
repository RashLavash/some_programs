from flask import Flask
from flask import render_template, redirect, url_for

from flask_wtf.csrf import CSRFProtect

import os
from dotenv import load_dotenv

from add_category_form import AddCategoryForm


load_dotenv()

SECRET_KEY = os.getenv('MY_SECRET_KEY')
NAV_LIST = [
    {"name": "Главная", "url": "home"}
]

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///add_categorys.db'

csrf = CSRFProtect(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', nav_list=NAV_LIST)


@app.route('/add_categories')
def add_categories():

    from add_category import AddCategory, db


    form = AddCategoryForm()

    if form.validate_on_submit():
        category_name = form.category_name.data

        add_in_table_info = AddCategory(category_name=category_name)

        try:
            db.session.add(add_in_table_info)
            db.session.commit()

            redirect(url_for('home'))
        except:
            return 'При добавлении статьи произошла ошибка'
    
    return render_template('add_categories.html', nav_list=NAV_LIST)


@app.route('/categories/<categories_id>')
def category(categories_id):
    pass
    # Получилось передать в динамический аргумент данные с помощью шаблонизации, см. в base.html
    # Теперь нужно использовать переданный в url строку динамический параметр, который является айдишником категории
    # сделай select запрос в бд, в которой хранятся категории для шапки, который вернет категорию по айди,
    # полученному из динамического аргумента <categories_id>





if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)

