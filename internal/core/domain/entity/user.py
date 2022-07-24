import uuid
from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass(frozen=True)
class User(BaseModel):
    id: uuid.UUID = Field(init=True, default_factory=uuid.uuid4)
