import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException
from flask_basicauth import BasicAuth
from flask_bootstrap import Bootstrap
from flask_cors import CORS
# from flask_mail import Mail


# instantiate extensions
login_manager = LoginManager()
db = SQLAlchemy()
basic_auth = BasicAuth()
bootstrap = Bootstrap()
# mail = Mail()


def create_app(environment="development"):

    from config import config
    from app.views import (
        main_blueprint,
        client_blueprint,
    )
    from app.models import (
        Client,
    )

    # Instantiate app.
    app = Flask(__name__)
    CORS(app)

    # Set app config.
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    # Set up extensions.
    db.init_app(app)
    bootstrap.init_app(app)
    basic_auth.init_app(app)
    # mail.init_app(app)

    # Register blueprints.
    app.register_blueprint(main_blueprint)
    app.register_blueprint(client_blueprint)

    # Set up flask login.
    @login_manager.user_loader
    def get_client(id):
        return Client.query.get(int(id))

    login_manager.login_view = "auth.signin"
    login_manager.login_message_category = "info"

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    return app
