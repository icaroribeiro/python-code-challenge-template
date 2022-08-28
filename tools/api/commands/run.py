from internal.infrastructure.env.env import Env
from tools.api.commands import create_app

env = Env()

http_port = env.get_env_with_default_value(key="HTTP_PORT", default_value="5000")

app = create_app()


class RunCmd:
    def __init__(self):
        pass

    @staticmethod
    def run():
        app.run(host="0.0.0.0", port=http_port)
