import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
import sqlalchemy.orm as orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    picture = sqlalchemy.Column(sqlalchemy.String)
    to_show_private_information = sqlalchemy.Column(sqlalchemy.Boolean)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    posts = orm.relation('Post', back_populates='user')
    comments = orm.relation('Comment', back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
