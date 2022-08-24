from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


def build_conn_string():
    return "postgresql://postgres:postgres@localhost:5432/db"


def build_database_engine(conn_string):
    return create_engine(url=conn_string)


def build_scoped_session():
    return None


def session():
    conn_string = build_conn_string()
    engine = build_database_engine(conn_string)
    # return scoped_session(sessionmaker(bind=engine))
    session1 = scoped_session(sessionmaker(bind=engine))
    try:
        yield session1
    except (Exception,):
        session1.rollback()
    finally:
        session1.close()


session20 = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        url="postgresql://postgres:postgres@localhost:5432/db",
        connect_args={"connect_timeout": 10},
    ),
)

_abc = session20()


def sfunc():
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=create_engine(
            url="postgresql://postgres:postgres@localhost:5432/db",
            connect_args={"connect_timeout": 10},
        ),
    )
    # try:
    #     yield session
    # except (Exception,):
    #     session.rollback()
    # finally:
    #     session.close()


session3 = sfunc()


def _cde():
    return next(_abc())


class Datastore:
    def __init__(self, conn_string: str):
        print("conn_string:", conn_string)
        self.engine = create_engine(url=conn_string)
        self.session_factory = _abc

    def get_session(self):
        # return Session(bind=self.engine.connect())
        yield next(self.session_factory())
        # session = scoped_session(sessionmaker(bind=self.engine))
        # connection = self.engine.connect()
        # session = self.session_factory()
        # try:
        #     yield session
        # except (Exception,):
        #     session.rollback()
        # finally:
        #     session.close()

    # @contextmanager
    # def session(self) -> Callable[..., AbstractContextManager[Session]]:
    #     session = self.session_factory
    #     try:
    #         yield session
    #     except (Exception,):
    #         session.rollback()
    #     finally:
    #         session.close()
