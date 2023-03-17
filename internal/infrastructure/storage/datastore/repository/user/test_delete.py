import uuid

from internal.core.domain.entity.user_factory import UserFactory as DomainUserFactory
from internal.infrastructure.storage.datastore.persistent_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.persistent_entity.user_factory import (
    UserFactory,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestDelete(TestRepositoryFixtures):
    def test_delete_should_succeed_in_deleting_a_user(self, session, repository, fake):
        persistent_user = UserFactory()
        session.add(persistent_user)
        session.flush()

        id = persistent_user.id
        username = persistent_user.username

        returned_deleted_user = repository.delete(id=id)

        count = session.query(UserDatastore).filter(UserDatastore.id == id).count()

        assert count == 0
        assert id == str(returned_deleted_user.id)
        assert username == returned_deleted_user.username

    def test_delete_should_not_succeed_in_deleting_the_user_if_user_id_is_not_found(
        self, session, repository, fake
    ):
        user = UserFactory()
        session.add(user)
        session.flush()

        id = fake.uuid4()

        returned_deleted_user = repository.delete(id=id)

        assert returned_deleted_user is None

    def test_delete_should_fail_in_deleting_a_user_if_an_error_occurs_when_deleting_a_user(
        self, session_mock, repository_with_session_mock, fake
    ):
        domain_user = DomainUserFactory()
        user_datastore = UserDatastore.from_domain(domain=domain_user)

        id = fake.uuid4()

        session_mock.query.return_value.filter.return_value.first.return_value = (
            user_datastore
        )

        session_mock.query.return_value.filter.return_value.delete.return_value = None

        returned_deleted_user = repository_with_session_mock.delete(id=id)

        assert returned_deleted_user is None
