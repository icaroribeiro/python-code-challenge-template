from dependency_injector import containers, providers
from sqlalchemy.orm import Session, scoped_session

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.application.service.healthcheck.service import TestService
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
    config = providers.Configuration("config")
    print("Test 0123:", config)


class DatastoreContainer(containers.DeclarativeContainer):
    # print("test:", Core.config.get("conn_string"))

    # core = providers.DependenciesContainer()
    # config = providers.Configuration()
    # print("config --->:", config.abc)
    config = providers.Configuration()
    print("config.conn_string in Datastore: ", config.conn_string)
    datastore = providers.Factory(
        Datastore,
        conn_string=config.conn_string,
    )
    session = providers.Factory(Datastore.session_factory, datastore=datastore)
    # session = providers.Callable(
    #     Datastore(
    #         conn_string=config.conn_string,
    #     ).provided.get_session
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
    print("Service")

    config = providers.Configuration()
    print("config.conn_string: ", config.conn_string)
    # repository = providers.DependenciesContainer()
    datastore = providers.DependenciesContainer()
    test_service = providers.Factory(TestService, test=config.conn_string)
    healthcheck_service = providers.Factory(
        HealthCheckService, session=datastore.session
    )

    # user_service = providers.Factory(UserService, repository=repository.user_repository)


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    # core = providers.Container(Core, config=config.core)

    print("AppContainer *****")
    # core = providers.Container(Core)
    # print(core.config)
    # print(Core.config["conn_string"])
    # conn_string = Core.config.app_config["conn_string"]
    # datastore = Datastore(
    #     conn_string="postgresql://postgres:postgres@localhost:5432/db"
    # )

    datastore = providers.Container(DatastoreContainer, config=config)

    # repository = providers.Container(RepositoryContainer, datastore=datastore)
    service = providers.Container(ServiceContainer, datastore=datastore, config=config)
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
