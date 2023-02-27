from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify
from flask_api import status

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.di.di import AppContainer

blueprint = Blueprint("healthcheck_route", __name__)


@blueprint.route("/status", methods=["GET"])
@inject
def get_status(
    service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
):
    if not service.get_status():
        return (
            jsonify({"error": "the app is not ready to work as expected"}),
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return jsonify({"message": "everything is up and running"}), status.HTTP_200_OK
