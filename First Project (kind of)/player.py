import time
import random
import potion
import monster
import spell

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.potions = [potion.HealthPotion(), potion.ManaPotion()]

    def use_potion(self, potion_type):
        for p in self.potions:
            if isinstance(p, potion_type) and p.number > 0:
                if isinstance(p, potion.HealthPotion):
                    self.health += p.restore_amount
                    print(f"{self.name} uses a {p.name} and restores {p.restore_amount} health.")
                elif isinstance(p, potion.ManaPotion):
                    self.mana += p.restore_amount
                    print(f"{self.name} uses a {p.name} and restores {p.restore_amount} mana.")
                p.number -= 1
                time.sleep(1)
                return True
        print(f"{self.name} has no {potion_type.__name__}s left!")
        time.sleep(1)
        return False

    def attack(self, monster):
        print(f"{self.name} attacks {monster.name}!")
        time.sleep(1)
        damage = random.randint(5, 10)
        monster.health -= damage
        print(f"{monster.name} takes {damage} damage and now has {monster.health} health.")
        time.sleep(1)
        return damage

    def is_alive(self):
        return self.health > 0
