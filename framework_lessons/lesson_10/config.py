from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect

from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'

db = SQLAlchemy(app)

SECRET_KEY = 'jkdfhadjhfad'
app.config['SECRET_KEY'] = SECRET_KEY

csrf = CSRFProtect(app)


migrate = Migrate(app, db)

login_manager = LoginManager(app)