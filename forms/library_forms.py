from wtforms import Form, StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField, EmailField, PasswordField, BooleanField
from wtforms.validators import Optional, DataRequired, Length, URL, Email

class BookForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=80)])
    description = TextAreaField('Description', validators=[Optional()])
    author = SelectMultipleField('Authors', validators=[Optional()], choices=[])
    category_id = SelectField('Category', validators=[DataRequired()], choices=[])
    state_id = SelectField('State', validators=[DataRequired()], choices=[])
    image = StringField('Image URL', validators=[Optional(), URL(message="Invalid URL")])
    submit = SubmitField('Save Book')


class AuthorForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=80)])
    biography = TextAreaField('Biography', validators=[Optional()])
    book = SelectMultipleField('Books', validators=[Optional()], choices=[])
    image = StringField('Image URL', validators=[Optional(), URL(message="Invalid URL")])
    submit = SubmitField('Save Author')

class SignupForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')