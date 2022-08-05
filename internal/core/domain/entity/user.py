import uuid
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True, eq=True)
class User:
    username: str
    id: uuid.UUID = field(init=True, default_factory=uuid.uuid4)
    # id: str = field(default_factory=lambda: str(uuid4()))
