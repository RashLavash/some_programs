from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', username='Rash')


if __name__ == '__main__':
    app.run()