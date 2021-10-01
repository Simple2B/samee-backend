from flask import (
    render_template,
    flash,
    Response,
    redirect,
)
from flask_admin import Admin
from flask_admin.actions import action
from flask_admin.contrib import sqla
from flask_admin.base import expose, AdminIndexView

# from flask_security import current_user
from werkzeug.exceptions import HTTPException


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
    # create_template = "admin_page/index.html"
    @action("download", text="Download")
    def  downlad():
        pass
    column_searchable_list = ["email"]
    # column_filters = [
    #     "first_name",
    #     "last_name",
    #     "email",
    #     "country",
    #     "organization",
    #     "authenticated",
    #     "signup_at",
    #     "role",
    # ]

def init_admin(app, db):
    admin = Admin(
        app,
        name="Client Monitoring Panel",
        template_mode="bootstrap3",
    )
    admin.add_views(ClientModelView(Client, db.session))
    return admin
