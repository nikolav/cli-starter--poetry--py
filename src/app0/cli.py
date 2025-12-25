import typer
from typing_extensions import Annotated

app = typer.Typer(
    help = 'app0 - small CLI utility',
  )

@app.command()
def hello(name: Annotated[str, typer.Argument()] = 'world'):
  typer.echo(f'Hello, {name}!')

@app.command()
def demo():
  typer.echo('running app0:demo')

@app.command()
def version():
  typer.echo("0.0.0")

def main():
  app()

if __name__ == '__main__':
  main()
