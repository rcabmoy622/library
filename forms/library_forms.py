from wtforms import Form, BooleanField, StringField, SubmitField, ValidationError, validators, TextAreaField, DateTimeField, SelectField
import datetime

class BookForm(Form):
    title = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    description = TextAreaField('Description',[validators.Optional()])
    author = SelectField('Author',[validators.DataRequired()], choices=[])
    category_id = SelectField('Category',[validators.DataRequired()], choices=[])
    state_id = SelectField('State',[validators.DataRequired()], choices=[])
    submit = SubmitField('Save book')


class AuthorForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    biography = TextAreaField('Description',[validators.Optional()])
    book = SelectField('Author',[validators.DataRequired()], choices=[])
    submit = SubmitField('Save author')