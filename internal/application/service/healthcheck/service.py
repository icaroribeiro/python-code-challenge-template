from dependency_injector.wiring import inject
from flask_sqlalchemy import SQLAlchemy

from internal.core.ports.application.service.healthcheck.service_interface import (
    IService,
)


class Service(IService):
    @inject
    def __int__(self, db: SQLAlchemy):
        self.db = db

    def get_status(self) -> bool:
        is_database_working = True

        try:
            self.db.engine.execute("SELECT 1")
        except (Exception,) as e:
            print(str(e))
            is_database_working = False

        return is_database_working
