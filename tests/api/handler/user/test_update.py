from flask_api import status

from internal.infrastructure.storage.datastore.persistent_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persistent_entity.user_factory import (
    UserFactory,
)
from internal.presentation.api.presentable_entity.error import Error
from tests.api.handler.user.test_integration_fixtures import TestIntegrationFixtures


class TestUpdate(TestIntegrationFixtures):
    def test_update_should_succeed_in_updating_a_user(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = user.id
        username = fake.name()

        expected_initial_count = 1

        expected_status_code = status.HTTP_200_OK
        expected_json_response = {"id": str(id), "username": username}

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(
            users_url_path=users_url_path, id=str(id)
        )
        json_data = {"username": username}
        response = test_client.put(path=path, json=json_data)
        json_response_data = response.get_json()

        user_datastore = (
            session.query(UserDatastore).filter(UserDatastore.id == id).first()
        )

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data
        assert id == user_datastore.id
        assert username == user_datastore.username

    def test_create_should_fail_if_the_json_body_is_an_empty_json(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = user.id

        expected_initial_count = 1

        text = "Bad Request"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_400_BAD_REQUEST

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(
            users_url_path=users_url_path, id=str(id)
        )
        json_data = {}
        response = test_client.put(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_update_should_fail_if_the_json_body_does_not_contain_expected_key_value_pairs(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        username = fake.name()

        expected_initial_count = 1

        text = "Bad Request"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_400_BAD_REQUEST

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(
            users_url_path=users_url_path, id=str(user.id)
        )
        json_data = {"name": username}
        response = test_client.put(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_update_should_fail_if_the_user_id_is_invalid(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = fake.word()
        username = fake.name()

        expected_initial_count = 1

        text = "Bad Request"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_400_BAD_REQUEST

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(users_url_path=users_url_path, id=id)
        json_data = {"username": username}
        response = test_client.put(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data

    def test_update_should_fail_if_the_user_id_is_not_found(
        self, test_client, users_url_path, session, fake
    ):
        user = UserFactory()
        session.add(user)
        session.commit()

        id = fake.uuid4()
        username = fake.name()

        expected_initial_count = 1

        text = "Not Found"
        expected_json_response = Error(text=text).to_json()
        expected_status_code = status.HTTP_404_NOT_FOUND

        initial_count = session.query(UserDatastore).count()

        path = self._build_users_with_id_url_path(users_url_path=users_url_path, id=id)
        json_data = {"username": username}
        response = test_client.put(path=path, json=json_data)
        json_response_data = response.get_json()

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data
