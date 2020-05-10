from flask_restful import abort, Resource
from flask import jsonify
from data.db_session import create_session
from data.users import User


def abort_if_user_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user or not user.to_show_private_information:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'surname', 'name', 'age', 'nickname',
                  'picture', 'created_date'))})


class UsersListResource(Resource):
    def get(self):
        session = create_session()
        users = session.query(User).filter(User.to_show_private_information == '1').all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'nickname')) for item in users]})
