from internal.di.di import AppContainer
from internal.transport.presentation.handler.healthcheck import (
    handler as healthcheck_handler,
)
from tools.api.commands import create_app

app = create_app("dev")


class RunCmd:
    def __init__(self):
        pass

    @staticmethod
    def run():
        app.run()
