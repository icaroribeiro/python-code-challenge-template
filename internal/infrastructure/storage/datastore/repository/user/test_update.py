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


class TestUpdate(TestRepositoryFixtures):
    def test_update_should_succeed_in_updating_a_user(self, session, repository, fake):
        persistent_user = UserFactory()
        session.add(persistent_user)
        session.commit()

        id = persistent_user.id
        updated_domain_user = DomainUserFactory(id=id)

        returned_updated_user = repository.update(id=str(id), user=updated_domain_user)

        assert updated_domain_user.id == returned_updated_user.id
        assert updated_domain_user.username == returned_updated_user.username

    def test_update_should_fail_in_updating_a_user_if_id_is_not_found(
        self, session, repository, fake
    ):
        persistent_user = UserFactory()
        session.add(persistent_user)
        session.commit()

        id = fake.uuid4()
        updated_domain_user = DomainUserFactory(id=id)

        returned_updated_user = repository.update(id=id, user=updated_domain_user)

        assert returned_updated_user is None

    def test_update_should_fail_in_updating_a_user_if_an_error_occurs_when_updating_a_user(
        self, session_mock, repository_with_session_mock, fake
    ):
        domain_user = DomainUserFactory()
        user_datastore = UserDatastore.from_domain(domain=domain_user)

        id = str(user_datastore.id)
        updated_domain_user = DomainUserFactory(id=user_datastore.id)

        session_mock.query.return_value.filter.return_value.first.return_value = (
            user_datastore
        )

        session_mock.query.return_value.filter.return_value.update.return_value = 0

        returned_updated_user = repository_with_session_mock.update(
            id=id, user=updated_domain_user
        )

        assert returned_updated_user is None
