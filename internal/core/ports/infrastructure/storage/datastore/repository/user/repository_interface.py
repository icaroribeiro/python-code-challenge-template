from typing import List

from internal.core.domain.entity.user import User


class IRepository:
    def create(self, user: User) -> User:
        raise NotImplemented

    def get_by_id(self, id: str) -> User:
        raise NotImplemented

    def get_all(self) -> List[User]:
        raise NotImplemented

    def update(self, id: str, user: User) -> User:
        raise NotImplemented

    def delete(self, id: str) -> User:
        raise NotImplemented
