from flask_restful import abort, Resource
from flask import jsonify
from data.db_session import create_session
from data.comments import Comment


def abort_if_comment_not_found(comment_id):
    session = create_session()
    comment = session.query(Comment).get(comment_id)
    if not comment:
        abort(404, message=f"Comment {comment_id} not found")


class CommentsResource(Resource):
    def get(self, comment_id):
        abort_if_comment_not_found(comment_id)
        session = create_session()
        comment = session.query(Comment).get(comment_id)
        return jsonify({'comment': comment.to_dict(
            only=('id', 'text', 'user_id', 'post_id', 'created_date'))})


class CommentsListResource(Resource):
    def get(self):
        session = create_session()
        comments = session.query(Comment).all()
        return jsonify({'comments': [item.to_dict(
            only=('id', 'text', 'user_id', 'post_id')) for item in comments]})
