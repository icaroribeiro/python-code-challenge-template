from flask_restplus import Namespace, fields


class User:
    api = Namespace("user", description="It refers to the operations related to user.")
    user = api.model(
        "user",
        {
            "id": fields.String(),
            "username": fields.String(),
        },
    )
