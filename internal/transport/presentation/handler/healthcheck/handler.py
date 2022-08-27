from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.application.service.healthcheck.service import TestService
from internal.di.di import AppContainer

blueprint = Blueprint("healthcheck_route", __name__)


@blueprint.route("/status", methods=["GET"])
@inject
def get_status(
    service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
):
    # @blueprint.route("/status", methods=["GET"])
    # def get_status():
    #     session = MySession()
    #     service = HealthCheckService(session=session)
    if service.get_status():
        return jsonify({"message": "everything is up and running"}), 200

    return jsonify({"error": "the app is not ready to work as expected"}), 500


@blueprint.route("/status2", methods=["GET"])
@inject
def get_status2(
    service: TestService = Provide[AppContainer.service.test_service],
):
    print("service.get_test(): ", service.get_test())

    return jsonify({"message": "everything is up and running"}), 200
