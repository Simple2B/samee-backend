from typing import Optional, List
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
    solution: List[str]
    type_of_save: str
    amount_of_money: int
    amount_of_savings: Optional[int]
    smoking: str
    sex: str
    tax: int
    scenario_optimistic: Optional[int]
    scenario_pessimistic: Optional[int]
    scenario_realistic: Optional[int]
    final_capital: Optional[int]
    saving_years: Optional[int]
    total_savings: Optional[int]
    fonds_percent: Optional[int]
    savings_percent: Optional[int]
    interest: Optional[int]
    occupation: Optional[str]
    amount_of_fonds: Optional[int]
    marital_status: MaritalStatus


class ClientPhoneValidation(BaseModel):
    client_id: int
    phone_validation_code: str
