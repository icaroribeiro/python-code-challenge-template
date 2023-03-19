from unittest.mock import MagicMock

import pytest
from faker import Faker

from internal.application.service.user.service import Service
from internal.core.ports.infrastructure.datastore.repository.user.repository_interface import (
    IRepository,
)


class TestServiceFixtures:
    @pytest.fixture
    def fake(self):
        return Faker()

    @pytest.fixture
    def repository(self):
        return MagicMock(spec=IRepository)

    @pytest.fixture
    def service(self, repository: IRepository):
        return Service(repository=repository)
