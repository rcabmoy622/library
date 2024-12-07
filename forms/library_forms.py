from wtforms import Form, BooleanField, StringField, SubmitField, ValidationError, validators, TextAreaField, DateTimeField, SelectField
import datetime

class BookForm(Form):
    title = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    biography = TextAreaField('Description',[validators.Optional()])
    category_id = SelectField('Category',[validators.DataRequired()], choices=[])
    author = SelectField('Author',[validators.DataRequired()], choices=[])
    state_id = SelectField('State',[validators.DataRequired()], choices=[])
    submit = SubmitField('Save book')

    def validate_due_date(form, field):
        if field.data < datetime.datetime.now():
            raise ValidationError('Datetime can not be previous to right now')