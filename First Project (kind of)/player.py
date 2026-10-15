import time, random, potion, monster, spell

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.potions = [potion.HealthPotion(), potion.ManaPotion()]

    def use_potion(self, potion):
        if potion.number > 0:
            potion.number -= 1
            return True
        else:
            print(f"{self.name} has no {potion.name}s left!\n")
            time.sleep(1)
            return False

    def attack(self, monster):
        print(f"{self.name} attacks {monster.name}!")
        time.sleep(1)
        damage = random.randint(5, 10)
        monster.health -= damage
        print(f"{monster.name} takes {damage} damage and now has {monster.health} health.\n")
        time.sleep(1)
        return damage

    def cast_spell(self, spell):
        if self.mana >= spell.cost:
            self.mana -= spell.cost
            return True
        else:
            print(f"{self.name} does not have enough mana to cast {spell.name}!\n")
            time.sleep(1)
            return False

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Mana: {self.mana})"