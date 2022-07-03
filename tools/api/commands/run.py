from cmd.api import create_app

app = create_app("dev")


class RunCmd:
    def __init__(self):
        pass

    @staticmethod
    def run():
        app.run(())
