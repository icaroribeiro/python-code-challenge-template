from internal.core.domain.entity.user_factory import UserFactory as DomainUserFactory
from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persisted_entity.user_factory import (
    UserFactory,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestGetAll(TestRepositoryFixtures):
    def test_get_all_should_succeed_in_getting_all_users(
        self, session, repository, fake
    ):
        persisted_users = [
            UserFactory() for _ in range(fake.pyint(min_value=1, max_value=10))
        ]
        session.add_all(persisted_users)
        session.flush()

        returned_users = repository.get_all()

        assert len(persisted_users) == len(returned_users)
        for persisted_user in persisted_users:
            for returned_user in returned_users:
                if persisted_user.id == str(returned_user.id):
                    assert persisted_user.username == returned_user.username

    def test_get_all_should_return_an_empty_list_if_there_is_no_user(self, repository):
        returned_users = repository.get_all()

        assert [] == returned_users
