import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from internal.core.domain.entity.user import User as UserDomain
from internal.infrastructure.storage.datastore.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid.UUID,
    )
    username = Column("username", String, unique=True, nullable=False)
    created_at = Column(
        "created_at", DateTime(), nullable=False, default=datetime.utcnow
    )
    updated_at = Column(
        "updated_at",
        DateTime(),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    @classmethod
    def from_domain(cls, domain):
        return cls(id=domain.id, username=domain.username)

    def to_domain(self):
        return UserDomain(id=self.id, username=str(self.username))
