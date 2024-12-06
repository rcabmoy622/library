from wtforms import Form, BooleanField, StringField, SubmitField, ValidationError, validators, TextAreaField, DateTimeField, SelectField
import datetime

class BookForm(Form):
    title = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    description = TextAreaField('Description',[validators.Optional()])
    due_date = DateTimeField('Due date',[validators.Optional()], format='%Y-%m-%d %H:%M:%S')
    reminder = BooleanField('Send me a reminder',[])
    category_id = SelectField('Category',[validators.DataRequired()], choices=[])
    submit = SubmitField('Guardar')

    def validate_due_date(form, field):
        if field.data < datetime.datetime.now():
            raise ValidationError('Datetime can not be previous to right now')