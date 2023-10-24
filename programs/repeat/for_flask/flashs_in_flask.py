from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sldkfkfcmei45nknl3kn5kl;'

menu = [
    {"name": "Установка", "url": "install_flask",},
    {"name": "Первое приложение", "url": "first_app"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route('/')
def index():
    return render_template('new.html', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['user_name']) > 2:
            flash('Сообщение отправлено', category='success') # задаем определенную категорию для мгновенноого сообщения
        else:                                                 # с помощью передачи именного параметра category
            flash('Ошибка отправки', category='error')
    
    return render_template('contact.html', title='Обратная связь', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)