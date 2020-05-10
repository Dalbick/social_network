from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserSearchForm(FlaskForm):
    nickname = StringField('Part of user nickname', validators=[DataRequired()])
    submit = SubmitField('Search')
