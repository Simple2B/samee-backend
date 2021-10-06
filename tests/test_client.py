import pytest
from app import db, create_app


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
            "name": "Test Client",
            "username": "test_client1",
            "email": "test_client@test.com",
            "phone_number": "+380522322343",
            "address": "France",
            "zip_plus_town": "43445 Paris",
            "nationality": "french",
            "birthday": "2021-09-29 13:39:53.160495",
            "profession": "teacher 65%",
            "guaranteed_solution": "Yes",
            "type_of_save": "Yearly",
            "amount_of_money": "4124",
            "smoking": "No",
            "sex": "Female",
            "saving_years": "10",
            "total_savings": "150000",
            "fonds_percent": "50",
            "savings_percent": "50",
            "interest": "Salary",
            "occupation": "work",
            "amount_of_fonds": "10000",
            "marital_status": "Unmarried",
        },
        follow_redirects=True,
    )
    assert response
    assert response.status_code == 200

    """Test client info add with bad email"""
    response_bad_email = client.post(
        "/add",
        json={
            "name": "Test Client",
            "username": "test_client2",
            "email": "bad email",
            "phone_number": "+380422342343",
            "address": "France",
            "zip_plus_town": "43445 Paris",
            "nationality": "french",
            "birthday": "2021-09-29 13:39:53.160495",
            "profession": "teacher 65%",
            "guaranteed_solution": "Yes",
            "type_of_save": "Yearly",
            "amount_of_money": "4124",
            "smoking": "No",
            "sex": "Female",
            "saving_years": "10",
            "total_savings": "150000",
            "fonds_percent": "50",
            "savings_percent": "50",
            "interest": "Salary",
            "occupation": "work",
            "amount_of_fonds": "10000",
            "marital_status": "Unmarried",
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
            "name": "Test Client",
            "username": "test_client3",
            "email": "test_client3@test.com",
            "phone_number": "+380422322343",
            "address": "France",
            "zip_plus_town": "43445 Paris",
            "nationality": "french",
            "birthday": "2021-09-29 13:39:53.160495",
            "profession": "teacher 65%",
            "guaranteed_solution": "Yes",
            "type_of_save": "Yearly",
            "amount_of_money": "4124",
            "smoking": "No",
            "sex": "Female",
            "saving_years": "10",
            "total_savings": "150000",
            "fonds_percent": "50",
            "savings_percent": "50",
            "interest": "Salary",
            "occupation": "work",
            "amount_of_fonds": "10000",
            "marital_status": "No",
        },
        follow_redirects=True,
    )
    assert response_enum_object
    assert response_enum_object.status_code == 400
    data = response_enum_object.json
    assert data["validation_error"]["body_params"][0]["msg"] == "value is not a valid enumeration member;"\
        " permitted: 'Unmarried', 'Married', 'Divorced', 'Widowed', 'Legally Separated'"
