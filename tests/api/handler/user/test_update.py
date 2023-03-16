from flask_api import status

from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persisted_entity.user_factory import (
    UserFactory,
)
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
        response = test_client.put(path=path, json={"username": username})
        json_response_data = response.get_json()

        user_datastore = (
            session.query(UserDatastore).filter(UserDatastore.id == id).first()
        )

        assert expected_initial_count == initial_count
        assert expected_status_code == response.status_code
        assert expected_json_response == json_response_data
        assert id == user_datastore.id
        assert username == user_datastore.username
