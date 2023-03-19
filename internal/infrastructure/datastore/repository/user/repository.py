import uuid
from typing import List, Optional

from internal.core.domain.entity.user import User
from internal.core.ports.infrastructure.datastore.repository.user.repository_interface import (
    IRepository,
)
from internal.infrastructure.datastore.persistent_entity.user import (
    User as UserDatastore,
)


class Repository(IRepository):
    def __init__(self, session) -> None:
        self.session = session

    def create(self, user: User) -> User:
        user_datastore = UserDatastore.from_domain(domain=user)
        self.session.add(user_datastore)
        self.session.commit()

        return user_datastore.to_domain()

    def get_all(self) -> List[User]:
        user_datastore_list: List[UserDatastore]

        user_datastore_list = self.session.query(UserDatastore).all()

        return [user_datastore.to_domain() for user_datastore in user_datastore_list]

    def get_by_id(self, id: str) -> Optional[User]:
        user_datastore = (
            self.session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .first()
        )

        return user_datastore.to_domain() if user_datastore else None

    def update(self, id: str, user: User) -> Optional[User]:
        user_datastore = (
            self.session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .first()
        )

        if not user_datastore:
            return None

        counter = (
            self.session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .update(
                {UserDatastore.username: user.username}, synchronize_session="fetch"
            )
        )

        if counter == 0:
            return None

        self.session.commit()
        return user

    def delete(self, id: str) -> Optional[User]:
        user_datastore = (
            self.session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .first()
        )

        if not user_datastore:
            return None

        deleted_user_counter = (
            self.session.query(UserDatastore)
            .filter(UserDatastore.id == uuid.UUID(id))
            .delete()
        )

        self.session.commit()
        return user_datastore.to_domain() if deleted_user_counter else None
