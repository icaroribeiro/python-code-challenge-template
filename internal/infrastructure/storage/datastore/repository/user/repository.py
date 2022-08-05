from internal.core.domain.entity.user import User
from internal.core.ports.infrastructure.storage.datastore.repository.user.repository_interface import (
    IRepository,
)
from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore


class Repository(IRepository):
    def __init__(self, session):
        self._session = session

    def create(self, user: User) -> User:
        user_datastore: UserDatastore

        user_datastore = UserDatastore.from_domain(domain=user)

        self._session.add(user_datastore)

        self._session.commit()

        return user_datastore.to_domain()
