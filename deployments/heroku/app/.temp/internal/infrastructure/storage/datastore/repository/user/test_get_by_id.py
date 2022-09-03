import uuid

from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestGetById(TestRepositoryFixtures):
    def test_get_by_id_should_succeed_in_getting_a_user_by_its_id(
        self, session, repository, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        returned_user = repository.get_by_id(id=str(user.id))

        assert user.id == str(returned_user.id)
        assert user.username == returned_user.username

    def test_get_by_id_should_return_none_if_id_is_not_found(
        self, session, repository, fake
    ):
        id = fake.uuid4()
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        returned_user = repository.get_by_id(id=str(id))

        assert returned_user is None

    def test_get_by_id_should_return_none_if_there_are_no_records(
        self, session, repository, fake
    ):
        id = fake.uuid4()

        returned_user = repository.get_by_id(id=str(id))

        assert returned_user is None