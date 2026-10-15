import player, monster, time

class Spell:
    def __init__(self, name, effect, cost, damage, health_restore, mana_restore):
        self.name = name
        self.effect = effect
        self.cost = cost
        self.damage = damage
        self.health_restore = health_restore
        self.mana_restore = mana_restore

class CastingMessage:
    def __init__(self, spell):
        self.spell = spell

    def display(self):
        print(f"{player.name} casts {self.spell.name}!\n")
        time.sleep(1)

class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", "A ball of fire that burns the enemy.", 20, 10, 0, 0)

    if player.cast_spell(self):
        CastingMessage(self).display()
        monster.health -= self.damage
        print(f"{monster.name} takes {self.damage} damage and now has {monster.health} health.\n")
        time.sleep(1)

class Freeze(Spell):
    def __init__(self):
        super().__init__("Freeze", "The targeted enemy is frozen in place for one turn.", 10, 0, 0, 0)

    if player.cast_spell(self):
        CastingMessage(self).display()  
        print(f"{monster.name} is frozen and cannot attack this turn!\n")
        time.sleep(1)

class FullHeal(Spell):
    def __init__(self):
        super().__init__("Full Heal", "A spell that fully restores health.", 25, 0, 100, 0)

    if player.cast_spell(self):
        player.health = self.health_restore
        print(f"{player.name} fully restores health and now has {player.health} health.\n")
        time.sleep(1)