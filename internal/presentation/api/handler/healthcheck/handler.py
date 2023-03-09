from dependency_injector.wiring import Closing, Provide, inject
from flask import Blueprint, jsonify
from flask_api import status
from flask_restx import Namespace, Resource, fields, reqparse

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.di.di import AppContainer
from internal.presentation.api.handler.healthcheck import ns_test


@ns_test.route("/")
class Hello(Resource):
    @inject
    def __init__(
        self,
        api=None,
        service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
        *args,
        **kwargs
    ):
        self.service = service
        super().__init__(api, *args, **kwargs)

    @ns_test.doc("say_hello")
    def get(self):
        if not self.service.get_status():
            return (
                {"error": "the app is not ready to work as expected"},
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return {"message": "everything is up and running"}, status.HTTP_200_OK

    # @ns_test.doc("say_hello")
    # @inject
    # def get(
    #     self,
    #     service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
    # ):
    #     if not service.get_status():
    #         return (
    #             {"error": "the app is not ready to work as expected"},
    #             status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         )
    #
    #     return {"message": "everything is up and running"}, status.HTTP_200_OK
