from flask import (
    Response,
    redirect,
)
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.base import expose, AdminIndexView
from werkzeug.exceptions import HTTPException

from app.logger import log
from app import basic_auth
from app.models import Client


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                "You could not be authenticated. Please refresh the page.",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            ),
        )


class MyView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render("admin_page/index.html")


class ClientModelView(sqla.ModelView):
    column_searchable_list = ["email"]
    can_export = True

    def is_accessible(self):
        if not basic_auth.authenticate():
            log(log.WARNING, "Not authenticated.")
            raise AuthException("Not authenticated.")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


def init_admin(app, db):
    admin = Admin(
        app,
        name="Client Monitoring Panel",
        template_mode="bootstrap3",
    )
    admin.add_views(ClientModelView(Client, db.session))
    return admin
