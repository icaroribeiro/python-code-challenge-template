from flask import Flask

from internal.di.di import AppContainer, Core
from internal.infrastructure.env.env import Env
from internal.transport.presentation.handler.healthcheck import (
    handler as healthcheck_handler,
)

env = Env()

driver = env.get_env_with_default_value(key="DB_DRIVER", default_value="postgresql")
user = env.get_env_with_default_value(key="DB_USER", default_value="postgres")
password = env.get_env_with_default_value(key="DB_PASSWORD", default_value="postgres")
host = env.get_env_with_default_value(key="DB_HOST", default_value="localhost")
port = env.get_env_with_default_value(key="DB_PORT", default_value="5432")
name = env.get_env_with_default_value(key="DB_NAME", default_value="testdb")


def create_app():
    _setup_config()
    app_container = AppContainer()
    app_container.wire(modules=[healthcheck_handler])
    app = Flask(__name__)
    app.register_blueprint(healthcheck_handler.blueprint)
    return app


def _setup_config():
    Core.config.override({"datastore_conn_string": _build_datastore_conn_string()})


def _build_datastore_conn_string():
    return "{driver}://{user}:{password}@{host}:{port}/{name}".format(
        driver=driver,
        user=user,
        password=password,
        host=host,
        port=port,
        name=name,
    )
