from internal.core.domain.entity.user_factory import UserFactory
from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestCreate(TestRepositoryFixtures):
    def test_create_should_succeed_in_creating_a_user(self, session, repository, fake):
        user = UserFactory()

        returned_user = repository.create(user)

        user_datastore = (
            session.query(UserDatastore).filter(UserDatastore.id == user.id).first()
        )

        new_user = user_datastore.to_domain()
        assert new_user.id == returned_user.id
        assert new_user.username == returned_user.username
