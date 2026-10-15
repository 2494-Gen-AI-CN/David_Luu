import time

from player import Player
from monster import Monster
from spell import Fireball, Freeze, FullHeal
from turn import TurnCounter

def spell_menu(hero, enemy):
    spells = [Fireball(), Freeze(), FullHeal()]

    while True:
        print("\n===== Spell Menu =====\n")
        for i, s in enumerate(spells, 1):
            print(f"{i}. {s.name} (cost {s.cost}): {s.effect}")
        print("4. Back\n")
        pick = input("Choose a spell: ")

        if pick == "4":
            print()
            return False

        if pick in ("1", "2", "3"):
            spell = spells[int(pick) - 1]
            if hero.mana < spell.cost:
                print(f"\nNot enough mana to cast {spell.name}! You have {hero.mana}, but it costs {spell.cost}.\n")
                continue
            hero.cast_spell(spell, enemy)
            return True

        print("\nInvalid choice, try again.\n")


def potion_menu(hero):
    print("\n===== Potion Menu =====\n")
    
    while True:
        for i, p in enumerate(hero.potions, 1):
            print(f"{i}. {p.name} x{p.number}: {p.effect}")
        print("3. Back\n")
        pick = input("Choose a potion: ")

        if pick == "3":
            print()
            return False

        if pick in ("1", "2"):
            potion = hero.potions[int(pick) - 1]
            if potion.number <= 0:
                print(f"\nYou have no {potion.name}s left!")
                continue
            hero.use_potion(potion)
            return True

        print("\nInvalid choice, try again.\n")


def player_turn(hero, enemy):
    while True:
        print(hero)
        print(enemy, "\n")
        print("1. Attack\n2. Cast a spell\n3. Use a potion\n")
        choice = input("Choose an action: ")

        if choice == "1":
            hero.attack(enemy)
            return

        elif choice == "2":
            if spell_menu(hero, enemy):
                return

        elif choice == "3":
            if potion_menu(hero):
                return

        else:
            print("\nInvalid choice, try again.\n")

def main():
    print("\nWelcome to the game!\n")
    time.sleep(3)

    hero = Player(input("Enter your name: "))
    enemy = Monster(input("Enter the name of the monster: "))

    print(f"\n{hero.name}, you are a knight of the Royal Army of Sir Brennenberg.\n")
    time.sleep(3)
    print(f"The kingdom where you and the king is under attack by a mysterious beast named {enemy.name}!\n")
    time.sleep(3)
    print(f"The king has sent you to defeat {enemy.name} and save the kingdom!\n")
    time.sleep(3)
    print(f"{hero.name} has arrived where {enemy.name} is waiting.\n")
    time.sleep(3)
    print(f"{enemy.name} has seen {hero.name} and charges at you!\n")
    time.sleep(3)

    print("Battle Start!\n")
    time.sleep(3)

    turns = TurnCounter()

    while hero.health > 0 and enemy.health > 0:
        turns.display()
        player_turn(hero, enemy)

        if enemy.health <= 0:
            break

        if enemy.is_frozen():
            print(f"{enemy.name} is frozen and skips its turn!\n")
            time.sleep(3)
            enemy.freeze = False

        else:
            enemy.attack(hero)

        turns.next_turn()

    if hero.health > 0:
        print(f"{hero.name} has defeated {enemy.name}!\n")
        time.sleep(3)
        print("The kingdom is saved! The people rejoice! They celebrate your victory!\n")
        time.sleep(3)
        print(f"{hero.name} returns to the king.\n")
        time.sleep(3)
        print(f"The king thanks {hero.name} for saving the kingdom and rewards you with by making you his right-hand!\n")
        time.sleep(3)
        print(f"{hero.name} is now the right-hand of the king and will be remembered as a hero! Congratulations!\n")
        time.sleep(3)
        print(f"You defeated {enemy.name} in {turns.turn} turn(s)!\n")

    else:
        print(f"{enemy.name} has defeated {hero.name}!\n")
        time.sleep(3)
        print("The beast went to slaughter the rest of the people in the kingdom!\n")
        time.sleep(3)
        print("No survivors were spared! No army could stop the beast! The king is dead! The kingdom is lost!\n")
        time.sleep(3)
        print(f"{hero.name} has failed in their quest.\n")
        time.sleep(3)
        print(f"{hero.name} was defeated on turn {turns.turn}.\n")

if __name__ == "__main__":
    main()