from comd.api.config import config_by_name

from flask import Flask

from internal.di.di import AppContainer, Core
from internal.infrastructure.env.env import Env
from internal.infrastructure.storage.datastore.datastore import Datastore
from internal.transport.presentation.handler.healthcheck import (
    handler as healthcheck_handler,
)


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config_by_name[config_name])
    app.register_blueprint(healthcheck_handler.blueprint)

    env = Env()

    driver = env.get_env_with_default_value(key="DB_DRIVER", default_value="postgresql")
    user = env.get_env_with_default_value(key="DB_USER", default_value="postgres")
    password = env.get_env_with_default_value(
        key="DB_PASSWORD", default_value="postgres"
    )
    host = env.get_env_with_default_value(key="DB_HOST", default_value="localhost")
    port = env.get_env_with_default_value(key="DB_PORT", default_value="5432")
    name = env.get_env_with_default_value(key="DB_NAME", default_value="testdb")

    conn_string = "{driver}://{user}:{password}@{host}:{port}/{name}".format(
        driver=driver,
        user=user,
        password=password,
        host=host,
        port=port,
        name=name,
    )

    app_container = AppContainer()
    Core.config.override({"conn_string": conn_string})
    # Core.config.conn_string = conn_string
    app_container.wire(modules=[healthcheck_handler])

    return app
