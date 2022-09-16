from comd.api import create_app
from internal.infrastructure.env.env import Env

env = Env()

http_port = env.get_env_with_default_value(key="HTTP_PORT", default_value="5000")

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=http_port)
