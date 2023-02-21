import random
import string


def name_generator():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


class Player:
    def __init__(self, name, hp, atk, df, gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
        self.gold = gold

    def take_damage(self, damage):
        self.hp -= damage / 100 * (100 - self.df)

    def deal_damage(self, enemy):
        enemy.take_damage(self.atk)

    def add_gold(self, gold):
        self.gold += gold

    def remove_gold(self, gold):
        self.gold -= gold

    def is_alive(self):
        return self.hp > 0


class Enemy:
    def __init__(self, lvl):
        self.name = f"[${lvl}] ${name_generator()}"
        self.hp = 100+lvl*10
        self.atk = 10+lvl
        self.df = 0+lvl

    def take_damage(self, damage):
        self.hp -= damage / 100 * (100 - self.df)

    def deal_damage(self, enemy):
        enemy.take_damage(self.atk)
