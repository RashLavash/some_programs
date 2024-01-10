from flask import Flask
from flask import render_template, request
import sqlite3


app = Flask(__name__)

nav_list = [
    {"name": "Главная", "url": "/"},
    {"name": "Новости", "url": "news"},
    {"name": "Админка", "url": "admin"},
    {"name": "О нас", "url": "about"}
]

male_list = {
    "male": "Мужской",
    "female": "Женский"
}


def connect_staff_db():
    """ Создаем бд для работников """
    con = sqlite3.connect('framework_lessons/home_work_2/db/staffs.db')
    return con


def connect_article_db():
    """ Создаем бд для статей """
    con = sqlite3.connect('framework_lessons/home_work_2/db/articles.db')
    return con


def create_staff_db():
    """ Создаем таблицу работников """
    con = connect_staff_db()
    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS staffs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        staff TEXT,
        staff_age INTEGER,
        staff_gender TEXT
    );
    ''')

    con.commit()
    cursor.close()
    con.close()


def create_article_db():
    """ Создаем таблицу для статей """
    con = connect_article_db()
    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        article TEXT
    );
    ''')

    con.commit()
    cursor.close()
    con.close()
    


@app.route('/')
def main_page():
    return render_template('main_page.html', title="Главная страница", nav_list=nav_list)

@app.route('/news')
def news():
    con = connect_article_db()
    con.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    cursor = con.cursor()
    cursor.execute('''
    SELECT title, article
    FROM articles
    ''')
    info_list = cursor.fetchall()

    con.commit()
    cursor.close()
    con.close()

    return render_template('news.html', title="Новости", nav_list=nav_list, info_list=info_list)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html', title="Админка", nav_list=nav_list, male_list=male_list)
    elif request.method == 'POST':

        if request.form.get('get_value') == 'Добавить работника':

            con = connect_staff_db()
            cursor = con.cursor()

            staff_query = ''' INSERT INTO staffs(staff, staff_age, staff_gender) VALUES(?, ?, ?)'''
            staff_data = (request.form.get('user_name'), request.form.get('user_age'), request.form.get('user_gender'))

            cursor.execute(staff_query, staff_data)

            con.commit()
            cursor.close()
            con.close()

            return render_template('admin.html', title="Админка", nav_list=nav_list, male_list=male_list)
        
        elif request.form.get('get_value') == 'Добавить статью':

            con = connect_article_db()
            cursor = con.cursor()

            article_query = ''' INSERT INTO articles(title, article) VALUES(?, ?)'''
            article_data = (request.form.get('title_article'), request.form.get('article_text'))

            cursor.execute(article_query, article_data)

            con.commit()
            cursor.close()
            con.close()

            return render_template('admin.html', title="Админка", nav_list=nav_list, male_list=male_list)


@app.route('/about')
def about():
    con = connect_staff_db()
    con.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    cursor = con.cursor()
    cursor.execute('''
    SELECT staff, staff_age, staff_gender
    FROM staffs
    ''')
    staff_list = cursor.fetchall()

    con.commit()
    cursor.close()
    con.close()

    return render_template('about.html', title="О нас", nav_list=nav_list, staff_list=staff_list)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
