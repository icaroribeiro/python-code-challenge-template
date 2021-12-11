import typer

import tools.api.api


class VersionCmd:
    def __init__(self):
        pass

    @staticmethod
    def run():
        typer.echo(f"api v{tools.api.api.VERSION}\n")
