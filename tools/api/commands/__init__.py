from comd.api.config import config_by_name

import flask_injector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from internal.di.di import DI
from internal.transport.presentation.handler.healthcheck import (
    handler as healthcheck_handler,
)

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(healthcheck_handler.blueprint)

    di = DI()
    di.wire(modules=[healthcheck_handler])

    db.init_app(app)

    def configure_dependencies(binder):
        binder.bind(SQLAlchemy, to=db, scope=flask_injector.singleton)

    flask_injector.FlaskInjector(app=app, modules=[configure_dependencies])

    return app
