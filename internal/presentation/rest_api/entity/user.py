import uuid
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class User:
    username: str
    id: uuid.UUID

    @classmethod
    def from_domain(cls, domain):
        return cls(id=domain.id, username=domain.username)
