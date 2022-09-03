import pytest
from faker import Faker

from internal.infrastructure.storage.datastore.repository.user.repository import (
    Repository,
)
from tests.api.integration_test import IntegrationTest


class TestRepositoryFixtures(IntegrationTest):
    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def repository(self, session):
        return Repository(session=session)
