import pytest

from app import db, create_app
from config import BaseConfig


PHONE_NUMBER = BaseConfig.TWILIO_PHONE_NUMBER


@pytest.fixture
def client():
    app = create_app(environment="testing")
    # app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


@pytest.mark.skipif(PHONE_NUMBER="Please set twilio phone number", reason="Need set test phone number")
def test_send_sms(client):
    """Create client"""
    create_client_response = client.post(
        "/api/add",
        json={
            "first_name": "Test",
            "last_name": "Client",
            "email": "ekedesh@gmail.com",
            "city": "Boston",
            "street": "test street",
            "street_number": "45",
            "phone_number": PHONE_NUMBER,
            "zip": "52345",
            "birthday": "2086-10-08 18:00:37",
            "profession": "teacher",
            "solution": "granties",
            "type_of_save": "monthly",
            "amount_of_money": "25123",
            "amount_of_savings": "12513212",
            "smoking": "No",
            "sex": "homme",
            "tax": 11254,
            "scenario_optimistic": "1244213",
            "scenario_pessimistic": "13123",
            "scenario_realistic": "13125412",
            "final_capital": "12315123",
            "saving_years": "12",
            # "total_savings": "12412534",
            "fonds_percent": "21",
            "savings_percent": "15",
            "interest": "12125412",
            "occupation": "teacher",
            "amount_of_fonds": "1242123",
            "marital_status": "Célibataire",
        },
        follow_redirects=True,
    )
    assert create_client_response
    assert create_client_response.status_code == 200
    data = create_client_response.json
    client_id = data["Client_id"]
    phone_validation_code = data["phone_validation_code"]

    """Test phone validation and mail sending """
    phone_validation_response = client.post(
        "/api/phone_validation",
        json={
            "client_id": client_id,
            "phone_validation_code": phone_validation_code
        }
    )
    assert phone_validation_response
    assert phone_validation_response.status_code == 200
