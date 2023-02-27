from unittest.mock import MagicMock

import pytest

from internal.application.service.healthcheck.service import Service


class TestServiceFixtures:
    @pytest.fixture
    def session(self):
        return MagicMock()

    @pytest.fixture
    def service(self, session):
        return Service(session=session)
