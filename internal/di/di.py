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
    config = providers.Configuration()


class DatastoreContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    datastore = providers.Factory(
        Datastore,
        conn_string=config.datastore_conn_string,
    )

    session = providers.Factory(Datastore.session_factory, datastore=datastore)


class RepositoryContainer(containers.DeclarativeContainer):
    datastore = providers.DependenciesContainer()

    user_repository = providers.Factory(UserRepository, session=datastore.session)


class ServiceContainer(containers.DeclarativeContainer):
    datastore = providers.DependenciesContainer()

    repository = providers.DependenciesContainer()

    healthcheck_service = providers.Factory(
        HealthCheckService, session=datastore.session
    )

    user_service = providers.Factory(UserService, repository=repository.user_repository)


class AppContainer(containers.DeclarativeContainer):
    datastore = providers.Container(DatastoreContainer, config=Core.config)

    repository = providers.Container(RepositoryContainer, datastore=datastore)

    service = providers.Container(
        ServiceContainer, datastore=datastore, repository=repository
    )
