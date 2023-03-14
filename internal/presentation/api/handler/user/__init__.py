from flask_restx import Namespace, fields

user_namespace = Namespace(
    "user",
    description="It refers to the operation related to user.",
    path="/api",
    # authorizations=authorizations,
)

error_model = user_namespace.model(
    "ErrorModel",
    {"error": fields.String()},
)

creatable_user_model = user_namespace.model(
    "CreatableUserModel",
    {
        "username": fields.String(),
    },
)

updatable_user_model = user_namespace.model(
    "UpdatableUserModel",
    {
        "username": fields.String(),
    },
)

# mylist_model = user_namespace.model("Mylist", {"a": fields.String()})

user_fields = {
    "id": fields.String(),
    "username": fields.String(),
    # "mylist": fields.List(fields.Nested(mylist_model)),
}

user_model = user_namespace.model(
    "UserModel",
    user_fields,
)

user_collection_model = [user_model]
