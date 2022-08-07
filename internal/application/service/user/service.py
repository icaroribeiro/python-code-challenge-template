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
