from flask import Flask
from flask import render_template, request
import sqlite3

app = Flask(__name__)

def connect_db():
    con = sqlite3.connect('framework_lessons/lesson_2/news.db')
    return con

def create_db():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT,
        article TEXT
    );
    ''')
    db.commit()
    cursor.close()
    db.close()

@app.route('/')
def index():
    return render_template('a_main.html')

@app.route('/public_news', methods=['GET', 'POST'])
def public_news():
    if request.method == 'GET':
        return render_template('public_news.html')
    elif request.method == 'POST':
        con = connect_db()
        cursor = con.cursor()
        query = ''' INSERT INTO news(author, article) VALUES(?, ?) '''
        query_data = (request.form.get('user_name'), request.form.get('user_article'))
        cursor.execute(query, query_data)

        con.commit()
        cursor.close()
        con.close()
        
        return render_template('public_news.html')


@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'GET':
        return render_template('b_news.html')
    elif request.method == 'POST':
        con = connect_db()
        con.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
        cursor = con.cursor()
        cursor.execute('''
        SELECT author, article
        FROM news
        ''')
        new_article = cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()

        for row in new_article:
            if request.form.get('search_author') == row['author']:
                return f"Статья: {row['article']}"
        return "Такого автра не существует"
        

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)