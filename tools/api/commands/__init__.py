from comd.api.config import config_by_name

from flask import Flask

from internal.di.di import AppContainer, Core
from internal.transport.presentation.handler.healthcheck import (
    handler as healthcheck_handler,
)

# db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(healthcheck_handler.blueprint)
    app_container = AppContainer()
    Core.config.override(
        {"conn_string": "postgres://postgres:postgres@localhost:5432/db"}
    )
    app_container.wire(modules=[healthcheck_handler])

    return app
