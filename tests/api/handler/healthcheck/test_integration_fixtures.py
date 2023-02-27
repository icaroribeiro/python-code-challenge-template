import pytest

from tests.api.api_test import APITest


class TestIntegrationFixtures(APITest):
    @pytest.fixture
    def url_path(self):
        return "/status"
