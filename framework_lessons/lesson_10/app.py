# pip install flask-login

from flask import render_template

from werkzeug.security import generate_password_hash, check_password_hash

from models import User, Address, Posts, Tags
from forms import UserForm, AddressForm
from config import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    db_sess = db.session.create_session()

    return db_sess.query(User).get(user_id)


@app.route('/')
def index():

    users = User.query.all()

    # post_1 = Posts(post_name='название 1')
    # post_2 = Posts(post_name='название 2')
    # print(post_1.post_name)
    # db.session.add(post_1)
    # db.session.add(post_2)

    # tag_1 = Tags(tag_name='тег1')
    # tag_2 = Tags(tag_name='тег2')
    # print(tag_1.tag_name)

    # db.session.add(tag_1)
    # db.session.add(tag_2)

    post_1 = Posts.query.get_or_404(1, 'Вы ошиблись')
    # print(post_1)

    tag_1 = Tags.query.get_or_404(1)
    tag_2 = Tags.query.get_or_404(2)

    # post_1.tags.append(tag_1)
    # post_1.tags.append(tag_2)

    print(post_1.tags)
    print(tag_1.posts)
    print(tag_2.posts)
    
    db.session.commit()
    return render_template('index.html', users=users)



@app.route('/users', methods=['GET', 'POST'])
def users():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user_name = user_form.user_name.data
        password = user_form.password.data
        address = user_form.address.data

        hashed_password = generate_password_hash(password)

        users = User(
            user_name=user_name,
            address_id=address,
            hashed_password=hashed_password
            )

        db.session.add(users)
        db.session.commit()
    
    users = User.query.all()
    
    return render_template('users.html', form=user_form, users=users)

@app.route('/spec_users', methods=['GET', 'POST'])
def get_user():
    user_form = UserForm()

    user = db.session.execute(db.select(User).filter_by(user_name='Lavash')).scalar()
    
    return render_template('users.html', form=user_form, users=user)

@app.route('/towns', methods=['GET', 'POST'])
def get_towns():
    address_form = AddressForm()

    if address_form.validate_on_submit():
        town_name = address_form.town_name.data
        town = Address(town_name=town_name)
        db.session.add(town)
        db.session.commit()

    towns = Address.query.all()

    return render_template('towns.html', towns=towns, form=address_form)


@app.errorhandler()
def page_not_found(error):
    return render_template('404.html', error=error), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)