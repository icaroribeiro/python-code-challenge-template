import contextlib
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class Datastore:
    def __init__(self, conn_string: str):
        print("conn_string:", conn_string)
        self.engine = create_engine(url=conn_string)
        # self.session_factory = Session(bind=self.engine.connect())
        self.session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine,
            ),
        )

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        # session = self.session_factory
        session = self.session_factory()
        try:
            yield session
        except (Exception,):
            session.rollback()
        finally:
            session.close()
