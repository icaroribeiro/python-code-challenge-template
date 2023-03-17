from flask_api import status

from internal.infrastructure.storage.datastore.persistent_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persistent_entity.user_factory import (
    UserFactory,
)
from internal.presentation.api.presentable_entity.error import Error
from tests.api.handler.user.test_integration_fixtures import TestIntegrationFixtures


class TestGetById(TestIntegrationFixtures):
    def test_get_by_id_should_succeed_in_getting_a_user_by_its_id(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = user.id
        username = user.username

        expected_initial_count = 1

        expected_status_code = status.HTTP_200_OK
        expected_json_response = {"id": str(id), "username": username}

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(
            users_url_path=users_url_path, id=str(id)
        )
        response = test_client.get(path=path)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_get_by_id_should_fail_if_the_user_id_is_invalid(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = fake.word()

        expected_initial_count = 1

        text = "Bad Request"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_400_BAD_REQUEST

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(users_url_path=users_url_path, id=id)
        response = test_client.get(path=path)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_get_by_id_should_fail_if_the_user_id_is_not_found(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = fake.uuid4()

        expected_initial_count = 1

        text = "Not Found"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_404_NOT_FOUND

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(users_url_path=users_url_path, id=id)
        response = test_client.get(path=path)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data
