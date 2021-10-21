from flask import Blueprint, jsonify, abort
from flask_pydantic import validate

from app.models.client_model import ClientModel, ClientPhoneValidation
from app.models import Client
from app.logger import log
from app.controllers.sms_send import send_sms
# from app.controllers.send_email import send_email


client_blueprint = Blueprint("/client", __name__, url_prefix="/api")


@client_blueprint.route("/add", methods=["POST"])
@validate()
def add_client_info(body: ClientModel):

    client = Client(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        phone_number=body.phone_number,
        city=body.city,
        street=body.street,
        street_number=body.street_number,
        zip=body.zip,
        birthday=body.birthday,
        profession=body.profession,
        solution=body.solution,
        type_of_save=body.type_of_save,
        amount_of_money=body.amount_of_money,
        smoking=body.smoking,
        sex=body.sex,
        saving_years=body.saving_years,
        total_savings=body.total_savings,
        amount_of_savings=body.amount_of_savings,
        fonds_percent=body.fonds_percent,
        savings_percent=body.savings_percent,
        interest=body.interest,
        occupation=body.occupation,
        amount_of_fonds=body.amount_of_fonds,
        tax=body.tax,
        scenario_optimistic=body.scenario_optimistic,
        scenario_pessimistic=body.scenario_pessimistic,
        scenario_realistic=body.scenario_realistic,
        final_capital=body.final_capital,
        marital_status=body.marital_status,
    ).save()
    log(log.INFO, "Client %s successfully added", client.first_name)
    try:
        send_sms(client.phone_validation_code, client.phone_number)
        log(log.INFO, "Sms was sent to %s number", client.phone_number)
        log(log.INFO, "Sms was sent to %s email", client.email)
        return jsonify({"Client_id": client.id})
    except Exception as e:
        log(log.ERROR, "Sms wasn't send! Error: [%s]", e)
        client.delete()
        abort(404, description="Can't send SMS")


@client_blueprint.route("/phone_validation", methods=["Post"])
@validate()
def phone_validation(body: ClientPhoneValidation):
    existed_client = Client.query.filter_by(id=body.client_id).first()
    if existed_client:
        if body.phone_validation_code == existed_client.phone_validation_code:
            existed_client.phone_valid = True
            existed_client.save()
            return jsonify(dict(message="Client phone number has been successfully verified", category="success"))
    # try:
    #     send_email(existed_client.email)
    # except Exception as e:
    #     log(log.ERROR, "Sms wasn't send! Error: [%s]", e)
