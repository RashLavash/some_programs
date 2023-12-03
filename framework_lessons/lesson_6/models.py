from config import db


class User(db.Model):
    __tablename__ = 'all_users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    user_surname = db.Column(db.String(80), unique=True, nullable=True)

    def __repr__(self):
        return f"User id = {self.id}, user_name = {self.user_name}"
    
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    author = db.Column(db.String(255))
    data = db.Column(db.String(255), nullable=False)
