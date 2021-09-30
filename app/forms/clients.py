from re import S
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SelectField
from wtforms.fields.core import DateTimeField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from app.models import (
    Client,
    GuaranteedSolution,
    Sex,
    Smoking,
    TypeOfSave,
    MaritalStatus,
)

class ClientInfoFOrm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    zip_plus_town = StringField("Zip + Town", validators=[DataRequired()])
    nationality = StringField("Nationality", validators=[DataRequired()])
    birthday = DateTimeField("Birthday", validators=[DataRequired()])
    profession = StringField("Profession", validators=[DataRequired()])
    guaranteed_solution = SelectField("Solution", choices=GuaranteedSolution, default=GuaranteedSolution.NO)
    type_of_save = SelectField("Type of save", choices=TypeOfSave, default=TypeOfSave.YEARLY)
    marital_status = SelectField("marital_status", choices=MaritalStatus, default=MaritalStatus.UNMARRIED)
    smoking = SelectField("Smoking", choices=Smoking, default=Smoking.NO)
    sex = SelectField("Sex", choices=Sex, default=Sex.FEMALE)

    def validate_email(form, field):
        if Client.query.filter_by(email=field.data).first() is not None:
            raise ValidationError('This email is already registered.')