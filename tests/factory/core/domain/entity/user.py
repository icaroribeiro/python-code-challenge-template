import uuid
from dataclasses import dataclass, field

from faker import Faker

fake = Faker()


@dataclass
class UserFactory:
    id: uuid = field(default_factory=fake.uuid4)
    username: str = field(default_factory=fake.name)
