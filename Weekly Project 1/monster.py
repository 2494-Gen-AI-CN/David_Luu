import random, time

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.freeze = False

    def attack(self, player):
        print(f"{self.name} attacks {player.name}!\n")
        time.sleep(3)
        
        damage = random.randint(10, 20)
        player.health -= damage

        if player.health < 0:
            player.health = 0

        print(f"{player.name} takes {damage} damage and now has {player.health} health.\n")
        time.sleep(3)

    def is_frozen(self):
        return self.freeze

    def __str__(self):
        return f"{self.name} (Health: {self.health})"