from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr

from .client import (
    MaritalStatus,
)


class ClientModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    city: str
    street: str
    street_number: str
    phone_number: str
    zip: str
    birthday: str
    profession: str
    solution: str
    type_of_save: str
    amount_of_money: str
    amount_of_savings: Optional[str]
    smoking: str
    sex: str
    tax: str
    scenario_optimistic: Optional[str]
    scenario_pessimistic: Optional[str]
    scenario_realistic: Optional[str]
    final_capital: Optional[str]
    saving_years: Optional[str]
    total_savings: Optional[str]
    fonds_percent: Optional[str]
    savings_percent: Optional[str]
    interest: Optional[str]
    occupation: Optional[str]
    amount_of_fonds: Optional[str]
    marital_status: MaritalStatus


class ClientPhoneValidation(BaseModel):
    client_id: int
    phone_validation_code: str
