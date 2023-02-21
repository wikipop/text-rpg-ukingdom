import random

from rich.console import Console
from entity import Player, Enemy
from helper_f import delay, print_stats
from rich.table import Table


def print_enemies(console: Console, enemies: [Enemy]):
    table = Table(show_header=True, header_style="bold red")
    table.add_column("id", style="yellow bold")
    table.add_column("Enemy")
    table.add_column("Health", style="red bold")
    table.add_column("Attack", style="red")
    table.add_column("Defense", style="red")
    table.add_column("Initiation", style="red")

    for enemy in enemies:
        table.add_row(str(enemy.id), str(enemy.name), str(round(enemy.hp)), str(enemy.atk), str(enemy.df),
                      str(enemy.initiation))
    console.print(" ")
    console.print(table)
    console.print(" ")


def combat(console: Console, player: Player, day):
    console.print("You go to the next room.")
    delay(1)
    console.print("You see enemies!")
    enemies = [Enemy(day, x) for x in range(3)]

    randomEnemy: Enemy = random.choice(enemies)

    if randomEnemy.initiation > player.initiation:
        console.print(" ")
        console.print(
            f"{randomEnemy.name} had better initiation stat ({randomEnemy.initiation}, compared to your {player.initiation}),")
        console.print(f"{randomEnemy.name} has attacked you first!")
        randomEnemy.deal_damage(player, console)
        delay(5)

    while True:
        enemies = list(filter(lambda x: x.alive, enemies))
        if len(enemies) == 0:
            console.print(" ")
            console.print("You have defeated all enemies!")
            reward = random.randint(1, 10) * (day+1)
            console.print(f"and you have gained {reward} gold!")
            player.gold += reward
            break

        if not player.is_alive():
            console.print(" ")
            console.print("You have died!")
            console.print(" ")
            exit(0)

        delay(1)
        print_enemies(console, enemies)
        console.print(" ")
        console.print("What do you want to do?")
        console.print("[bold]1.[/bold] Fight")
        console.print("[bold]2.[/bold] Run")
        console.print("[bold]3.[/bold] Show stats")
        console.print(" ")

        prompt = input("> ")

        match prompt.lower():
            case "1":
                fight(console, player, enemies)
            case "2":
                break
            case "3":
                print_stats(console, player)
            case _:
                console.print("Wrong input!")

    return 1


def fight(console, player, enemies: [Enemy]):
    console.print(" ")
    console.print("[i] Whom will I attack? [/i]")
    console.print("[i] type [bold][red]exit[/bold][/red] to leave [/i]")
    console.print(" ")
    delay(0.5)
    print_enemies(console, enemies)
    ids = [enemy.id for enemy in enemies]

    while (prompt := str(input("> "))).lower() != "exit":
        if int(prompt) in ids:
            enemy: Enemy = list(filter(lambda x: x.id == int(prompt), enemies))[0]
            player.deal_damage(enemy, console)
        else:
            break

        delay(1)

        randomEnemy: Enemy = random.choice(enemies)
        randomEnemy.deal_damage(player, console)
        break
