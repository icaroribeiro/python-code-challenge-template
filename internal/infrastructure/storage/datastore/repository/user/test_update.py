from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestUpdate(TestRepositoryFixtures):
    def test_update_user_should_succeed_in_updating_the_user(self, session, repository, fake):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = user_datastore.id
        updated_user = UserFactory(id=id)

        returned_updated_user = repository.update(id=str(id), user=updated_user)

        user_datastore = (
            session.query(UserDatastore)
            .filter(UserDatastore.id == id)
            .first()
        )

        expected_updated_user = user_datastore.to_domain()

        assert expected_updated_user.id == returned_updated_user.id
        assert expected_updated_user.username == returned_updated_user.username

    def test_update_user_should_not_succeed_in_updating_the_user_if_user_id_is_not_found(self, session, repository, fake):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = fake.uuid4()
        updated_user = UserFactory(id=user_datastore.id)

        returned_updated_user = repository.update(id=id, user=updated_user)

        expected_updated_user = None

        assert expected_updated_user == returned_updated_user
