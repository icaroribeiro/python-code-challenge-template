import os


class Env:
    def __init__(self):
        pass

    @staticmethod
    def get_env_with_default_value(key: str, default_value: str) -> str:
        return os.environ.get(key, default_value)
