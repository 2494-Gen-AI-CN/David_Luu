import potion as p

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.potions = [
            p.HealthPotion("Health Potion", "Restores 20 health.", 3, 20),
            p.ManaPotion("Mana Potion", "Restores 10 mana.", 3, 10)
            ]

    def drink_potion(self, potion):
        if potion in self.potions:
            self.health += potion.restore_amount
            self.potions.remove(potion)
            print(f"{self.name} drank a {potion.name} and healed for {potion.restore_amount} health!")
        else:
            print(f"{self.name} doesn't have a {potion.name} to drink.")