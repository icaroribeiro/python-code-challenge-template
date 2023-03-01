import uuid
from unittest.mock import patch

from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore
from internal.infrastructure.storage.datastore.repository.user.repository import (
    Repository,
)
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

        returned_updated_user = repository.update(id=str(id), user=updated_user)

        updated_user_datastore = (
            session.query(UserDatastore).filter(UserDatastore.id == id).first()
        )

        expected_updated_user = updated_user_datastore.to_domain()

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
        self, session, repository, fake
    ):
        user = UserFactory()
        user_datastore = UserDatastore.from_domain(domain=user)
        session.add(user_datastore)
        session.commit()

        id = user_datastore.id
        updated_user = UserFactory(id=id)

        session.query().filter().update.side_effect = 0

        returned_updated_user = repository.update(id=id, user=updated_user)

        assert returned_updated_user is None
