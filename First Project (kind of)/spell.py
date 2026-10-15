import time
import player

class Spell:
    def __init__(self, name, effect, cost, damage, health_restore, mana_restore):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.damage = damage
        self.health_restore = health_restore
        self.mana_restore = mana_restore

class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", "A ball of fire that burns the enemy.", 20, 10, 0, 0)

class Freeze(Spell):
    def __init__(self):
        super().__init__("Freeze", "The targeted enemy is frozen in place for one turn.", 10, 0, 0, 0)

class FullHeal(Spell):
    def __init__(self):
        super().__init__("Full Heal", "A spell that fully restores health.", 25, 0, 100, 0)