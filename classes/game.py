import random
from .magic import Spell
import pprint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack","Magic","Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    # def generate_spell_damage(self, i):
    #     mgl = self.magic[i]["dmg"] - 5
    #     mgh = self.magic[i]["dmg"] + 5
    #     return random.randrange(mgl,mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp =0
        return self.hp

    def heal(self, dmg):
        self.hp +=dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]["name"]
    #
    # def get_spell_mp_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1

        print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD +"    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1


    def choose_magic(self):
        i = 1
        
        print("\n" + bcolors.OKBLUE + bcolors.BOLD +"    Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i += 1


    def get_enemy_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) *50

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += "  "

        print("\n")
        print(bcolors.BOLD + self.name + "  " +
              str(self.hp) + "/" + str(self.maxhp) + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|"  )

    def get_stats(self):


        bar_ticks = int((self.hp / self.maxhp) * 25)
        hp_bar = ""
        while bar_ticks >0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += "  "

        bar_ticks = int((self.mp / self.maxmp) * 10)
        mp_bar = ""
        while bar_ticks > 0:
            mp_bar += "█"
            bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += "  "

        print("\n")
        print(bcolors.BOLD + self.name + "  " +
              str(self.hp) + "/"+ str(self.maxhp) +" |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|   " + str(self.mp) + "/" + str(self.maxmp) + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
