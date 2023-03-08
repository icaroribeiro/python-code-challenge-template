from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify
from flask_api import status
from flask_restx import Namespace, Resource, fields, reqparse

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.di.di import AppContainer

# Namespace
ns_test = Namespace("test", description="a test namespace")

# Models
custom_greeting_model = ns_test.model(
    "Custom",
    {
        "greeting": fields.String(required=True),
        "id": fields.Integer(required=True),
    },
)

# Parser
custom_greeting_parser = reqparse.RequestParser()
custom_greeting_parser.add_argument("greeting", required=True, location="json")


custom_greetings = list()


@inject
@ns_test.route("/kkk")
class Hello(Resource):
    @inject
    @ns_test.doc("say_hello")
    def get(
        self,
        service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
    ):
        print("EEEE")
        if not service.get_status():
            print("BBB")
            return (
                jsonify({"error": "the app is not ready to work as expected"}),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        print("CCC")
        return jsonify({"message": "everything is up and running"}), status.HTTP_200_OK


# from flask_api import status
# from flask_restx import Namespace, Resource, fields
#
# namespace = Namespace(
#     "health check", "It refers to the operations related to healthcheck."
# )
#
# status_model = namespace.model(
#     "Status",
#     {"message": fields.String},
# )
#
# namespace.route("/status")
#
#
# class HealthCheck(Resource):
#     @namespace.response(status.HTTP_200_OK, "OK")
#     def get(self):
#         """ffefef"""
#         return {}, status.HTTP_200_OK
