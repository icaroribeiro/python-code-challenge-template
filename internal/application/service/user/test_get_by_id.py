from internal.application.service.user.test_service_fixtures import TestServiceFixtures
from tests.factory.core.domain.entity.user import UserFactory


class TestGetById(TestServiceFixtures):
    def test_get_by_id_should_succeed_in_getting_a_user_by_its_id(self, service, repository, fake):
        user = UserFactory()

        repository.get_by_id.return_value = user

        return_user = service.get_by_id(id=user.id)

        assert user == return_user

        repository.get_by_id.assert_called_once_with(id=user.id)

    def test_get_by_id_should_return_none_if_there_is_no_user(self, service, repository, fake):
        id = fake.uuid4()

        repository.get_by_id.return_value = None

        return_user = service.get_by_id(id=id)

        assert return_user is None

        repository.get_by_id.assert_called_once_with(id=id)
