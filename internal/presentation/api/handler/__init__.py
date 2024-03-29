from flask import Blueprint
from flask_restx import Api

from internal.presentation.api.handler.healthcheck import health_check_namespace
from internal.presentation.api.handler.user import user_namespace

blueprint = Blueprint("api", __name__, url_prefix="")

api_extension = Api(
    blueprint,
    title="X Tech Challenge",
    version="1.0",
    description="A REST API developed using Python programming language, Postgres database and Docker container.",
    doc="/apidoc",
)

api_extension.add_namespace(health_check_namespace)
api_extension.add_namespace(user_namespace)
