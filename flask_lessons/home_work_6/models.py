from config import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    user_surname = db.Column(db.String(50), unique=True, nullable=True)

    def __repr__(self):
        return f"User(id = {self.id}, user_name = {self.user_name})"
    

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=True)
    text = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f"Posts(id = {self.id}, title = {self.title}, text = {self.text})"
    

class MyDate(db.Model):
    __tablename__ = 'my_date'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"MyDate(id = {self.id}, date = {self.date})"