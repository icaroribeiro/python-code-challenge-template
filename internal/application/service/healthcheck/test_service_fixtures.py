import pytest

from internal.application.service.healthcheck.service import Service
from tests.integration_test import IntegrationTest


class TestServiceFixtures(IntegrationTest):
    @pytest.fixture
    def service(self, session):
        return Service(session=session)
