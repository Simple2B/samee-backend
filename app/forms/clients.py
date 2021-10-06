from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SelectField
from wtforms.fields.core import DateTimeField
from wtforms.validators import DataRequired, Email

from app.models import (
    Client,
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
    guaranteed_solution = StringField("Solution", validators=[DataRequired()])
    type_of_save = StringField("Type of save", validators=[DataRequired()])
    amount_of_money = StringField("amount_of_money", validators=[DataRequired()])
    smoking = StringField("Smoking", validators=[DataRequired()])
    sex = StringField("Sex", validators=[DataRequired()])
    saving_years = StringField("saving_years", validators=[DataRequired()])
    total_savings = StringField("total_savings", validators=[DataRequired()])
    fonds_percent = StringField("fonds_percent", validators=[DataRequired()])
    savings_percent = StringField("saving_years", validators=[DataRequired()])
    interest = StringField("interest", validators=[DataRequired()])
    occupation = StringField("occupation", validators=[DataRequired()])
    amount_of_fonds = StringField("amount_of_fonds", validators=[DataRequired()])
    marital_status = SelectField("marital_status", choices=MaritalStatus, default=MaritalStatus.UNMARRIED)

    def validate_email(form, field):
        if Client.query.filter_by(email=field.data).first() is not None:
            raise ValidationError('This email is already registered.')
