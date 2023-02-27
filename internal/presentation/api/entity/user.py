import uuid
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class User:
    id: uuid.UUID
    username: str

    @classmethod
    def from_domain(cls, domain):
        return cls(id=domain.id, username=domain.username)
