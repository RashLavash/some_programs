import sqlite3
import os
from flask import Flask, render_template, request, g

# Конфигурация
DATABASE = '/for_flask/flsite.db'
DEBUG = True
SECRET_KEY = 'afdffereter8:fdsd;fwef3'

app = Flask(__name__)
app.config.from_object(__name__) # Загружаем конфигурацию из нашего приложения

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db'))) # Переопределяем путь к БД

def connect_db(): # Создаем оющую функцию для установления соединения с БД
    """ соединение с БД """
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory =  sqlite3.Row
    return con

def create_db():
    """ Вспомогательная функция для запуска создания БД """
    db = connect_db() # Сохраняем соединение с БД
    with app.open_resource('sq_db.sql', mode='r') as new_file: # Открываем sql файл, хранящий созданную таблицу
        db.cursor().executescript(new_file.read()) # Считываем содержимое файла sql
    
    db.commit()
    db.close()


def get_db():
    """ Соединение с БД, если оно не установлено """
    if not hasattr(g, 'link_db'): # Проверяем, существует ли у объекта g этот 'link_db'
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db() # Устанавливаем соединение с БД 
    return render_template('new.html', menu=[])


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'): # После завершения обработки запроса автоматически закрываем соединение с БД
        g.link_db.close()



if __name__ == '__main__':
    app.run(debug=True)