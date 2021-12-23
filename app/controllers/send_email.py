from app.logger import log
from config import BaseConfig as cfg
from flask import render_template
from flask_mail import Message

from app.models import Client
from app import mail


def send_mail(client: Client):
    # letter_text = render_template("contact_email.html", client=client)
    log(log.INFO, "Send mail server: %s:%d", cfg.MAIL_SERVER, cfg.MAIL_PORT)
    subject = "Confirmation envoi du formulaire"
    msg = Message(subject=subject, sender=cfg.MAIL_FROM, recipients=[client.email])
    msg.html = render_template("contact_email.html", client=client)
    mail.send(msg)
    log(log.INFO, "Message was sent to %s", client.email)


def send_mail_to_owner(client: Client):
    # letter_text = render_template("contact_email.html", client=client)
    log(log.INFO, "Send mail server: %s:%d", cfg.MAIL_SERVER, cfg.MAIL_PORT)
    subject = "We have a new lead!"
    msg = Message(subject=subject, sender=cfg.MAIL_FROM, recipients=[cfg.OWNER_MAIL])
    msg.html = render_template("owner_email.html", client=client)
    mail.send(msg)
    log(log.INFO, "Message was sent to %s", client.email)
