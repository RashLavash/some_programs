from flask import current_app as app
from finances.models import Post
    

@app.route('/')
def index():
    return 'Главная страница'
