from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session

from internal.core.ports.application.service.healthcheck.service_interface import (
    IService,
)


class Service(IService):
    def __init__(self, datastore_factory) -> None:
        self.datastore_factory = datastore_factory

    def get_status(self) -> bool:
        is_database_working = True

        try:
            with self.datastore_factory.session() as session:
                session.execute("SELECT 1")
        except (Exception,) as e:
            print("error:", e)
            is_database_working = False

        return is_database_working
