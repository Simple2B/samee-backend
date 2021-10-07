from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr

from .client import (
    MaritalStatus,
)


class ClientModel(BaseModel):
    name: str
    username: str
    email: EmailStr
    phone_number: str
    address: str
    zip_plus_town: str
    nationality: str
    birthday: datetime
    profession: str
    guaranteed_solution: str
    type_of_save: str
    amount_of_money: str
    smoking: str
    sex: str
    saving_years: str
    total_savings: str
    fonds_percent: str
    savings_percent: str
    interest: str
    occupation: str
    amount_of_fonds: str
    marital_status: MaritalStatus


class ClientPhoneValidation(BaseModel):
    id: int
    phone_validation_code: str
