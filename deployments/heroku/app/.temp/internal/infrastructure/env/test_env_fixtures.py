import pytest
from faker import Faker

from internal.infrastructure.env.env import Env


class TestEnvFixtures:
    @pytest.fixture
    def faker(self):
        return Faker

    @pytest.fixture
    def env(self):
        return Env
