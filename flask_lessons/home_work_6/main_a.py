from flask import render_template, redirect, url_for, request

from flask_migrate import Migrate

from config import app, db

from models import Users, Posts, MyDate


migrate = Migrate(app, db)

@app.route('/')
def index():

    users = Users.query.all()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    user_name = request.form.get('user_name')
    user_surname = request.form.get('user_surname')

    user = Users(user_name=user_name, user_surname=user_surname)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        title = request.form.get('user_title')
        text = request.form.get('user_text')
        author = request.form.get('author')

        post = Posts(title=title, text=text, author=author)

        try:
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('posts'))
        except:
            print('Ошибка пи отправлеии данных')
    posts = Posts.query.all()
    return render_template('posts.html', posts=posts)


@app.route('/my_date', methods=['GET', 'POST'])
def my_date():

    if request.method == 'POST':
        my_date = request.form.get('my_date')

        add_date = MyDate(date=my_date)
        try:
            db.session.add(add_date)
            db.session.commit()

            redirect(url_for('my_date'))
        except:
            return 'При добавлении даты в базу данных произошла ошибка'
    
    get_date = MyDate.query.all()

    return render_template('my_date.html', my_date=get_date)



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)