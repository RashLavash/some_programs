# pip install Flask-RESTful
# pip install SQLAlchemy-serializer

from config import app, api, db
from posts_resources import PostListResource, PostResource

from analytics import analytics_blueprint


api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')

app.register_blueprint(analytics_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return 'Not found' , 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='127.0.0.1', port=8000)
