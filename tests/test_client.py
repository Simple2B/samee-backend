import pytest
from app import db, create_app
from config import BaseConfig

PHONE_NUMBER = BaseConfig.TWILIO_PHONE_NUMBER


@pytest.fixture
def client():
    app = create_app(environment="testing")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


def test_add_client_info(client):
    response = client.post(
        "/add",
        json={
            "first_name": "Test",
            "last_name": "Client",
            "email": "test@test.com",
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
            "tax": "11254",
            "scenario_optimistic": "1244213",
            "scenario_pessimistic": "13123",
            "scenario_realistic": "13125412",
            "final_capital": "12315123",
            "saving_years": "12",
            "total_savings": "12412534",
            "fonds_percent": "21",
            "savings_percent": "15",
            "interest": "12125412",
            "occupation": "teacher",
            "amount_of_fonds": "1242123",
            "marital_status": "Célibataire",
        },
        follow_redirects=True,
    )
    assert response
    assert response.status_code == 200

    """Test client info add with bad email"""
    response_bad_email = client.post(
        "/add",
        json={
            "first_name": "Test",
            "last_name": "Client",
            "email": "funny",
            "city": "Boston",
            "street": "test street",
            "street_number": "45",
            "phone_number": "+380423453234",
            "zip": "52345",
            "birthday": "2086-10-08 18:00:37",
            "profession": "teacher",
            "solution": "granties",
            "type_of_save": "monthly",
            "amount_of_money": "25123",
            "amount_of_savings": "12513212",
            "smoking": "No",
            "sex": "homme",
            "tax": "11254",
            "scenario_optimistic": "1244213",
            "scenario_pessimistic": "13123",
            "scenario_realistic": "13125412",
            "final_capital": "12315123",
            "saving_years": "12",
            "total_savings": "12412534",
            "fonds_percent": "21",
            "savings_percent": "15",
            "interest": "12125412",
            "occupation": "teacher",
            "amount_of_fonds": "1242123",
            "marital_status": "Célibataire",
        },
        follow_redirects=True,
    )
    assert response_bad_email
    assert response_bad_email.status_code == 400, response_bad_email
    data = response_bad_email.json
    assert data["validation_error"]["body_params"][0]["msg"] == "value is not a valid email address"

    """Test client info add with bad enum object"""
    response_enum_object = client.post(
        "/add",
        json={
            "first_name": "Test",
            "last_name": "Client",
            "email": "test@test.com",
            "city": "Boston",
            "street": "test street",
            "street_number": "45",
            "phone_number": "+380423453234",
            "zip": "52345",
            "birthday": "2086-10-08 18:00:37",
            "profession": "teacher",
            "solution": "granties",
            "type_of_save": "monthly",
            "amount_of_money": "25123",
            "amount_of_savings": "12513212",
            "smoking": "No",
            "sex": "homme",
            "tax": "11254",
            "scenario_optimistic": "1244213",
            "scenario_pessimistic": "13123",
            "scenario_realistic": "13125412",
            "final_capital": "12315123",
            "saving_years": "12",
            "total_savings": "12412534",
            "fonds_percent": "21",
            "savings_percent": "15",
            "interest": "12125412",
            "occupation": "teacher",
            "amount_of_fonds": "1242123",
            "marital_status": "married",
        },
        follow_redirects=True,
    )
    assert response_enum_object
    assert response_enum_object.status_code == 400
    data = response_enum_object.json
    assert data["validation_error"]["body_params"][0]["msg"] == "value is not a valid enumeration member;"\
        " permitted: 'Célibataire', 'Marié(e)', 'Divorcé(e)', 'Veuf(ve)'"

    """Test Client phone verification"""
    client_phone_verification = client.post(
        "/phone_validation",
        json={
            "id": "1",
            "phone_validation_code": "235674",
        },
        follow_redirects=True,
    )
    assert client_phone_verification
