from flask import Flask

from internal.di.di import AppContainer, Core
from internal.infrastructure.env.env import Env
from internal.presentation.api.handler import blueprint as documented_endpoint
from internal.presentation.api.handler.healthcheck import handler as healthcheck_handler
from internal.presentation.api.handler.user import handler as user_handler

env = Env()

http_port = env.get_env_with_default_value(key="HTTP_PORT", default_value="5000")

driver = env.get_env_with_default_value(key="DB_DRIVER", default_value="postgresql")
user = env.get_env_with_default_value(key="DB_USER", default_value="postgres")
password = env.get_env_with_default_value(key="DB_PASSWORD", default_value="postgres")
host = env.get_env_with_default_value(key="DB_HOST", default_value="localhost")
port = env.get_env_with_default_value(key="DB_PORT", default_value="5433")
name = env.get_env_with_default_value(key="DB_NAME", default_value="db_container")


def create_app():
    _setup_config()

    app_container = AppContainer()
    app_container.wire(modules=[healthcheck_handler])
    app_container.wire(modules=[user_handler])

    app = Flask(__name__)
    app.config["RESTX_MASK_SWAGGER"] = False
    app.register_blueprint(documented_endpoint)

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
