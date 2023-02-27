import pytest

from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)
from tests.factory.core.domain.entity.user import UserFactory


class TestCreate(TestRepositoryFixtures):
    def test_create_should_succeed_in_creating_a_user(self, session, repository, fake):
        user = UserFactory()

        returned_user = repository.create(user)

        counter = session.query(UserDatastore).count()

        expected_counter = 0

        assert counter > expected_counter
        assert user.id == str(returned_user.id)
        assert user.username == returned_user.username
