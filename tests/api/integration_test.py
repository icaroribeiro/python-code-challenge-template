import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from internal.infrastructure.env.env import Env
from internal.infrastructure.storage.datastore.base import Base


class IntegrationTest:
    @pytest.fixture(scope="session", autouse=True)
    def engine(self):
        env = Env()

        driver = env.get_env_with_default_value(
            key="DB_DRIVER", default_value="postgresql"
        )
        user = env.get_env_with_default_value(key="DB_USER", default_value="postgres")
        password = env.get_env_with_default_value(
            key="DB_PASSWORD", default_value="postgres"
        )
        host = env.get_env_with_default_value(key="DB_HOST", default_value="localhost")
        port = env.get_env_with_default_value(key="DB_PORT", default_value="5432")
        name = env.get_env_with_default_value(key="DB_NAME", default_value="testdb")

        conn_string = "{driver}://{user}:{password}@{host}:{port}/{name}".format(
            driver=driver,
            user=user,
            password=password,
            host=host,
            port=port,
            name=name,
        )

        return create_engine(url=conn_string)

    @pytest.fixture(scope="session")
    def tables(self, engine):
        Base.metadata.create_all(engine)
        yield
        Base.metadata.drop_all(engine)

    @pytest.fixture
    def session(self, engine, tables):
        connection = engine.connect()
        transaction = connection.begin()
        session = Session(bind=connection)
        try:
            yield session
        except (Exception,):
            session.rollback()
        finally:
            session.close()
            transaction.rollback()
            connection.close()
