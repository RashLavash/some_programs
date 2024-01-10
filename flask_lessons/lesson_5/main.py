# pip install Flask_SQLAlchemy

from flask import Flask
from flask import render_template, redirect, request, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'all_users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    # Наиболее популярные типы данных - Text, Boolean, DateTime, Float, LargeBinary

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)



@app.route('/')
def index():

    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    user_name = request.form.get('user_name')

    user = User(user_name=user_name)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        title = request.form.get('user_title')
        text = request.form.get('user_text')

        print(title)
        print(text)

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('posts'))
        except:
            print('Ошибка пи отправлеии данных')
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='127.0.0.1', port=8000)

