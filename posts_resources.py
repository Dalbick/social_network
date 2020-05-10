from flask_restful import abort, Resource
from flask import jsonify
from data.db_session import create_session
from data.posts import Post


def abort_if_post_not_found(post_id):
    session = create_session()
    post = session.query(Post).get(post_id)
    if not post or post.is_private:
        abort(404, message=f"Post {post_id} not found")


class PostsResource(Resource):
    def get(self, post_id):
        abort_if_post_not_found(post_id)
        session = create_session()
        post = session.query(Post).get(post_id)
        return jsonify({'post': post.to_dict(
            only=('id', 'picture', 'description', 'user_id', 'created_date'))})


class PostsListResource(Resource):
    def get(self):
        session = create_session()
        posts = session.query(Post).filter(Post.is_private == '0').all()
        return jsonify({'posts': [item.to_dict(
            only=('id', 'description', 'user_id')) for item in posts]})
