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

    def use(self, player):
        if player.health >= 100:
            print(f"{player.name} is already at full health!\n")

        else:
            player.health += self.restore_amount

            if (player.health > 100):
                player.health = 100
            
            print(f"{player.name} restored {self.restore_amount} health!\n")

        time.sleep(3)

class ManaPotion(Potion):
    def __init__(self):
        super().__init__("Mana Potion", "Restores 10 mana.", 3, 10)

    def use(self, player):
        if player.mana >= 50:
            print(f"{player.name} is already at full mana!\n")

        else:
            player.mana += self.restore_amount
            
            if (player.mana > 50):
                player.mana = 50
            
            print(f"{player.name} restored {self.restore_amount} mana!\n")

        time.sleep(3)