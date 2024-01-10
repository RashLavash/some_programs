# Устанавливаем фласк

from flask import Flask, render_template, request

app = Flask(__name__) # Создаем объект приложения

@app.route('/index')
@app.route('/') # декоратор, определяющий url
def hello_world():
    return 'Hello world!' # Flask преобразует строку в объект ответа


@app.route('/about')
def about_us():
    return render_template('temp.html')


@app.route('/users/<username>') # В url задается динамический параметр username
def show_user(username):
    return f'User whith id {username}'

@app.route('/posts/<int:id>') # В url задается явный параметр id
# int, float, string
def show_post(id):
    return f'Публикация № {id}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('temp.html')
    else:
        return 'Chetko', 201


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000) # Изменяем порт