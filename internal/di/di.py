from dependency_injector import containers, providers

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.application.service.user.service import Service as UserService
from internal.infrastructure.storage.datastore.datastore import Datastore
from internal.infrastructure.storage.datastore.repository.user.repository import (
    Repository as UserRepository,
)


class Core(containers.DeclarativeContainer):
    config = providers.Configuration("app_config")


class DatastoreContainer(containers.DeclarativeContainer):
    datastore = providers.Singleton(
        Datastore, conn_string="postgresql://postgres:postgres@localhost:5432/db"
    )


class RepositoryContainer(containers.DeclarativeContainer):
    datastore = providers.DependenciesContainer()
    user_repository = providers.Factory(
        UserRepository, session_factory=datastore.provided.session
    )


class ServiceContainer(containers.DeclarativeContainer):
    datastore = providers.DependenciesContainer()
    repository = providers.DependenciesContainer()
    healthcheck_service = providers.Factory(
        HealthCheckService, datastore_factory=datastore.provided
    )
    user_service = providers.Factory(UserService, repository=repository.user_repository)


class AppContainer(containers.DeclarativeContainer):
    # datastore = providers.Container(DatastoreContainer)
    # repository = providers.Container(RepositoryContainer, datastore=datastore)
    # service = providers.Container(
    #     ServiceContainer, datastore=datastore, repository=repository
    # )
    datastore = providers.Singleton(
        Datastore, conn_string="postgresql://postgres:postgres@localhost:5432/db"
    )
    user_repository = providers.Factory(
        UserRepository, datastore_factory=datastore.provider
    )
    healthcheck_service = providers.Factory(
        HealthCheckService, datastore_factory=datastore.provided
    )
    user_service = providers.Factory(UserService, repository=user_repository)
