from flask_api import status

from tests.rest_api.handler.healthcheck.test_integration_fixtures import TestIntegrationFixtures


class TestGetStatus(TestIntegrationFixtures):
    def test_get_status_should_succeed_in_getting_the_status(self, test_client, url_path):
        test_response = test_client.get(url_path)

        expected_json_response = {'message': 'everything is up and running'}

        assert test_response.status_code == status.HTTP_200_OK
        assert test_response.json == expected_json_response
