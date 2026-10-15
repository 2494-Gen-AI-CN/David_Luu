import player, random, time

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 200

    def attack(self):
        print(f"{self.name} attacks {player.name}!\n")
        time.sleep(1)
        damage = random.randint(10, 20)
        player.health -= damage
        print(f"{player.name} takes {damage} damage and now has {player.health} health.\n")
        time.sleep(1)

    def __str__(self):
        return f"{self.name} (Health: {self.health})"