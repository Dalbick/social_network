from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    picture = FileField('Picture', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    is_private = BooleanField('Private post')
    submit = SubmitField('Submit')
