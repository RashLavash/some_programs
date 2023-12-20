from flask_login import UserMixin
from config import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, unique=True, nullable=False)
    hashed_password = db.Column(db.Text, nullable=False)

