
from flask import render_template, request, redirect, url_for

from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect

from models import Posts
from config import app, db
from forms import PostForm

migrate = Migrate(app, db)

SECRET_KEY = 'MY SECRET KEY'
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

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


@app.route('/posts/<int:post_id>')
def get_post(post_id):

    get_posts = Posts.query.get_or_404(post_id)
    return render_template('single_post.html', post=get_posts)

@app.route('/posts/author/<string:author_name>')
def get_author_popsts(author_name):
    # posts = Posts.query.filter_by(author=author_name).all()
    posts = Posts.query.filter_by(author=author_name).first_or_404()

    return render_template('author_posts.html', posts=posts)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='127.0.0.1', port=8000)