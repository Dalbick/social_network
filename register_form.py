from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, FileField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    picture = FileField('Profile picture', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    to_show_private_information = BooleanField('Show your private information to other users (surname, name and age)')
    submit = SubmitField('Submit')
