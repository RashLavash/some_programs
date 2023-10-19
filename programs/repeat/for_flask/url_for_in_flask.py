from flask import Flask, render_template, url_for


app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]

@app.route("/")
@app.route("/index") # Вернет последний указанный url - адрес по умолчанию
def index():
    print(url_for('index')) # Возвращает url - адрес, привязанный к передаваемой в качестве аргумента функции
    return render_template('new.html', menu=menu)

@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)

# @app.route('/profile/<username>') # Создаем переменную, ринимающую в себя какое-либо значение, и передаем ее функции, как аргумент
@app.route('/profile/<path:username>') # path - это конвертор, с помощью которого можно использовать любые допустимые символы URL 
def profile(username):
    return f'Пользователь {username}'

# with app.test_request_context(): # Тестовый контекст запроса - позволяет проверить работает ли функция url_for()
#     print(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)