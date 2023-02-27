import pytest

from comd.api import create_app
from tests.integration_test import IntegrationTest


class APITest(IntegrationTest):
    @pytest.fixture
    def test_client(self):
        flask_app = create_app()

        with flask_app.test_client() as flask_client:
            with flask_app.app_context():
                yield flask_client
