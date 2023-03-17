from flask_api import status

from internal.infrastructure.storage.datastore.persistent_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persistent_entity.user_factory import (
    UserFactory,
)
from internal.presentation.api.presentable_entity.error import Error
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
        json_data = {"username": username}
        response = test_client.post(path=path, json=json_data)
        json_response_data = response.get_json()

        final_count = session.query(UserDatastore).count()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_final_count == final_count
        assert (
            expected_partial_json_response["username"] == json_response_data["username"]
        )

    def test_create_should_fail_if_the_json_body_is_an_empty_json(
        self, test_client, user_url_path, session, fake
    ):
        expected_initial_count = 0

        text = "Bad Request"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_400_BAD_REQUEST

        initial_count = session.query(UserDatastore).count()

        path = user_url_path
        json_data = {}
        response = test_client.post(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_create_should_fail_if_the_json_body_does_not_contain_expected_key_value_pairs(
        self, test_client, user_url_path, session, fake
    ):
        name = fake.name()

        expected_initial_count = 0

        text = "Bad Request"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_400_BAD_REQUEST

        initial_count = session.query(UserDatastore).count()

        path = user_url_path
        json_data = {"name": name}
        response = test_client.post(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_create_should_fail_if_the_json_body_contains_a_key_with_duplicated_key_value(
        self, test_client, user_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        expected_initial_count = 1

        text = "Conflict"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_409_CONFLICT

        initial_count = session.query(UserDatastore).count()

        path = user_url_path
        json_data = {"username": user.username}
        response = test_client.post(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data
