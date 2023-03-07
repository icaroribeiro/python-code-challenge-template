from internal.application.service.user.test_service_fixtures import TestServiceFixtures
from internal.core.domain.entity.user_factory import UserFactory


class TestUpdate(TestServiceFixtures):
    def test_update_should_succeed_in_updating_the_user(
        self, service, repository, fake
    ):
        id = fake.uuid4()
        updated_user = UserFactory(id=id)

        repository.update.return_value = updated_user

        returned_updated_user = service.update(id=id, user=updated_user)

        assert updated_user == returned_updated_user

        repository.update.assert_called_once_with(id=id, user=updated_user)

    def test_update_should_not_succeed_in_updating_the_user_if_user_id_is_not_found(
        self, service, repository, fake
    ):
        id = fake.uuid4()
        updated_user = UserFactory(id=id)

        repository.update.return_value = None

        returned_updated_user = service.update(id=id, user=updated_user)

        assert returned_updated_user is None

        repository.update.assert_called_once_with(id=id, user=updated_user)
