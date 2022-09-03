from internal.application.service.healthcheck.test_service_fixtures import (
    TestServiceFixtures,
)


class TestGetStatus(TestServiceFixtures):
    def test1(self, service):
        is_database_working = service.get_status()

        assert is_database_working is True
