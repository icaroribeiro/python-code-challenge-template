from dependency_injector import containers, providers
from sqlalchemy.orm import Session, scoped_session

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.application.service.user.service import Service as UserService

# from internal.infrastructure.storage.datastore.datastore import (
#     Datastore,
#     _cde,
#     session,
#     session20,
#     sfunc,
# )
from internal.infrastructure.storage.datastore.datastore import Datastore
from internal.infrastructure.storage.datastore.repository.user.repository import (
    Repository as UserRepository,
)


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()
    print(config)


class DatastoreContainer(containers.DeclarativeContainer):
    datastore = providers.Factory(
        Datastore, conn_string="postgresql://postgres:postgres@localhost:5432/db"
    )
    session = providers.Singleton(datastore.provided.get_session())
    # session = providers.Singleton(
    #     Datastore(
    #         conn_string="postgresql://postgres:postgres@localhost:5432/db"
    #     ).get_session
    # )


#
#
# class RepositoryContainer(containers.DeclarativeContainer):
#     datastore = providers.DependenciesContainer()
#     user_repository = providers.Factory(
#         UserRepository, session_factory=datastore.provided.session
#     )
#
#
class ServiceContainer(containers.DeclarativeContainer):
    datastore = providers.DependenciesContainer()
    # repository = providers.DependenciesContainer()
    healthcheck_service = providers.Factory(
        HealthCheckService, session=datastore.session
    )
    # user_service = providers.Factory(UserService, repository=repository.user_repository)


class AppContainer(containers.DeclarativeContainer):
    # print(Core.config["conn_string"])
    # conn_string = Core.config.app_config["conn_string"]
    # datastore = Datastore(
    #     conn_string="postgresql://postgres:postgres@localhost:5432/db"
    # )
    datastore = providers.Container(DatastoreContainer)

    # repository = providers.Container(RepositoryContainer, datastore=datastore)
    service = providers.Container(ServiceContainer, datastore=datastore)
    # datastore = providers.Factory(
    #     Datastore, conn_string="postgresql://postgres:postgres@localhost:5432/db"
    # )

    # user_repository = providers.Factory(UserRepository, session=scoped_session(sfunc))
    # healthcheck_service = providers.Factory(HealthCheckService, session=session)
    # user_service = providers.Factory(UserService, repository=user_repository)


# Funciona
# class AppContainer(containers.DeclarativeContainer):
#     datastore = Datastore(
#         conn_string="postgresql://postgres:postgres@localhost:5432/db"
#     )
#     session = providers.Singleton(datastore.get_session)
#     healthcheck_service = providers.Factory(HealthCheckService, session=session)
