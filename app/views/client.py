from flask import Blueprint, flash, jsonify
from flask_pydantic import validate


from app.models.client_model import ClientModel
from app.models import Client
from app.logger import log

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
        amount_of_money=body.amount_of_money,
        smoking=body.smoking,
        sex=body.sex,
        saving_years=body.saving_years,
        total_savings=body.total_savings,
        fonds_percent=body.fonds_percent,
        savings_percent=body.savings_percent,
        interest=body.interest,
        occupation=body.occupation,
        amount_of_fonds=body.amount_of_fonds,
        marital_status=body.marital_status,
    ).save()
    flash("Client info added successfully!", "success")
    log(log.INFO, "Client %s successfully added", client.name)
    return jsonify("OK")
