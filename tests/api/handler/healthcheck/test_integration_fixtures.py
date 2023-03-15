import pytest

from tests.api.api_test import APITest


class TestIntegrationFixtures(APITest):
    @pytest.fixture
    def path_prefix(self):
        return "/api"

    @pytest.fixture
    def status_url_path(self, path_prefix):
        return f"{path_prefix}/status"
