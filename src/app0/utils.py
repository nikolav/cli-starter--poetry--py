import typer
# from typing_extensions import Annotated

app = typer.Typer(
    help = 'utils - small CLI utility',
  )

@app.command()
def demo():
  typer.echo(f'utils:demo')

@app.command()
def version():
  typer.echo('0.0.0')
  
def main():
  app()

if __name__ == '__main__':
  main()
