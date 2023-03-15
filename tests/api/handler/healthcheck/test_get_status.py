from flask_api import status

from internal.presentation.api.entity.message import Message
from tests.api.handler.healthcheck.test_integration_fixtures import (
    TestIntegrationFixtures,
)


class TestGetStatus(TestIntegrationFixtures):
    def test_get_status_should_succeed_in_getting_the_status(
        self, test_client, status_url_path
    ):
        expected_status_code = status.HTTP_200_OK

        text = "everything is up and running"
        expected_json_response = Message(text=text).to_json()

        test_response = test_client.get(status_url_path)

        assert expected_status_code == test_response.status_code
        assert expected_json_response == test_response.json
