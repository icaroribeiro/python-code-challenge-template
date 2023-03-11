from flask_restx import Namespace, fields, reqparse

# authorizations = {
#     "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "Authorization"}
# }

health_check_namespace = Namespace(
    "health check",
    description="It refers to the operation related to health check.",
    path="/api",
    # authorizations=authorizations,
)

message_model = health_check_namespace.model(
    "Message",
    {"message": fields.String()},
)

error_model = health_check_namespace.model(
    "Error",
    {"error": fields.String()},
)
