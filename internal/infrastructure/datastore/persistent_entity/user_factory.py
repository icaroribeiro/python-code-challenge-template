from datetime import datetime, timedelta

import factory
from factory import BUILD_STRATEGY, LazyAttribute, LazyFunction
from faker import Faker

from internal.infrastructure.datastore.persistent_entity.user import User

fake = Faker()


class UserFactory(factory.Factory):
    class Meta:
        strategy = BUILD_STRATEGY
        model = User

    id = LazyFunction(fake.uuid4)
    username = LazyFunction(fake.name)
    created_at = LazyFunction(datetime.utcnow)
    # created_at = LazyAttribute(lambda _: datetime.utcnow() - timedelta(days=1))
    updated_at = LazyFunction(datetime.utcnow)
