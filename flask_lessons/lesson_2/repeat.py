from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<string:user_name>', methods=['GET', 'POST'])
def index(username):
    return f"Здравствуйте {username}"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)