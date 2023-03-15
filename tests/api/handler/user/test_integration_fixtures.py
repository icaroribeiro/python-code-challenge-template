import pytest
from faker import Faker

from tests.api.api_test import APITest


class TestIntegrationFixtures(APITest):
    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def path_prefix(self):
        return "/api"

    @pytest.fixture
    def user_url_path(self, path_prefix):
        return f"{path_prefix}/user"

    @pytest.fixture
    def users_url_path(self, path_prefix):
        return f"{path_prefix}/users"
