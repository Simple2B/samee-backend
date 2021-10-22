from app.logger import log
from config import BaseConfig as cfg
# from flask import render_template
from flask_mail import Mail, Message
from flask import current_app

from app.models import Client


def send_mail(client: Client):
    mail = Mail(current_app)
    # letter_text = render_template("contact_email.html", client=client)
    msg = Message("Samme", sender=cfg.MAIL_FROM, recipients=client.email)
    msg.body = "Hello world"
    log(log.INFO, "Message was sent to %s", client.email)
    mail.send(msg)
