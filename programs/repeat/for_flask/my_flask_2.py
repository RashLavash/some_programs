from flask import Flask, render_template

app = Flask(__name__)


menu = ["Установка", "Первое приложение", "Обратная связь"]

@app.route('/new')
@app.route('/')
def new_page():
    return render_template('new.html', menu=menu)

@app.route('/about')
def about_us():
    return render_template('about.html', title="О нас", menu=menu)



if __name__ == '__main__':
    app.run(debug=True)