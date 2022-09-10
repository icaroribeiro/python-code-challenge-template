import typer

import internal.tools.api.api


class VersionCmd:
    def __init__(self):
        pass

    @staticmethod
    def run():
        typer.echo(f"api v{internal.tools.api.api.VERSION}\n")
