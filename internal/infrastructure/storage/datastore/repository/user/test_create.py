from internal.core.domain.entity.user_factory import UserFactory as DomainUserFactory
from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestCreate(TestRepositoryFixtures):
    def test_create_should_succeed_in_creating_a_user(self, session, repository, fake):
        domain_user = DomainUserFactory()

        returned_user = repository.create(user=domain_user)

        persisted_user = (
            session.query(UserDatastore)
            .filter(UserDatastore.id == domain_user.id)
            .first()
        )

        assert persisted_user.id == returned_user.id
        assert persisted_user.username == returned_user.username
