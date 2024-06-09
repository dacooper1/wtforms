from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    ''' For for adding pets'''

    name = StringField("Pet Name",validators=[InputRequired()])
    species = SelectField("Species", validators=[InputRequired()], choices=[('cat', 'cat'), ('dog', 'dog'), ('pc','porcupine')])
    img = StringField("Photo URL", validators=[URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message='Age range 0-30')])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    img = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", false_values=None)
