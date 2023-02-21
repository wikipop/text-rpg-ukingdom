"""
Text-based RPG
- Wiktor Popiołek
"""
from helper_f import delay, print_stats, actions, shop
from entity import Player
from combat import combat
from rich.console import Console


def start(console):
    console.print(" ")
    console.print("Welcome to the game!")
    delay(0.5)
    console.print("What is your name?")
    delay(0.5)
    name = input("> ")
    delay(0.5)
    console.print("Hello, " + name + "!")
    delay(1)
    console.print("Long story short, yesterday you had drunk a lot of alcohol and you woke up in a dungeon.")
    delay(2)
    console.print("You don't remember anything, but you know that you have to get out of here.")
    delay(2)

    return Player(name, 100, 10, 0, 0)


def main():
    console = Console()
    player = start(console)
    day = 0
    room = 0

    while player.is_alive():

        if room == 5:
            console.print(" ")
            console.print("You have reached the exit!")
            console.print(" ")
            console.print("Congratulations!")
            console.print(" ")
            exit(0)

        delay(1)
        console.print(f"[bold]====================[/bold]")
        console.print(f"[bold]====== Day  {day} ======[/bold]")
        console.print(f"[bold]====== Room {room} ======[/bold]")
        console.print(f"[bold]====================[/bold]")
        console.print(" ")
        while (action := str(actions(console))) != "4":
            match action:
                case "1":
                    if combat(console, player, day):
                        room = + 1
                        console.print(" ")
                        console.print("After long fight...")
                        console.print("You feel that you are getting closer to the exit.")
                        console.print("But also you need to get some rest.")
                        console.print(" ")
                        delay(1)
                        break
                case "2":
                    shop(console, player)
                case "3":
                    print_stats(player, console)
                case _:
                    console.print("Wrong input!")

        print("Sleeping...")
        delay(1)
        day = + 1


if __name__ == '__main__':
    main()
