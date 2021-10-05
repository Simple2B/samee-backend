from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr


from .client import(
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
    marital_status: MaritalStatus
    smoking: str
    sex: str
