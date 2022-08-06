import uuid

from internal.core.domain.entity.user import User
from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestCreate(TestRepositoryFixtures):
    def test_create_should_succeed_in_creating_a_user(self, session, repository, fake):
        user = User(id=uuid.uuid4(), username=fake.name())

        returned_user = repository.create(user)

        count = session.query(UserDatastore).count()

        assert count > 0
        assert user == returned_user
