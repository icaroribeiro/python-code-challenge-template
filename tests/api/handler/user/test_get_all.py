from typing import List

from flask_api import status

from internal.infrastructure.storage.datastore.persistent_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persistent_entity.user_factory import (
    UserFactory,
)
from tests.api.handler.user.test_integration_fixtures import TestIntegrationFixtures


class TestGetAll(TestIntegrationFixtures):
    def test_get_all_should_succeed_in_getting_all_users(
        self, test_client, users_url_path, session, fake
    ):
        number_of_users = fake.pyint(min_value=1, max_value=10)
        users = [UserFactory() for _ in range(number_of_users)]
        session.add_all(users)
        session.commit()

        expected_initial_count = number_of_users

        expected_status_code = status.HTTP_200_OK
        expected_json_response = []
        for user in users:
            expected_json_response.append(
                {
                    "id": str(user.id),
                    "username": user.username,
                }
            )

        initial_count = session.query(UserDatastore).count()

        path = users_url_path
        response = test_client.get(path=path)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert self._build_json_data_dict(
            expected_json_response
        ) == self._build_json_data_dict(json_response_data)

    def test_get_all_should_succeed_in_getting_an_empty_list_if_there_are_no_users(
        self, test_client, users_url_path, session, fake
    ):
        number_of_users = 0

        expected_initial_count = number_of_users

        expected_status_code = status.HTTP_200_OK
        expected_json_response = []

        initial_count = session.query(UserDatastore).count()

        path = users_url_path
        response = test_client.get(path=path)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    @staticmethod
    def _build_json_data_dict(json_data_list: List) -> dict:
        json_data_dict = dict()

        for json_data in json_data_list:
            id = json_data["id"]
            json_data_dict[id] = json_data

        return json_data_dict
