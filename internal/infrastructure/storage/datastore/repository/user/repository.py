class User(Base):
    __tablename__ = "user"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.UUID)
    type = Column("type", Enum(AType), nullable=False)
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
        domain = UserDomain(
            id=self.id,
        )
