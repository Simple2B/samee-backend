from twilio.rest import Client as TwilioClient

from config import BaseConfig
from app.logger import log

ACCOUNT_SID = BaseConfig.TWILIO_ACCOUNT_SID
AUTH_TOKEN = BaseConfig.TWILIO_AUTH_TOKEN
SERVICE_SID = BaseConfig.TWILIO_SERVICE_SID


def sent_sms(phone_validation_code, phone_number):
    client_verify = TwilioClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client_verify.messages.create(
        messaging_service_sid=SERVICE_SID,
        body=phone_validation_code,
        to=phone_number
    )
    log(log.INFO, "Message to number: %s has been sent", message.to)
