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