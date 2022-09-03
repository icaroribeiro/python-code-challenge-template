import uuid

import pytest

from internal.application.service.user.test_service_fixtures import TestServiceFixtures
from internal.core.domain.entity.user import User


class TestCreate(TestServiceFixtures):
    def test_create_should_succeed_in_creating_a_user(self, service, repository, fake):
        user = User(id=uuid.uuid4(), username=fake.name())

        repository.create.return_value = user

        returned_user = service.create(user=user)

        assert user == returned_user

    def test_create_should_fail_if_an_expection_is_risen_when_creating_a_user(
        self, service, repository, fake
    ):
        user = User(id=uuid.uuid4(), username=fake.name())

        repository.create.side_effect = Exception("Failed!")

        with pytest.raises(Exception) as ex:
            service.create(user=user)
            assert ex.value == "Failed!"
