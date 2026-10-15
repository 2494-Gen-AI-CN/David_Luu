import time

class Potion:
    def __init__(self, name, effect, initial_number, restore_amount):
        self.name = name
        self.effect = effect
        self.number = initial_number
        self.restore_amount = restore_amount

class HealthPotion(Potion):
    def __init__(self):
        super().__init__("Health Potion", "Restores 20 health.", 3, 20)

class ManaPotion(Potion):
    def __init__(self):
        super().__init__("Mana Potion", "Restores 10 mana.", 3, 10)