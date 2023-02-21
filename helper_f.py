import time

from rich.console import Console
from rich.table import Table

from entity import Player


def print_stats(entity, console):
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Stats", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("[bold]Name[/bold]", f"[bold]{str(entity.name)}[/bold]")
    if entity.gold:
        table.add_row("[yellow]Gold[/yellow]", f"[yellow]{str(entity.gold)}[/yellow]")
    table.add_row("Health", str(entity.hp))
    table.add_row("Attack", str(entity.atk))
    table.add_row("Defense", str(entity.df))

    console.print(table)


def actions(console: Console):
    console.print(" ")
    console.print("What do you want to do?")
    console.print("[bold]1.[/bold] Go to the next room")
    console.print("[bold]2.[/bold] Go to the shop")
    console.print("[bold]3.[/bold] Show stats")
    console.print("[bold]4.[/bold] Sleep")
    console.print(" ")
    return str(input("> "))


def shop(console: Console, player: Player):
    table = Table(show_header=True, header_style="yellow bold")
    table.add_column("Item")
    table.add_column("Price", style="yellow")
    table.add_column("Effect")
    table.add_row("Potion", "10$", "Heal 10 HP")
    table.add_row("Sword", "20$", "Increase attack by 5")
    table.add_row("Shield", "20$", "Increase defense by 5")
    table.add_row("Boots", "30$", "Increase initiation by 3")
    console.print(table)

    # Nie chcę mi się tworzyć datadclass dla przedmiotów, ale byłoby to bardziej poprawne
    while True:
        console.print(" ")
        console.print(f"Your gold: [yellow][bold]{player.gold}[/yellow][/bold]")
        console.print(" ")
        console.print("[cyan]Shopkeeper[/cyan]: Would you like to buy something?")
        console.print("Type [red][bold]exit[/bold][/red] when you are ready")
        console.print(" ")
        prompt = input("> ")
        console.print(" ")
        if prompt.lower() == "exit":
            break

        match prompt.lower():
            case "potion":
                if player.gold >= 10:
                    player.gold -= 10
                    player.hp += 10
                    console.print("[cyan]Shopkeeper[/cyan]: Thank you!")
                else:
                    console.print("[cyan]Shopkeeper[/cyan]: You cant afford this item!")
            case "sword":
                if player.gold >= 20:
                    player.gold -= 20
                    player.atk += 5
                    console.print("[cyan]Shopkeeper[/cyan]: Thank you!")
                else:
                    console.print("[cyan]Shopkeeper[/cyan]: You cant afford this item!")
            case "shield":
                if player.gold >= 20:
                    player.gold -= 20
                    player.df += 5
                    console.print("[cyan]Shopkeeper[/cyan]: Thank you!")
                else:
                    console.print("[cyan]Shopkeeper[/cyan]: You cant afford this item!")
            case "boots":
                if player.gold >= 30:
                    player.gold -= 30
                    player.initiation += 3
                    console.print("[cyan]Shopkeeper[/cyan]: Thank you!")
                else:
                    console.print("[cyan]Shopkeeper[/cyan]: You cant afford this item!")
            case _:
                print("Wrong input!")


def delay(timeH=1):
    time.sleep(timeH)
