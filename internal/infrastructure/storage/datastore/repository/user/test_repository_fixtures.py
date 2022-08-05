import pytest
from faker import Faker

from tests.api.integration_test import IntegrationTest


class TestRepositoryFixtures(IntegrationTest):
    @pytest.fixture
    def faker(self):
        return Faker()
