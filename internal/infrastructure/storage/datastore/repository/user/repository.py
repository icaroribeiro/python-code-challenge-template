import uuid
from typing import List

from internal.core.domain.entity.user import User
from internal.core.ports.infrastructure.storage.datastore.repository.user.repository_interface import (
    IRepository,
)
from internal.infrastructure.storage.datastore.entity.user import User as UserDatastore


class Repository(IRepository):
    def __init__(self, session) -> None:
        self._session = session

    def create(self, user: User) -> User:
        user_datastore: UserDatastore

        user_datastore = UserDatastore.from_domain(domain=user)

        self._session.add(user_datastore)

        self._session.commit()

        return user_datastore.to_domain()

    def get_all(self) -> List[User]:
        user_datastore_list: List[UserDatastore]

        user_datastore_list = self._session.query(UserDatastore).all()

        return [user_datastore.to_domain() for user_datastore in user_datastore_list]

    def get_by_id(self, id: str) -> User:
        user_datastore: UserDatastore

        user_datastore = (
            self._session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .first()
        )

        return user_datastore.to_domain()

    def update(self, id: str, user: User) -> User:
        user_datastore: UserDatastore

        user_datastore = (
            self._session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .update({UserDatastore.username: user.username}, synchronize_session=False)
        )

        self._session.commit()

        return user_datastore.to_domain()

    def delete(self, id: str) -> User:
        user_datastore: UserDatastore

        user_datastore = (
            self._session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .delete()
        )

        self._session.commit()

        return user_datastore.to_domain()
