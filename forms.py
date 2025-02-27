from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password')])

class ChapterForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    is_pro = BooleanField('Pro Content')
    order = StringField('Order')

class SubChapterForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    chapter_id = SelectField('Chapter', coerce=int)
    order = StringField('Order')

class ContentForm(FlaskForm):
    content_type = SelectField('Type', choices=[
        ('text', 'Text'),
        ('video', 'Video URL'),
        ('link', 'External Link')
    ])
    content = TextAreaField('Content', validators=[DataRequired()])
    order = StringField('Order')
