from flask_sqlalchemy import SQLAlchemy
from home_main import app

db = SQLAlchemy(app)

class AddCategory(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50))

    


