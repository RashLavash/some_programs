from flask import Flask

app = Flask(__name__)

@app.route('/new_page')
@app.route('/')
def new_page():
    return "new_page"

@app.route('/about')
def new_page_2():
    return "<h1>About us</h1>"


if __name__ == '__main__':
    app.run(debug=True)