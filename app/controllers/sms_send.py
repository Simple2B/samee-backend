from twilio.rest import Client as TwilioClient

from config import BaseConfig
from app.logger import log

ACCOUNT_SID = BaseConfig.TWILIO_ACCOUNT_SID
AUTH_TOKEN = BaseConfig.TWILIO_AUTH_TOKEN
SERVICE_SID = BaseConfig.TWILIO_SERVICE_SID
# ACCOUNT_SID = config.

print("ACCOUNT_SID:", ACCOUNT_SID)


def send_sms(phone_validation_code, phone_number):
    try:
        client_verify = TwilioClient(ACCOUNT_SID, AUTH_TOKEN)
        message = client_verify.messages.create(
            messaging_service_sid=SERVICE_SID,
            # messaging_service_sid="MG2989696df239452604dd00c045c8455a",
            body=phone_validation_code,
            to=phone_number
        )
        log(log.INFO, "Message to number: %s has been sent", message.to)
        return f"Message to number: {message.to} has been sent"
    except Exception as error:
        log(log.ERROR, "Message wasn't send: %s", error)
        return None
# send_sms("532513", "+380634136800")
