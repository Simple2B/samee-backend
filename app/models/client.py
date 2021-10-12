from enum import Enum
from random import randint
from datetime import datetime

from app import db
from app.models.utils import ModelMixin


def gen_validation_code() -> str:
    return str.join("", [str(randint(0, 9)) for i in range(6)])


class MaritalStatus(str, Enum):
    SINGLE = "Célibataire"
    MARRIED = "Marié(e)"
    DIVORCED = "Divorcé(e)"
    WIDOWED = "Veuf(ve)"


class Client(db.Model, ModelMixin):

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(256))
    street = db.Column(db.String(256))
    street_number = db.Column(db.String(6))
    zip = db.Column(db.String(32))
    birthday = db.Column(db.String)
    profession = db.Column(db.String(128))
    solution = db.Column(db.String)
    type_of_save = db.Column(db.String(32))
    amount_of_money = db.Column(db.Integer)
    smoking = db.Column(db.String(16))
    sex = db.Column(db.String(32))
    saving_years = db.Column(db.Integer)
    total_savings = db.Column(db.Integer)
    amount_of_savings = db.Column(db.Integer)
    fonds_percent = db.Column(db.Integer)
    savings_percent = db.Column(db.Integer)
    interest = db.Column(db.Integer)
    occupation = db.Column(db.String(64))
    amount_of_fonds = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    scenario_optimistic = db.Column(db.Integer)
    scenario_pessimistic = db.Column(db.Integer)
    scenario_realistic = db.Column(db.Integer)
    final_capital = db.Column(db.Integer)
    marital_status = db.Column(db.Enum(MaritalStatus), default=MaritalStatus.SINGLE)
    phone_valid = db.Column(db.Boolean, default=False)
    phone_validation_code = db.Column(db.String(6), default=gen_validation_code)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<{self.id} : {self.username}>"
