import os

from flask import Blueprint, session, jsonify
from flask_pydantic import validate
from twilio.rest import Client as TwilioClient

from app.models.client_model import ClientModel, ClientPhoneValidation
from app.models import Client
from app.logger import log

client_blueprint = Blueprint("/client", __name__)

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
service_sid = os.environ.get("SERVICE_SID")


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

    client_verify = TwilioClient(account_sid, auth_token)
    message = client_verify.messages.create(
        messaging_service_sid=service_sid,
        body=client.phone_validation_code,
        to=Client.phone_number
    )

    log(log.INFO, "Client %s successfully added", client.name)
    log(log.INFO, "Message to number: %s has been sent", message.to)
    session["client_id"] = client.id
    return jsonify({"Client_id": client.id})


@client_blueprint.route("/phone_validation", methods=["Post"])
@validate
def phone_validation(body: ClientPhoneValidation):
    if body.id == Client.id:
        if body.phone_validation_code == Client.phone_validation_code:
            Client.phone_valid = True
            Client.save()
            return jsonify(message="Client phone number has been successfully verified", category="success", status=200)
        return jsonify(message="Bad phone verification code!", category="error", status=404)
    return jsonify(message="No such Client id", category="error", status=404)
