import logging

from sqlalchemy.orm import Session

from internal.core.ports.application.service.healthcheck.service_interface import (
    IService,
)

logger = logging.getLogger(__name__)


class Service(IService):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_status(self) -> bool:
        is_database_working = True

        try:
            self.session.execute("SELECT 1")
        except (Exception,) as e:
            logger.error("%s", e)
            is_database_working = False

        return is_database_working
