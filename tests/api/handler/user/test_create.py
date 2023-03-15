from unittest.mock import patch

import pytest

from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from tests.api.handler.user.test_integration_fixtures import TestIntegrationFixtures


class TestCreate(TestIntegrationFixtures):
    def test_create_user_should_succeed_in_creating_a_user(
        self, test_client, user_url_path, session, fake
    ):
        a = session.query(UserDatastore).count()

        test_response = test_client.post(user_url_path, json={"username": fake.name()})
        #
        #     json_data = test_response.get_json()
        #
        #     # expected_status_code = status.HTTP_201_CREATED
        #
        b = session.query(UserDatastore).count()
        assert a == 0
        assert b == 1
        assert True is True

    # a = session.query(UserDatastore).count()
    #
    # test_response = test_client.post(
    #     user_url_path, json={"username": "icaroribeiro"}
    # )
    #
    # json_data = test_response.get_json()
    #
    # # expected_status_code = status.HTTP_201_CREATED
    #
    # assert True is True
