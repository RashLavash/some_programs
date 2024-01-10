# pip install Flask-RESTful
# pip install SQLAlchemy-serializer

from flask import jsonify, request
from flask_restful import Resource

from models import Post
from config import app, api, db



class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
    
        return jsonify(
            {
                'posts': [
                    post.to_dict(only=('text',))
                    for post in posts
                ]
            }
        )


    def post(self):

        data1 = request.json

        post = Post(text=data1['text'])
        db.session.add(post)
        db.session.commit()
        # return jsonify({'success': 'OK'})
        return jsonify(
            {
                'posts': post.to_dict(only=('text',))
            }
        )



class PostResource(Resource):
    def get(self, post_id):
        return {'message': f'Get {post_id}'}

    def put(self, post_id):
        return {'message': f'Put {post_id}'}
    
    def delete(self, post_id):
        return {'message': f'Delete {post_id}'}



api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='127.0.0.1', port=8000)
