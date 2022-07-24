import typer

from tools.api.commands.run import RunCmd
from tools.api.commands.version import VersionCmd

app = typer.Typer()


@app.command()
def version():
    cmd1 = VersionCmd()
    cmd1.run()


@app.command()
def run():
    cmd1 = RunCmd()
    cmd1.run()


if __name__ == "__main__":
    app()
