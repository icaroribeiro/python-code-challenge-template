from internal.core.domain.entity.user import User
from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestCreate(TestRepositoryFixtures):
    def test_create_should_succeed_in_creating_a_user(self, session, repository, fake):
        user = UserFactory()

        returned_user = repository.create(user)

        count = session.query(UserDatastore).count()

        assert count > 0
        self._assert_users(user=user, returned_user=returned_user)

    @staticmethod
    def _assert_users(user: UserFactory, returned_user: User):
        assert user.id == returned_user.id
        assert user.username == returned_user.username
