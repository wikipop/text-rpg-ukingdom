import random
import string

from rich.console import Console


def name_generator():
    return f'{random.choice(string.ascii_uppercase)}' + ''.join(
        random.choices(string.ascii_lowercase, k=random.randint(5, 9)))


class Player:
    def __init__(self, name, hp, atk, df, gold, initiation):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
        self.gold = gold
        self.initiation = initiation

    def take_damage(self, damage, console, name):
        console.print(" ")
        console.print(f"{name} delt you {damage}!")
        console.print(f"You are now at {round(self.hp - (damage / 100 * (100 - self.df)))} health points.")
        console.print(" ")
        self.hp -= round(damage / 100 * (100 - self.df))

    def deal_damage(self, enemy, console: Console):
        enemy.take_damage(self.atk, console)

    def add_gold(self, gold):
        self.gold += gold

    def remove_gold(self, gold):
        self.gold -= gold

    def is_alive(self):
        return self.hp > 0


class Enemy:
    def __init__(self, lvl, EId):
        self.name = f"[bold][[cyan]{lvl} lvl[/cyan]][/bold] {name_generator()}"
        self.hp = 20 + lvl * 6
        self.atk = 2 + lvl
        self.df = 0 + lvl
        self.id = EId
        self.initiation = lvl
        self.alive = True

    def take_damage(self, damage, console: Console):
        console.print(" ")
        console.print(f"{self.name} has taken {damage / 100 * (100 - self.df)} damage!")
        console.print(f"{self.name} is now at {round(self.hp - (damage / 100 * (100 - self.df)))} health points.")
        self.hp -= round(damage / 100 * (100 - self.df))
        if self.hp <= 0:
            self.alive = False
            console.print(f"[bold][red]{self.name} has died! [/bold][/red]")
        console.print(" ")

    def deal_damage(self, enemy, console):
        enemy.take_damage(self.atk, console, self.name)
