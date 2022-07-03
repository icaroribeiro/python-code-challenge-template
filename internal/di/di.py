from dependency_injector import containers, providers

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)


class DI(containers.DeclarativeContainer):
    db = providers.DependenciesContainer()
    healthcheck_service = providers.Singleton(HealthCheckService, db=db.client)
