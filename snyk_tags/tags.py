#! /usr/bin/env python3

import logging
import typer

from typing import Optional
from snyk_tags import __app_name__, __version__, apply


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
)

app = typer.Typer()
app.add_typer(apply.app, name="apply")

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

def _name_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit",
        callback=_version_callback,
        is_eager=True,
    ), name: Optional[bool] = typer.Option(
        None,
        "--name",
        "-n",
        help="Show the application's name and exit",
        callback=_name_callback,
        is_eager=True,
    )
) -> None:
    return
