from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestGetAll(TestRepositoryFixtures):
    def test_get_all_should_succeed_in_getting_all_users(
        self, session, repository, fake
    ):
        users = [UserFactory() for _ in range(fake.pyint(min_value=1, max_value=10))]
        user_datastore_list = [UserDatastore.from_domain(user) for user in users]
        session.add_all(user_datastore_list)
        session.commit()

        returned_users = repository.get_all()

        assert len(user_datastore_list) == len(returned_users)
        assert {
            user_datastore.to_domain() for user_datastore in user_datastore_list
        } == {returned_user for returned_user in returned_users}
