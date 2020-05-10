from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')
