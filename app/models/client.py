from enum import Enum
# from sqlalchemy import Column, Integer, DateTime

from app import db
from app.models.utils import ModelMixin


class MaritalStatus(str, Enum):
    UNMARRIED = "Unmarried"
    MARRIED = "Married"
    DIVORCED = "Divorced"
    WIDOWED = "Widowed"
    SEPARATED = "Legally Separated"


class Client(db.Model, ModelMixin):

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String(256))
    zip_plus_town = db.Column(db.String(32))
    nationality = db.Column(db.String(128))
    birthday = db.Column(db.String)
    profession = db.Column(db.String(128))
    guaranteed_solution = db.Column(db.String(32))
    type_of_save = db.Column(db.String(32))
    amount_of_money = db.Column(db.String(64))
    smoking = db.Column(db.String(16))
    sex = db.Column(db.String(32))
    saving_years = db.Column(db.String(32))
    total_savings = db.Column(db.String(32))
    fonds_percent = db.Column(db.String(32))
    savings_percent = db.Column(db.String(32))
    interest = db.Column(db.String(32))
    occupation = db.Column(db.String(64))
    amount_of_fonds = db.Column(db.String(32))
    marital_status = db.Column(db.Enum(MaritalStatus), default=MaritalStatus.UNMARRIED)

    def __repr__(self):
        return f"<{self.id} : {self.username}>"
