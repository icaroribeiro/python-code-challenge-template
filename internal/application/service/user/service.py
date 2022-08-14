from typing import List

from internal.core.domain.entity.user import User
from internal.core.ports.application.service.user.service_interface import IService
from internal.core.ports.infrastructure.storage.datastore.repository.user.repository_interface import (
    IRepository,
)


class Service(IService):
    _repository: IRepository

    def __init__(self, repository: IRepository) -> None:
        self._repository = repository

    def create(self, user: User) -> User:
        return self._repository.create(user)

    def get_all(self) -> List[User]:
        return self._repository.get_all()

    def get_by_id(self, id: str) -> User:
        return self._repository.get_by_id(id=id)

    def update(self, id: str, user: User) -> User:
        return self._repository.update(id=id, user=user)

    def delete(self, id: str) -> User:
        return self._repository.delete(id=id)
