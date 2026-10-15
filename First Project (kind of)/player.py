import time, random, potion, monster, spell

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.potions = [potion.HealthPotion(), potion.ManaPotion()]

    def use_potion(self):
        if potion.number > 0:
            potion.number -= 1
        else:
            print(f"{self.name} has no {potion.name}s left!\n")
            time.sleep(1)

    def attack(self):
        print(f"{self.name} attacks {monster.name}!")
        time.sleep(1)
        damage = random.randint(5, 10)
        monster.health -= damage
        print(f"{monster.name} takes {damage} damage and now has {monster.health} health.\n")
        time.sleep(1)

    def cast_spell(self):
        if self.mana >= spell.cost:
            self.mana -= spell.cost
        else:
            print(f"{self.name} does not have enough mana to cast {spell.name}!\n")
            time.sleep(1)

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Mana: {self.mana})"