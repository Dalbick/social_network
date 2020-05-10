import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin


class Comment(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'comments'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('posts.id'))
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    user = orm.relation('User', back_populates='comments')
    post = orm.relation('Post', back_populates='comments')
