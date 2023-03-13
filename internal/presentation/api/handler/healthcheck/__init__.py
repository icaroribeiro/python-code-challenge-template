from flask_restx import Model, Namespace, fields

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
    "MessageModel",
    {"message": fields.String()},
)

error_model = health_check_namespace.model(
    "ErrorModel",
    {"error": fields.String()},
)
