from flask_restplus import Namespace, fields


class Auth:
    api = Namespace(
        "auth", description="It refers to the operations related to authentication."
    )
    credentials = api.model(
        "auth",
        {
            "username": fields.String(required=True),
            "password": fields.String(required=True),
        },
    )
