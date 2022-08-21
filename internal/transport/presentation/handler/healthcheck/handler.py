from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.di.di import AppContainer

blueprint = Blueprint("healthcheck_route", __name__)


@blueprint.route("/status", methods=["GET"])
@inject
def get_status(
    service: HealthCheckService = Provide[AppContainer.healthcheck_service],
):
    if service.get_status():
        return jsonify({"message": "everything is up and running"}), 200

    return jsonify({"error": "the app is not ready to work as expected"}), 500
