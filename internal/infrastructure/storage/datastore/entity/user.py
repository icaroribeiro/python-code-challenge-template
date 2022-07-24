import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

from internal.core.domain.entity.user import User as UserDomain

Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
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
        return cls(
            id=domain.id,
        )

    def to_domain(self):
        return UserDomain(
            id=self.id,
        )
