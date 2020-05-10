import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin


class Post(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'posts'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    picture = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    user = orm.relation('User', back_populates='posts')
    comments = orm.relation('Comment', back_populates='post')
