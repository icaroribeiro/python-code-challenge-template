from sqlalchemy.orm import Session

from internal.core.ports.application.service.healthcheck.service_interface import (
    IService,
)


class Service(IService):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_status(self) -> bool:
        is_database_working = True

        try:
            self.session.execute("SELECT 1")
        except (Exception,) as e:
            print("error:", e)
            is_database_working = False

        return is_database_working
