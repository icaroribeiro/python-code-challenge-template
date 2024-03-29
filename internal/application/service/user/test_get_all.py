import pytest

from internal.application.service.user.test_service_fixtures import \
    TestServiceFixtures
from internal.core.domain.entity.user_factory import UserFactory


class TestGetAll(TestServiceFixtures):
    def test_get_all_should_succeed_in_getting_all_users(
        self, service, repository, fake
    ):
        users = [UserFactory() for _ in range(fake.pyint(min_value=1, max_value=10))]

        repository.get_all.return_value = users

        returned_users = service.get_all()

        assert users == returned_users

        repository.get_all.assert_called_once()

    def test_get_all_should_return_an_empty_list_if_there_is_no_user(
        self, service, repository, fake
    ):
        repository.get_all.return_value = []

        returned_users = service.get_all()

        assert [] == returned_users

        repository.get_all.assert_called_once()

    def test_get_all_should_fail_if_an_exception_is_throw_when_getting_all_users(
        self, service, repository, fake
    ):
        repository.get_all.side_effect = Exception("Unexpected!")

        with pytest.raises(Exception) as ex:
            service.get_all()
            assert ex.value == "Unexpected!"

        repository.get_all.assert_called_once()
