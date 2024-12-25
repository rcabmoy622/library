from wtforms import Form, StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField, EmailField, PasswordField, BooleanField
from wtforms.validators import Optional, DataRequired, Length, URL, Email, Regexp

class BookForm(Form):
    title = StringField('Title', validators=[DataRequired(message="A book title is required."), 
                                             Length(min=4, max=80, message="Book title must be between 4 and 80 characters long."),
                                             Regexp(r'^[A-Za-z\s]+$', message="Book title can only contain letters and spaces.")])
    description = TextAreaField('Description', validators=[Optional()])
    author = SelectMultipleField('Authors', validators=[Optional()], choices=[])
    category_id = SelectField('Category', validators=[DataRequired(message="A book category is required.")], choices=[])
    state_id = SelectField('State', validators=[DataRequired(message="A book state is required.")], choices=[])
    image = StringField('Image URL', validators=[Optional(), URL(message="Invalid image URL.")])
    submit = SubmitField('Save Book')


class AuthorForm(Form):
    name = StringField('Full Name', validators=[DataRequired(message="An author name is required."), 
                                                Length(min=4, max=80, message="Author name must be between 4 and 80 characters long."),
                                                Regexp(r'^[A-Za-z\s]+$', message="Author name can only contain letters and spaces.")])
    biography = TextAreaField('Biography', validators=[Optional()])
    book = SelectMultipleField('Books', validators=[Optional()], choices=[])
    image = StringField('Image URL', validators=[Optional(), URL(message="Invalid image URL.")])
    submit = SubmitField('Save Author')

class SignupForm(Form):
    email = EmailField('Email', validators=[DataRequired(message="An email is required."), 
                                            Email()])
    name = StringField('Full Name', validators=[DataRequired(message="Your name is required."), 
                                                Length(min=4, max=80, message="Your name must be between 4 and 80 characters long."),
                                                Regexp(r'^[A-Za-z\s]+$', message="Your name can only contain letters and spaces.")])
    password = PasswordField('Password', validators=[DataRequired(message="A password is required."), 
                                                     Length(min=6, message="Your password must contain at least 6 characters.")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = EmailField('Email', validators=[DataRequired(message="Your email is required."), 
                                            Email()])
    password = PasswordField('Password', validators=[DataRequired(message="Your password is required."), 
                                                     Length(min=6, message="Your password must contain at least 6 characters.")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')

class ProfileForm(Form):
    name = StringField('Full Name', validators=[DataRequired(message="Your name is required."), 
                                                Length(min=4, max=80, message="Your name must be between 4 and 80 characters long."),
                                                Regexp(r'^[A-Za-z\s]+$', message="Your name can only contain letters and spaces.")])
    email = EmailField('Email', validators=[DataRequired(message="An email is required."), 
                                            Email()])
    profilePicture = StringField('Profile Picture URL', validators=[Optional(), URL(message="Invalid image URL.")])
    password = PasswordField('New Password', validators=[Optional(), 
                                                         Length(min=6, message="Your password must contain at least 6 characters.")])
    submit = SubmitField('Update profile')