import enum

from app import db
from app.models.utils import ModelMixin


class MaritalStatus(enum.Enum):
    UNMARRIED = "Unmarried"
    MARRIED = "Married"
    DIVORCED = "Divorced"
    WIDOWED = "Widowed"
    SEPARATED = "Legally Separated"


class Smoking(enum.Enum):
    YES = "Yes"
    NO = "No"


class Sex(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"


class TypeOfSave(enum.Enum):
    MONTHLY = "Monthly"
    YEARLY = "Yearly"


class GuaranteedSolution(enum.Enum):
    YES = "Yes"
    NO = "No"


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
    birthday = db.Column(db.Datetime)
    guaranteed_solution = db.Column(db.Enum(GuaranteedSolution), default=GuaranteedSolution.NO)
    type_of_save = db.Column(db.Enum(TypeOfSave), default=TypeOfSave.YEARLY)
    marital_status = db.Column(db.Enum(MaritalStatus), default=MaritalStatus.UNMARRIED)
    smoking = db.Column(db.Enum(Smoking), default=Smoking.NO)
    sex = db.Column(db.Enum(Sex),default=Sex.FEMALE)

    def __repr__(self):
        return f"<{self.id} : {self.username}>"
