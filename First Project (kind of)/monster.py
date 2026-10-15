import player
import random
import time

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, player):
        print(f"{self.name} attacks {player.name}!")
        time.sleep(1)
        damage = random.randint(10, 20)
        player.take_damage(self)
        print(f"{player.name} takes {damage} damage and now has {player.health} health.")
        time.sleep(1)
        return damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health})"