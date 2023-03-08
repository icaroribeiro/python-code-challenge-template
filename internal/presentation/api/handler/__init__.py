from flask import Blueprint
from flask_restx import Api

from internal.presentation.api.handler.healthcheck import (
    ns_test as health_check_namespace,
)

blueprint = Blueprint("documented_api", __name__, url_prefix="/documented_api")

api_extension = Api(
    blueprint,
    title="X Tech Challenge",
    version="1.0",
    description="A REST API developed using Python programming language and Postgres database.",
    doc="/docs",
)

api_extension.add_namespace(health_check_namespace)
