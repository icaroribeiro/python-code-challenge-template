import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from internal.infrastructure.env.env import Env


def build_scoped_session():
    conn_string: any

    deploy = Env.get_env_with_default_value(key="DEPLOY", default_value="NO")
    if deploy == "YES":
        conn_string = os.environ.get("DATABASE_URL")
    else:
        driver = Env.get_env_with_default_value(
            key="DB_DRIVER", default_value="postgres"
        )
        user = Env.get_env_with_default_value(key="DB_USER", default_value="postgres")
        password = Env.get_env_with_default_value(
            key="DB_PASSWORD", default_value="postgres"
        )
        host = Env.get_env_with_default_value(key="DB_HOST", default_value="localhost")
        port = Env.get_env_with_default_value(key="DB_PORT", default_value="5432")
        name = Env.get_env_with_default_value(key="DB_NAME", default_value="db")
        conn_string = "{driver}://{user}:{password}@{host}:{port}/{name}".format(
            driver=driver,
            user=user,
            password=password,
            host=host,
            port=port,
            name=name,
        )
    print(conn_string)
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/db")

    # Session = sessionmaker(bind=engine)
    # connection = engine.connect()
    return scoped_session(sessionmaker(bind=engine))


_abc = build_scoped_session()


def MySession():
    return _abc()
