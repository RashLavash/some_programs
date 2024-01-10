# Миграции. 
# pip install flask-migrate
# export FLASK_APP=main
# flask db init
# flask db migrate -m "Расширили модель пользователя"
# flask db upgrade

# Расширение Alembic


from flask import render_template, request, redirect, url_for

from flask_migrate import Migrate

from models import User, Post
from config import app, db


migrate = Migrate(app, db)


@app.route('/')
def index():

    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    user_name = request.form.get('user_name')
    user_surname = request.form.get('user_surname')

    user = User(user_name=user_name, user_surname=user_surname)

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

