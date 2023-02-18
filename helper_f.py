import time
from rich.table import Table


def print_stats(entity, console):
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Stat", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("[bold]Name[/bold]", f"[bold]{str(entity.name)}[/bold]")
    if entity.gold:
        table.add_row("[yellow]Gold[/yellow]", f"[yellow]{str(entity.gold)}[/yellow]")
    table.add_row("Max Health", str(entity.hp))
    table.add_row("Attack", str(entity.atk))
    table.add_row("Defense", str(entity.df))

    console.print(table)


def delay(timeH=1):
    time.sleep(timeH)
