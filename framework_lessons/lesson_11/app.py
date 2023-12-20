# pip install flask-login

from flask import render_template, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from flask_login import login_required

from models import User
from forms import UserForm, LoginForm
from config import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    # db_sess = db.session.create_session()

    # return db_sess.query(User).get(user_id)

    return User.query.get(user_id)


@app.route('/', methods=['GET', 'POST'])
def index():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        login_name = login_form.login_name.data
        login_password = login_form.login_password.data

        user = User.query.filter_by(user_name=login_name).first()

        if user and check_password_hash(user.hashed_password, login_password):
            login_user(user)
            return redirect(url_for('user_info'))
        print("не прошло")
        return render_template('index.html', form=login_form)

    return render_template('index.html', form=login_form)


@app.route('/user_info')
@login_required
def user_info():
    return f"Саламалейкум!!! {current_user.user_name}"


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/users', methods=['GET', 'POST'])
def users():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user_name = user_form.user_name.data
        password = user_form.password.data

        hashed_password = generate_password_hash(password)

        users = User(
            user_name=user_name,
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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)