from flask import Blueprint, jsonify
from flask_pydantic import validate

from app.models.client_model import ClientModel, ClientPhoneValidation
from app.models import Client
from app.logger import log
from app.controllers.twilio import sent_sms

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
    log(log.INFO, "Client %s successfully added", client.name)
    sent_sms(client.phone_validation_code, client.phone_number)
    log(log.INFO, "Sms was sent to %s number", client.phone_number)
    return jsonify({"Client_id": client.id})


@client_blueprint.route("/phone_validation", methods=["Post"])
@validate
def phone_validation(body: ClientPhoneValidation):
    existed_client = Client.query.filter_by(id=body.id).first()
    if existed_client:
        if body.phone_validation_code == existed_client.phone_validation_code:
            existed_client.phone_valid = True
            existed_client.save()
            return jsonify(dict(message="Client phone number has been successfully verified", category="success"))
        else:
            return jsonify(dict(message="Bad phone verification code!", category="error")), 404
    else:
        return jsonify(dict(message="No such Client id", category="error")), 404
