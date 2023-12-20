from config import db


class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)
    author_surname = db.Column(db.String(50), nullable=False)
    author_lastname = db.Column(db.String(50), nullable=False)
    author_age = db.Column(db.Integer, nullable=False)
    author_gender = db.Column(db.String(50), nullable=True)
    date_time = db.Column(db.String(50), nullable=False)