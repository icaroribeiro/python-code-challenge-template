from internal.core.domain.entity.user_factory import UserFactory
from internal.infrastructure.storage.datastore.persisted_entity.user import (
    User as UserDatastore,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestDelete(TestRepositoryFixtures):
    def test_delete_should_succeed_in_deleting_the_user(
        self, session, repository, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = user.id
        expected_deleted_user = user_datastore.to_domain()

        returned_deleted_user = repository.delete(id=id)

        assert expected_deleted_user.id == returned_deleted_user.id
        assert expected_deleted_user.username == returned_deleted_user.username

    def test_delete_should_not_succeed_in_deleting_the_user_if_user_id_is_not_found(
        self, session, repository, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = fake.uuid4()

        returned_deleted_user = repository.delete(id=id)

        assert returned_deleted_user is None

    def test_delete_should_fail_in_deleting_a_user_if_an_error_occurs_when_deleting_a_user(
        self, session_mock, repository_with_session_mock, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)

        id = fake.uuid4()

        session_mock.query.return_value.filter.return_value.first.return_value = (
            user_datastore
        )

        session_mock.query.return_value.filter.return_value.delete.return_value = None

        returned_deleted_user = repository_with_session_mock.delete(id=id)

        assert returned_deleted_user is None
