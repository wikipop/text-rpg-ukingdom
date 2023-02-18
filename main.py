"""
Text-based RPG
- Wiktor Popiołek
"""
from helper_f import delay, print_stats
from player import Player
from rich.console import Console


def start(console):
    return Player("Wiktor", 100, 10, 0, 0)

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

    while player.is_alive():
        print_stats(player, console)
        delay(10)


if __name__ == '__main__':
    main()
