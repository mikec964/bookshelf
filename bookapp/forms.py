from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostBook(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    isbn = StringField('ISBN', validators=[Length(min=9, max=17)])
    submit = SubmitField('Post')
