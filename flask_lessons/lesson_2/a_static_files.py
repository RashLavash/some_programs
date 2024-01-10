from flask import Flask
from flask import url_for, render_template, request
import sqlite3

app = Flask(__name__)


USERS = {
    'Rash': '1234',
    'Murtuz': '4567'
}


con = sqlite3.connect('framework_lessons/lesson_2/new_db.db')
cursor = con.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    user_password INTEGER
);
''')

con.commit()
cursor.close()
con.close()


@app.route('/')
def index():
    return f"Здравствуйте"

@app.route('/news')
def news():
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{ url_for('static', filename='css/style.css') }">
    <title>News</title>
</head>
<body>
    <h1>News</h1>
    <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, doloribus assumenda voluptatibus dicta necessitatibus nostrum minus facilis repellendus, praesentium dolorem quo esse eos, blanditiis accusantium consequatur asperiores fugiat nobis? Distinctio.
    </div>
    <img src="{url_for('static', filename='img/')}" alt="картинка">
</body>
</html>

'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        con = sqlite3.connect('framework_lessons/lesson_2/new_db.db')
        # con.row_factory = sqlite3.Row
        con.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
        cursor = con.cursor()

        cursor.execute('''
        SELECT user_name, user_password
        FROM users
        ''')
        database_dates = cursor.fetchall()
        cursor.close()
        con.close()

        for rows in database_dates:
            # print(rows['user_password'])
            if rows['user_password'] == int(request.form.get('psw')):
                return "Добро пожаловать"
        return "Пароль неверный"
            
    else:
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{ url_for('static', filename='css/style.css') }">
    <title>Stranichko</title>
</head>
<body>

    <form action="/login" method="post" >
        <input type="text" name="user_name">
        <input type="password" name="psw">
        <input type="submit">
    </form>
</body>
</html>
'''
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    
    if request.method == 'POST':
        # print(request.form.get('login'))  
        # print(request.form.get('psw'))
        con = sqlite3.connect('framework_lessons/lesson_2/new_db.db')
        cursor = con.cursor()
        query = ''' INSERT INTO users(user_name, user_password) VALUES(?, ?) '''
        query_data = (request.form.get('user_name'), request.form.get('psw'))
        cursor.execute(query, query_data)
        con.commit()
        
        cursor.close()
        con.close()
        return 'Регистрация прошла успешно!'
    else:
        return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{ url_for('static', filename='css/style.css') }">
        <title>Stranichko</title>
    </head>
    <body>

        <form action="/registration" method="post" class="new_form">
            <input type="text" name="user_name">
            <input type="password" name="psw">
            <input type="submit">
        </form>

    </body>
    </html>
    '''



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)