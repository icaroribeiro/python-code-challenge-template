from dependency_injector import containers, providers

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.application.service.user.service import Service as UserService
from internal.infrastructure.storage.datastore.repository.user.repository import (
    Repository as UserRepository,
)


class DI(containers.DeclarativeContainer):
    db = providers.DependenciesContainer()
    healthcheck_service = providers.Singleton(HealthCheckService, db=db.client)
    user_repository = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, repository=user_repository)
