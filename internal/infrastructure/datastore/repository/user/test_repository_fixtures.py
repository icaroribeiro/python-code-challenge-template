import pytest
from faker import Faker

from internal.infrastructure.datastore.repository.user.repository import Repository
from tests.integration_test import IntegrationTest


class TestRepositoryFixtures(IntegrationTest):
    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def repository(self, session):
        return Repository(session=session)

    @pytest.fixture
    def repository_with_session_mock(self, session_mock):
        return Repository(session=session_mock)
