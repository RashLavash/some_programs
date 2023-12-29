from flask_restful import Resource, reqparse

from flask import jsonify, request, abort

from models import db, Post



parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('text', required=True)
parser.add_argument('author_id', required=True, type=int)


def abort_if_post_doesnt_exists(post_id):
    post = Post.query.get(post_id)

    if not post:
        abort(
            404, 
            message=f"Post with id={post_id} doesn\'t exist."
            )


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
    
        return jsonify(
            {
                'posts': [
                    post.to_dict(only=('title',))
                    for post in posts
                ]
            }
        )


    def post(self):

        args = parser.parse_args()

        post = Post(
            title=args['title'],
            text=args['text'],
            author_id=args['author_id']
        )

        db.session.add(post)
        db.session.commit()
        # return jsonify({'success': 'OK'})
        
        return jsonify(
            {
                'posts': post.to_dict(only=('title',))
                # 'success': 'OK'
            }
        )



class PostResource(Resource):
    def get(self, post_id):
        abort_if_post_doesnt_exists(post_id)
        posts = Post.query.get(post_id)
        # posts = Post.query.filter_by(id=post_id).all()
    
        return jsonify(
            {
                'posts': posts.to_dict(only=(
                    'title', 'text', 'author_id'
                ))              
            }
        )

    def put(self, post_id):
        
        args = parser.parse_args()

        abort_if_post_doesnt_exists(post_id)
        post = Post.query.get(post_id)

        post.title = args['title']
        post.text = args['text']
        post.author_id = args['author_id']
        
        db.session.commit()

        return jsonify(
            {
                'posts': post.to_dict(only=(
                    'title', 'text', 'author_id'
                ))              
            }
        )

        
    
    def delete(self, post_id):
        
        abort_if_post_doesnt_exists(post_id)
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()

        return jsonify(
            {
                'success': 'OK'
            }
        )
