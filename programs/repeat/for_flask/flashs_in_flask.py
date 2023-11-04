from flask import Flask, render_template, request, flash, session, redirect, url_for, abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sldkfkfcmei45nknl3kn5kl;'

menu = [
    {"name": "Установка", "url": "install_flask"},
    {"name": "Первое приложение", "url": "first_app"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route('/')
def index():
    return render_template('new.html', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title="О нас", menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['user_name']) > 2:
            flash("Сообщение отправлено", category='success') # задаем определенную категорию для мгновенноого сообщения
        else:                                                 # с помощью передачи именного параметра category
            flash("Ошибка отправки", category='error')
    
    return render_template('contact.html', title="Обратная связь", menu=menu)

@app.route('/profile/<user_name>')
def profile(user_name):
    if 'userLogged' not in session or session['userLogged'] != user_name: # Если пользвоатель вводит чужой profile через адресную строку, выдаем исключение abort(404)
        abort(401)

    return f"Профиль пользователя: {user_name}"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:      # Если пользователь залогинился, преведем его по профильному url
        return redirect(url_for('profile', user_name=session['userLogged']))
    elif request.method == 'POST' and request.form['user_name'] == 'Rash' and request.form['user_psw'] == 2003: # Иначе, если имя пользователся и его пароль верны, добавляем данные в сессию
        session['userLogged'] = request.form['user_name']

    return render_template('login.html', title="Авторизация", menu=menu) # В противном случае, вернем изначальную страницу авторизации


@app.errorhandler(404)              # Отлавливаем ошибку, если страницы не существует
def page_not_found(error):          # Передаем методу отловленную ошибку
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404 # В терминал выведится номер ошибки, т.е. 404

if __name__ == '__main__':
    app.run(debug=True)