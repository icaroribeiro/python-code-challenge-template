from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestUpdate(TestRepositoryFixtures):
    def test_update_should_succeed_in_updating_a_user(self, session, repository, fake):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = user_datastore.id
        updated_user = UserFactory(id=id)
        expected_updated_user = updated_user

        returned_updated_user = repository.update(id=str(id), user=updated_user)

        assert expected_updated_user.id == returned_updated_user.id
        assert expected_updated_user.username == returned_updated_user.username

    def test_update_should_fail_in_updating_a_user_if_id_is_not_found(
        self, session, repository, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = fake.uuid4()
        updated_user = UserFactory(id=id)

        returned_updated_user = repository.update(id=id, user=updated_user)

        assert returned_updated_user is None

    def test_update_should_fail_in_updating_a_user_if_an_error_occurs_when_updating_a_user(
        self, session_mock, repository_with_session_mock, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)

        id = str(user_datastore.id)
        updated_user = UserFactory(id=user_datastore.id)

        session_mock.query.return_value.filter.return_value.first.return_value = (
            user_datastore
        )

        session_mock.query.return_value.filter.return_value.update.return_value = 0

        returned_updated_user = repository_with_session_mock.update(
            id=id, user=updated_user
        )

        assert returned_updated_user is None
