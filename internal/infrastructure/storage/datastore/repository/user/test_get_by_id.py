import uuid

from internal.infrastructure.storage.datastore.persisted_entity.user_factory import (
    UserFactory,
)
from internal.infrastructure.storage.datastore.repository.user.test_repository_fixtures import (
    TestRepositoryFixtures,
)


class TestGetById(TestRepositoryFixtures):
    def test_get_by_id_should_succeed_in_getting_a_user_by_its_id(
        self, session, repository, fake
    ):
        persisted_user = UserFactory()
        session.add(persisted_user)
        session.flush()

        id = str(persisted_user.id)

        returned_user = repository.get_by_id(id=id)

        assert uuid.UUID(persisted_user.id) == returned_user.id
        assert persisted_user.username == returned_user.username

    def test_get_by_id_should_return_none_if_id_is_not_found(
        self, session, repository, fake
    ):
        persisted_user = UserFactory()
        session.add(persisted_user)
        session.flush()

        id = fake.uuid4()

        returned_user = repository.get_by_id(id=id)

        assert returned_user is None
