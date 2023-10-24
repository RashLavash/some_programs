from flask import Flask, render_template, url_for, request


app = Flask(__name__)

menu = [
    {"name": "Установка", "url": "install_flask"},
    {"name": "Первое приолжение", "url": "ferst_app"},
    {"name": "Обратная связь", "url": "contact"}
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('new.html', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        print(request.form['user_name'])

    return render_template('contact.html', title='Обратная связь', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
