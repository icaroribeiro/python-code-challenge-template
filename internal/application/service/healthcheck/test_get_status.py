import pytest

from internal.application.service.healthcheck.test_service_fixtures import (
    TestServiceFixtures,
)


class TestGetStatus(TestServiceFixtures):
    def test_get_status_should_succeed_in_getting_the_status(self, service):
        is_database_working = service.get_status()

        assert is_database_working is True

    def test_get_status_should_fail_if_an_exception_is_throw_when_checking_if_the_database_is_alive(
        self, service, session
    ):
        session.execute.side_effect = Exception("Failed!")

        with pytest.raises(Exception) as ex:
            is_database_working = service.get_status()
            assert ex.value == "Failed!"
            assert is_database_working is False

        session.execute.assert_called_once_with("SELECT 1")
