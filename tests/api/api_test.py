import os
from unittest.mock import patch

import pytest

from comd.api import create_app
from tests.integration_test import IntegrationTest


class APITest(IntegrationTest):
    @pytest.fixture
    def test_client(self, session):
        with patch(
            "internal.infrastructure.datastore.datastore.Datastore.build_session"
        ) as datastore_mock:
            datastore_mock.return_value = session

            flask_app = create_app()
            with flask_app.test_client() as flask_client:
                with flask_app.app_context():
                    yield flask_client
