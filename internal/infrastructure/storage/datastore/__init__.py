import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from internal.infrastructure.env.env import Env

env = Env()

conn_string: str

deploy = Env.get_env_with_default_value(key="DEPLOY", default_value="NO")
if deploy == "YES":
    conn_string = os.environ.get("DATABASE_URL")
else:
    driver = Env.get_env_with_default_value(key="DB_DRIVER", default_value="postgres")
    user = ""
    password = ""
    host = ""
    port = ""
    name = ""
    conn_string = "{driver}://{user}:{password}@{host}:{port}/{name}".format(
        driver=driver,
        user=user,
        password=password,
        host=host,
        port=port,
        name=name,
    )

engine = create_engine(url=conn_string)

Session = sessionmaker(bind=engine)
