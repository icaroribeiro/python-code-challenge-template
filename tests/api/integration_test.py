import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from internal.infrastructure.env.env import Env


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

    @pytest.fixture
    def session(self, engine):
        connection = engine.connect()

        transaction = connection.begin()

        session = Session(bind=connection)

        yield session

        session.close()

        transaction.rollback()

        connection.close()
