import time, random, potion, monster, spell

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.potions = [potion.HealthPotion(), potion.ManaPotion()]

    def use_potion(self, p):
        if p.number <= 0:
            print(f"No {p.name} left!\n")
            return
        p.number -= 1
        print(f"\n{self.name} uses {p.name}!\n")
        time.sleep(3)
        p.use(self)

    def attack(self, monster):
        print(f"\n{self.name} attacks {monster.name}!")
        time.sleep(3)

        damage = random.randint(5, 10)
        monster.health -= damage
        
        if monster.health < 0:
            monster.health = 0

        print(f"\n{monster.name} takes {damage} damage and now has {monster.health} health.\n")
        time.sleep(3)

    def cast_spell(self, spell, monster):
        spell.cast(self, monster)

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Mana: {self.mana})"