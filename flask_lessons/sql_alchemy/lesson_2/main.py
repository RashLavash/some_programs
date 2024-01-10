import os

from flask import Flask
from flask import render_template, redirect, url_for

from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv

import sqlalchemy as db

from my_form_2 import MyForm


load_dotenv()


SECRET_KEY = os.getenv('MY_SECRET_KEY')


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

NAV_LIST = [
    {"name": "Главная", "url": "/"},
    {"name": "Публикации", "url": "public_news"}
]
FOOTER_NAME = "Rash_Lavash"


engine = db.create_engine(
    'sqlite:///framework_lessons/sql_alchemy/lesson_2/db/authors_and_publics.db'
)

metadata = db.MetaData()

authors_and_publics_db = db.Table('authors_and_publics', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('author_name', db.Text),
    db.Column('author_email', db.Text),
    db.Column('public_title', db.Text),
    db.Column('public_text', db.Text),
    db.Column('date_public', db.Text)
)

metadata.create_all(engine)


def connect_db():
    con = engine.connect()
    return con


def insert_db(author_name, author_email, public_title, public_text, date_public):
    con = connect_db()
    insertion_query = authors_and_publics_db.insert().values({
        "author_name": author_name,
        "author_email": author_email,
        "public_title": public_title,
        "public_text": public_text,
        "date_public": date_public
    })

    con.execute(insertion_query)
    con.commit()




@app.route('/')
def home():
    con = connect_db()
    select_query = db.select(authors_and_publics_db)
    select_results = con.execute(select_query)

    db_results = select_results.fetchall()

    con.commit()
    con.close()

    return render_template('home_page.html',
        footer_name=FOOTER_NAME,
        nav_list=NAV_LIST,
        db_results=db_results
    )


@app.route('/public_news', methods=['GET', 'POST'])
def public():
    form = MyForm()

    if form.validate_on_submit():
        author_name = form.author_name.data
        author_email = form.author_email.data
        public_title = form.public_title.data
        public_text = form.public_text.data
        date_public = form.date_public.data

        print(author_name, author_email, public_title, public_text, date_public)

        insert_db(
            author_name=author_name,
            author_email=author_email,
            public_title=public_title,
            public_text=public_text,
            date_public=date_public
        )

        return redirect(url_for('home'))
    print('Валидация не пройдена')
    
    return render_template('publics.html', footer_name=FOOTER_NAME, nav_list=NAV_LIST, form=form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
