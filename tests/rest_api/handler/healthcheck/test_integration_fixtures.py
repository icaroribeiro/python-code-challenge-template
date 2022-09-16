import pytest

from tests.rest_api.rest_api_test import RestAPITest


class TestIntegrationFixtures(RestAPITest):
    @pytest.fixture
    def url_path(self):
        return '/status'
