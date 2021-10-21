import smtplib

from app.logger import log
from config import BaseConfig


GMAIL_USER = BaseConfig.GMAIL_USER
GMAIL_PASSWORD = BaseConfig.GMAIL_PASSWORD


def send_email(receiver):
    sent_from = GMAIL_USER
    to = receiver
    subject = 'Lorem ipsum dolor sit amet'
    body = 'consectetur adipiscing elit'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(GMAIL_USER, GMAIL_PASSWORD)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        log(log.INFO, "Email sent successfully!")
        # print("Email sent successfully!")
    except Exception as ex:
        log(log.ERROR, "Something went wrong: [%s] ", ex)
        # print("Something went wrong: ", ex)
