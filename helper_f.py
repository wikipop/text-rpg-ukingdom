import time

from rich.console import Console
from rich.table import Table

from entity import Player, Enemy


def print_stats(entity, console):
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Stats", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("[bold]Name[/bold]", f"[bold]{str(entity.name)}[/bold]")
    if entity.gold:
        table.add_row("[yellow]Gold[/yellow]", f"[yellow]{str(entity.gold)}[/yellow]")
    table.add_row("Max Health", str(entity.hp))
    table.add_row("Attack", str(entity.atk))
    table.add_row("Defense", str(entity.df))

    console.print(table)


def actions(console: Console):
    console.print("What do you want to do?")
    console.print("[bold]1.[/bold] Go to the next room")
    console.print("[bold]2.[/bold] Go to the shop")
    console.print("[bold]3.[/bold] Show stats")
    console.print("[bold]4.[/bold] Sleep")

    return str(input("> "))


def shop(console: Console, player: Player):
    table = Table(show_header=True, header_style="yellow bold")
    table.add_column("Item")
    table.add_column("Price", style="yellow")
    table.add_column("Effect")
    table.add_row("Potion", "10$", "Heal 10 HP")
    table.add_row("Sword", "20$", "Increase attack by 5")
    table.add_row("Shield", "20$", "Increase defense by 5")

    console.print(table)


def generate_room(console: Console, day):
    console.print("You go to the next room.")
    delay(1)
    console.print("You see enemies!")
    enemies = [Enemy(day) for x in range(1, day + 1)]
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Enemy")
    table.add_column("Health", style="red bold")
    table.add_column("Attack", style="red")
    table.add_column("Defense", style="red")

    for enemy in enemies:
        table.add_row(str(enemy.name), str(enemy.hp), str(enemy.atk), str(enemy.df))
    console.print(table)
    delay(1)
    console.print("What do you want to do?")
    console.print("[bold]1.[/bold] Fight")
    console.print("[bold]2.[/bold] Run")
    console.print("[bold]3.[/bold] Show stats")

    return str(input("> "))


def delay(timeH=1):
    time.sleep(timeH)
