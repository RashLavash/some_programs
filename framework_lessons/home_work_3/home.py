import os

from flask import Flask
from flask import render_template, redirect, url_for

from flask_wtf.csrf import CSRFProtect

import sqlite3

from dotenv import load_dotenv

from my_form_class import MyHomeForm

load_dotenv()

SECRET_KEY = os.getenv('MY_SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

nav_list = [
    {"name": "Главная", "url": "/"},
    {"name": "Публикации", "url": "public_news"}
]


def connect_authors_publics_info_db():
    con = sqlite3.connect('framework_lessons/home_work_3/db/autors_publics_info.db')

    return con

def create_authors_publics_info_table():
    con = connect_authors_publics_info_db()
    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors_publics_info(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_name TEXT,
        author_email TEXT,
        public_title TEXT,
        public_text TEXT,
        date_public TEXT
    );
    ''')



def insert_for_author_publics_db(author_name, author_email, public_title, public_text, date_public):
    con = connect_authors_publics_info_db()
    cursor = con.cursor()

    query = ''' 
    INSERT INTO authors_publics_info(author_name, author_email, public_title, public_text, date_public) VALUES(?, ?, ?, ?, ?)
    '''
    query_data = (author_name, author_email, public_title, public_text, date_public)

    cursor.execute(query, query_data)

    con.commit()
    cursor.close()
    con.close()


@app.route('/')
def home():

    con = connect_authors_publics_info_db()
    con.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    cursor = con.cursor()

    cursor.execute('''
    SELECT author_name, author_email, public_title, public_text, date_public
    FROM authors_publics_info
    ''')

    db_response = cursor.fetchall()

    con.commit()
    con.close()

    return render_template('home.html', nav_list=nav_list, db_response=db_response)




@app.route('/public_news', methods=['GET', 'POST'])
def public_news():

    my_form = MyHomeForm()

    if my_form.validate_on_submit():
        author_name = my_form.author_name.data
        author_email = my_form.author_email.data
        date_public = my_form.date_public.data
        public_title = my_form.public_title.data
        public_text = my_form.public_text.data

        insert_for_author_publics_db(
            author_name=author_name,
            author_email=author_email,
            date_public=date_public,
            public_title=public_title,
            public_text=public_text
        )

        return redirect(url_for('home'))

    return render_template('public_news.html', nav_list=nav_list, form=my_form)



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)

