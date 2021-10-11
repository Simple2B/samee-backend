import pytest
from app import db, create_app
from config import BaseConfig

from app.controllers.sms_send import send_sms

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


@pytest.mark.skipif(PHONE_NUMBER is None, reason="Need set test phone number")
def test_send_sms(client):
    sms_test = send_sms("532513", PHONE_NUMBER)
    assert sms_test == f"Message to number: {PHONE_NUMBER} has been sent"
