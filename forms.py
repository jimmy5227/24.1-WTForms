from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, URL, Optional, AnyOf, NumberRange


class AddPetForm(FlaskForm):

    pet_name = StringField("Pet Name", validators=[
                           InputRequired(message="Pet name cannot be empty")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[
                          AnyOf(['cat', 'dog', 'porcupine']), InputRequired(message="Species name cannot be empty")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(
        require_tld=True, message="Please enter a valid photo link.")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(
        min=1, max=30, message='Age must be between 1-30')])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL(
        require_tld=True, message="Please enter a valid photo link.")])
    notes = StringField("Notes", validators=[Optional()])
    availability = SelectField("Availability", choices=[
        ('True', 'Available'), ('False', 'Not Available')])
