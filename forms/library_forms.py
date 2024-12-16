from wtforms import Form, StringField, SubmitField, validators, TextAreaField, SelectField, SelectMultipleField
import datetime

class BookForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=80), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Optional()])
    author = SelectMultipleField('Authors', [validators.Optional()], choices=[])
    category_id = SelectField('Category', [validators.DataRequired()], choices=[])
    state_id = SelectField('State', [validators.DataRequired()], choices=[])
    image = StringField('Image URL', [validators.Optional(), validators.URL(message="Invalid URL")])
    submit = SubmitField('Save book')


class AuthorForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    biography = TextAreaField('Biography', [validators.Optional()])
    book = SelectMultipleField('Books', [validators.Optional()], choices=[])
    image = StringField('Image URL', [validators.Optional(), validators.URL(message="Invalid URL")])
    submit = SubmitField('Save author')