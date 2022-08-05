import factory
from factory import LazyFunction
from faker import Faker

from internal.core.domain.entity.user import User

fake = Faker()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = LazyFunction(fake.uuid)
    username = LazyFunction(fake.username)
