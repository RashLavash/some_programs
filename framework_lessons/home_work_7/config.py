from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = 'MY_SECRET_KEY'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://some.db'
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

csrf = CSRFProtect(app)

migrate = Migrate(app, db)