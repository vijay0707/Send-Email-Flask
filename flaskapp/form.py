from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, Email
from wtforms.validators import ValidationError

class SurveyForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=2,max=20)])
    email = StringField(validators=[InputRequired(), Email(message="enter valid email id")]) 

    submit = SubmitField()