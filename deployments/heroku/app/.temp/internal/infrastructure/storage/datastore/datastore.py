from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Datastore:
    def __init__(self, conn_string: str):
        self.conn_string = conn_string

    def build_session(self):
        engine = create_engine(url=self.conn_string)
        connection = engine.connect()
        return Session(bind=connection)

    @staticmethod
    def session_factory(datastore):
        return datastore.build_session()
