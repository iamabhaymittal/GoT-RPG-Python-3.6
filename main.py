from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 30, 800, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaelixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]

# player_items = [potion, hipotion, superpotion, elixir, megaelixir, grenade]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 15},
                {"item": megaelixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

#Instantiate People
player1 = Person(" Jon:",3160, 132, 300, 34, player_spells, player_items)
player2 = Person("Arya:",4160, 138, 311, 34, player_spells, player_items)
player3 = Person("Dany:",3089, 174, 288, 34, player_spells, player_items)

enemy = Person("The Night King",21200, 751, 625, 25, [],[])

players = [player1, player2, player3]

running = True
i = 0
print("===================================")
print(bcolors.OKBLUE + bcolors.BOLD + "Winter is Here!" + bcolors.ENDC)
print("===================================")
print(bcolors.FAIL + bcolors.BOLD + "The Long Night has begun. \nProtect the north from the dead by \nneutralizing the Night King \nbefore he adds you to his army!" + bcolors.ENDC)

while running:
    print("===================================")

    print("\n\n")
    print("NAME:              HP                                      MP")
    for player in players:
        player.get_stats()

    print("\n")
    enemy.get_enemy_status()
    for player in players:

        player.choose_action()
        choice = input("    Choose Action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(player.name+" Attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic:")) - 1

            if magic_choice == -1:
                continue
            # magic_dmg = player.generate_spell_damage(magic_choice)
            # spell = player.get_spell_name(magic_choice)
            # cost = player.get_spell_mp_cost(magic_choice)
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "Item exhausted..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1


            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.type == "megaelixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "HP" + bcolors.ENDC)

    character_set = [0,1,2]
    target = random.choice(character_set)


    enemy_dmg = enemy.generate_damage()
    players[target].take_damage(enemy_dmg)
    print("The NK attacked " + players[target].name + "for", enemy_dmg, "points of damage.")

    # print("---------------------------------------")
    # print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp())+ "\n" + bcolors.ENDC)
    # print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    #
    # print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif players[target].get_hp() == 0:
        if target == 0:
            print(bcolors.FAIL + "We've lost Jon!" + bcolors.ENDC)
            character_set.remove(0)
        if target == 1:
            print(bcolors.FAIL + "We've lost Arya!" + bcolors.ENDC)
            character_set.remove(1)
        if target == 2:
            print(bcolors.FAIL + "We've lost Dany!" + bcolors.ENDC)
            character_set.remove(2)
        k=0
        for i in players:
            k += i.hp
        if k == 0:
            print(bcolors.FAIL + bcolors.BOLD + "The NIGHT KING WINS!!" + bcolors.ENDC)
            running = False

