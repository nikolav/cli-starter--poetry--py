import typer
# from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table


app = typer.Typer(
    help = 'utils - small CLI utility',
  )

@app.command()
def demo():
  # typer.echo(f'utils:demo')
  console = Console()
  table   = Table(title = 'Demo')

  table.add_column('Name')
  table.add_column('Status')
  table.add_column('Foo')
  table.add_row('Build', 'Done', 'foo:1')
  table.add_row('Test', 'Running', 'foo:2')
  table.add_row('Bar', 'Init', 'foo:3')

  console.print(table)

@app.command()
def version():
  typer.echo('0.0.0')
  
def main():
  app()

if __name__ == '__main__':
  main()
