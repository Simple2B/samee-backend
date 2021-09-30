import pydantic

from flask_wtf.form import _is_submitted
from flask import Blueprint, render_template, url_for, redirect, flash, request, jsonify
from flask_pydantic import validate

from app.models.client_model import ClientModel
from app.models import Client


client_blueprint = Blueprint("/client", __name__)


@client_blueprint.route("/add", methods=["POST"])
@validate()
def add_client_info(body: ClientModel):

    client = Client(
        name=body.name,
        username=body.username,
        email=body.email,
        phone_number=body.phone_number,
        address=body.address,
        zip_plus_town=body.zip_plus_town,
        nationality=body.nationality,
        birthday=body.birthday,
        profession=body.profession,
        guaranteed_solution=body.guaranteed_solution,
        type_of_save=body.type_of_save,
        marital_status=body.marital_status,
        smoking=body.smoking,
        sex=body.sex,
    ).save()
    flash("Client info added successfully!","success")
    return jsonify("OK")