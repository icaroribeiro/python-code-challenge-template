from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestDelete(TestRepositoryFixtures):
    def test_delete_should_succeed_in_deleting_the_user(self, session, repository, fake):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = user.id

        returned_deleted_user_counter = repository.delete(id=id)

        expected_returned_deleted_user_counter = 1

        assert expected_returned_deleted_user_counter == returned_deleted_user_counter

    def test_delete_should_not_succeed_in_deleting_the_user_if_user_id_is_not_found(self, session, repository, fake):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = fake.uuid4()

        returned_deleted_user_counter = repository.delete(id=id)

        expected_returned_deleted_user_counter = 0

        assert expected_returned_deleted_user_counter == returned_deleted_user_counter
