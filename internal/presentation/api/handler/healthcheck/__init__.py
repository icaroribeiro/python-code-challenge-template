from flask_restx import Namespace, fields, reqparse

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
