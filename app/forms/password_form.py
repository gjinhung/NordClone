from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class PasswordForm(FlaskForm):
    website = StringField("website", validators=[Length(max=500)])
    email = StringField("email", validators=[Length(max=500)])
    username = StringField("username", validators=[DataRequired(), Length(max=500)])
    password = StringField("password", validators=[DataRequired(), Length(max=500)])
    name = StringField("name", validators=[Length(max=500)])
    submit = SubmitField("Submit")
