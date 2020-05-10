from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostSearchForm(FlaskForm):
    description = StringField('Part of post description', validators=[DataRequired()])
    submit = SubmitField('Search')
