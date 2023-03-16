from flask_api import status

from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from tests.api.handler.user.test_integration_fixtures import TestIntegrationFixtures


class TestCreate(TestIntegrationFixtures):
    def test_create_should_succeed_in_creating_a_user(
        self, test_client, user_url_path, session, fake
    ):
        username = fake.name()

        expected_initial_count = 0
        expected_final_count = 1

        expected_status_code = status.HTTP_201_CREATED
        expected_partial_json_response = {"username": username}

        initial_count = session.query(UserDatastore).count()

        path = user_url_path
        response = test_client.post(path=path, json={"username": username})
        json_response_data = response.get_json()

        final_count = session.query(UserDatastore).count()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_final_count == final_count
        assert (
            expected_partial_json_response["username"] == json_response_data["username"]
        )
