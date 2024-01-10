from flask import render_template, redirect, url_for

from models import User, Posts
from forms import UserForm, PostForm
from config import app, db

from flask_migrate import Migrate

migrate = Migrate(app, db)


@app.route('/')
def index():

    return render_template('index.html')



@app.route('/posts', methods=['GET', 'POST'])
def posts():
    post_form = PostForm()

    if post_form.validate_on_submit():

        title = post_form.title.data
        text = post_form.text.data
        author = post_form.author.data

        post = Posts(title=title, text=text, author=author)

        try:
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('posts'))
        except:
            print('Ошибка пи отправлеии данных')
    posts = Posts.query.all()
    return render_template('posts.html', posts=posts, form=post_form)


@app.route('/users', methods=['GET', 'POST'])
def users():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user_name = user_form.user_name.data
        age = user_form.age.data
        address = user_form.address.data

        users = User(user_name=user_name, age=age, address=address)

        db.session.add(users)
        db.session.commit()
    
    users = User.query.all()
    
    return render_template('users.html', form=user_form, users=users)


@app.route('/spec_users', methods=['GET', 'POST'])
def get_user():
    user_form = UserForm()
    # users = User.query.all()
    # users = User.query.filter_by(address='Semender').all()
    # users = User.query.filter(User.user_name=='Rash').all()
    # users = User.query.filter(User.user_name.in_(('Ruslan', 'Rash'))).all()
    # users = User.query.filter(User.age.in_(range(10, 30))).all()
    # users = User.query.filter(User.age.not_in(range(10, 30))).all()
    # users = User.query.filter(
    #     db.and_(
    #         User.age.in_(range(10, 30)),
    #         User.address == 'Semender',
    #         User.user_name == 'Rash'
    #     )
    #     ).all()
    
    # Аналогично с db.or_()

    # users = User.query.filter(
    #     db.and_(
    #         db.or_(
    #             User.age.in_(range(10, 30)),
    #             User.address == 'Semender'
    #         ),
    #         User.user_name == 'Rash'
    #     )
    #     ).all()
    # users = User.query.order_by(User.age).filter_by(address='Semender').all()
    # users = User.query.order_by(User.age)
    # users = User.query.order_by(User.age.desc()).all()
    # users = User.query.limit(1).all()

    # users = User.query.filter(User.user_name.endswith('h')).all()
    # users = User.query.filter(User.user_name.startswith('L')).all()

    # db.session.query(User, )

    user = db.session.execute(db.select(User).filter_by(user_name='Lavash')).scalar()
    
    return render_template('users.html', form=user_form, users=user)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)