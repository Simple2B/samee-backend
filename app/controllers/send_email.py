from app.logger import log
from config import BaseConfig as cfg
from flask import render_template
from flask_mail import Message

from app.models import Client
from app import mail


def send_mail(client: Client):
    # letter_text = render_template("contact_email.html", client=client)
    log(log.INFO, "Send mail server: %s:%d", cfg.MAIL_SERVER, cfg.MAIL_PORT)
    msg = Message("Samme", sender=cfg.MAIL_FROM, recipients=[client.email])
    msg.html = render_template("contact_email.html", client=client)
    mail.send(msg)
    log(log.INFO, "Message was sent to %s", client.email)
