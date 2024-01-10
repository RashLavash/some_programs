from config import db

    
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    author = db.Column(db.Text, nullable=True)


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.Integer, nullable=True)
