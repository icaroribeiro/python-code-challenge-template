import uuid

from internal.application.service.user.test_service_fixtures import TestServiceFixtures
from internal.core.domain.entity.user import User


class TestCreate(TestServiceFixtures):
    def test_create_should_succeed_in_creating_a_user(self, service, repository, fake):
        user = User(id=uuid.uuid4(), username=fake.name())

        repository.create.return_value = user

        returned_user = service.create(user=user)

        assert user == returned_user
