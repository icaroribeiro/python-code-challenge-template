import os

from internal.infrastructure.env.test_env_fixtures import TestEnvFixtures


class TestGetEnvWithDefaultValue(TestEnvFixtures):
    def test_should_succeed_in_getting_env_value(self, env, faker):
        key = "ENV_VAR"
        value = "value"
        default_value = ""

        os.environ.setdefault(key=key, value=value)

        returned_value = env.get_env_with_default_value(
            key=key, default_value=default_value
        )

        assert returned_value == value
