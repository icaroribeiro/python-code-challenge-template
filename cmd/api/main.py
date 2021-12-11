import typer

from tools.api.commands.run import RunCmd
from tools.api.commands.version import VersionCmd

app = typer.Typer()


@app.command()
def version():
    cmd = VersionCmd()
    cmd.run()


@app.command()
def run():
    cmd = RunCmd()
    cmd.run()


if __name__ == "__main__":
    app()
