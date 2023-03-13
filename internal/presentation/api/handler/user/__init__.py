from flask_restx import Namespace, fields

user_namespace = Namespace(
    "user",
    description="It refers to the operation related to user.",
    path="/api",
    # authorizations=authorizations,
)

user_model = user_namespace.model(
    "UserModel",
    {
        "id": fields.String(),
        "username": fields.String(),
    },
)

user_list_model = user_namespace.model(
    "UserListModel",
    {
        "abc": fields.List(
            {
                "id": fields.String(),
                "username": fields.String(),
            }
        )
    },
)

message_model = user_namespace.model(
    "MessageModel",
    {"message": fields.String()},
)

error_model = user_namespace.model(
    "ErrorModel",
    {"error": fields.String()},
)
