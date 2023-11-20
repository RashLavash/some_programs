from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase

# from datetime import datetime



# class Base(DeclarativeBase):
#     pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# Чтобы создать базу данных, путь терминала должен находиться в той папке,
# в которой находится ваш файл с ваше созданной бд.
# в терминале активируем пайтон, если работайте через pycharm, то через пайтон консоль,
# затем мипортируем из нашего файла наше приложение и экземпляр класса SQLAlchemy.
# from your_file.py import app, db
# Далее вызовем app.app_context().push()
# Наконец db.create_all()


# Либо запустим наш файл, так же находясь в нужном пути в терминале, прописав:
# with app.app_context():
#     db.create_all()


# app.app_context().push()
# db.create_all()

# if __name__ == '__main__':
#     app.run(debug=True)
