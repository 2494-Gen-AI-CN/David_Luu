import time

class Spell:
    def __init__(self, name, effect, cost):
        self.name = name
        self.effect = effect
        self.cost = cost

    def cast(self, player, monster):
        if player.mana < self.cost:
            print(f"\n{player.name} does not have enough mana to cast {self.name}!\n")
            time.sleep(3)
            return
        player.mana -= self.cost
        print(f"\n{player.name} casts {self.name}!\n")
        time.sleep(3)
        self.apply(player, monster)

    def apply(self, player, monster):
        raise NotImplementedError

class Fireball(Spell):
    damage = 10

    def __init__(self):
        super().__init__("Fireball", "A ball of fire that burns the enemy for 10 damage.", 15)

    def apply(self, player, monster):
        monster.health -= self.damage
        if monster.health < 0:
            monster.health = 0
            
        print(f"{monster.name} takes {self.damage} damage and now has {monster.health} health.\n")
        time.sleep(3)

class Freeze(Spell):
    def __init__(self):
        super().__init__("Freeze", "The targeted enemy is frozen in place for one turn.", 10)

    def apply(self, player, monster):
        monster.freeze = True
        print(f"{monster.name} is frozen and will skip its next turn!\n")
        time.sleep(3)

class FullHeal(Spell):
    def __init__(self):
        super().__init__("Full Heal", "A spell that fully restores health.", 25)

    def apply(self, player, monster):
        if player.health >= 100:
            print(f"{player.name} is already at full health!\n")
            time.sleep(3)
            return
        player.health = 100

        print(f"{player.name} is fully healed!\n")
        time.sleep(3)