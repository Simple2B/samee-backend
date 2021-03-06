# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = "Samee backend"
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "Ensure you set a secret key, this is important!"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

    BASIC_AUTH_USERNAME = os.environ.get(
        "BASIC_AUTH_USERNAME", "Please set admin username"
    )
    BASIC_AUTH_PASSWORD = os.environ.get(
        "BASIC_AUTH_PASSWORD", "Please set admin password"
    )

    """Twilio configuration"""
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "Please set twilio account sid")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "Please set twilio auth token")
    TWILIO_SERVICE_SID = os.environ.get("TWILIO_SERVICE_SID", "Please set twilio service sid")
    TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER", "Please set twilio phone number")

    """Email service configuration"""
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "Please set mail user")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "Please set mail user password")
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "Please set mail server")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 465))
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_FROM = os.environ.get("MAIL_FROM", "Please set mail from")
    MAIL_SUBJECT = os.environ.get("MAIL_SUBJECT", "No subject")
    OWNER_MAIL = os.environ.get("OWNER_MAIL", "Please set owner mail")

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEVEL_DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "database-devel.sqlite3"),
    )


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "database-test.sqlite3"),
    )


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "db/database.sqlite3")
    )
    WTF_CSRF_ENABLED = True


config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
