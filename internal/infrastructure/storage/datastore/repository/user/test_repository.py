import uuid

import pytest

from internal.core.domain.entity.user import User
from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.repository import (
    Repository,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestRepository(TestRepositoryFixtures):
    @pytest.fixture
    def repository(self, session):
        return Repository(session=session)

    class TestCreate:
        def test_1(self, session, repository):
            # user = UserFactory(username="a")
            user = User(id=uuid.uuid4(), username="a")

            returned_user = repository.create(user)

            count = session.query(UserDatastore).count()

            assert count > 0
            assert user == returned_user
