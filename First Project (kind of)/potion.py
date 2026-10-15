import time, player

class Potion:
    def __init__(self, name, effect, initial_number, restore_amount):
        self.name = name
        self.effect = effect
        self.number = initial_number
        self.restore_amount = restore_amount

class HealthPotion(Potion):
    def __init__(self):
        super().__init__("Health Potion", "Restores 20 health.", 3, 20)

    if player.use_potion(self):
        player.health += self.restore_amount
        print(f"{player.name} uses a {self.name} and restores {self.restore_amount} health.\n")
        print(f"{player.name} now has {player.health} health.\n")
        time.sleep(1)

class ManaPotion(Potion):
    def __init__(self):
        super().__init__("Mana Potion", "Restores 10 mana.", 3, 10)

    if player.use_potion(self):
        player.mana += self.restore_amount
        print(f"{player.name} uses a {self.name} and restores {self.restore_amount} mana.\n")
        print(f"{player.name} now has {player.mana} mana.\n")
        time.sleep(1)