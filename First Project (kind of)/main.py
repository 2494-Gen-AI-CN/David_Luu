import monster, spell, player, potion, time

def main():

    print("Welcome to the game!\n")
    time.sleep(1)
    player_name = input("Enter your name: ")
    player = player.Player(player_name)
    monster_name = input("Enter the name of the monster you want to fight: ")
    monster = monster.Monster(monster_name)