import random
import pygame
import time
from all_items import*
tilesize = 42
black = (0, 0, 0)
class plr:
    def __init__(self):
        self.width = tilesize
        self.heigth = tilesize
        self.cls_tot = 'press the rogue before starting!'
        self.clas = 'rogue'
        self.potions = random.randint(1, 6)
        self.n = ''
        self.chat = False
        plr.open_shop = False
        plr.inventory_not_open = True
        self.mana = 0
        self.max_mana = 0
        plr.bandits_killed = 0
        self.level = 1
        self.armour = {
            'helmet':{'name':'', 'defense':0, 'intelligence':0, 'stat':'int'},
            'chestplate':{'name':'', 'defense':0, 'health':0, 'stat':'hp'},
            'leggings':{'name':'', 'defense':0, 'strength':0, 'stat':'str'},
            'gauntlets':{'name':'', 'defense':0, 'mana':0, 'stat':'mana'},
            'boots':{'name':'', 'defense':0, 'stamina':0, 'stat':'stamina'}}
        self.armour_list = []
        self.xp = 0
        self.quest = ''
        self.nxt_lvl_xp = 0
        self.weap = ''
        self.item_img = []
        self.items = []
        self.money = 20+random.randint(1, 20)
        self.tot_hp = 0
        self.hp = 0
        self.mon_dam = 0
        self.mon_hp = 0+5
        self.plwd = 0
        self.stamina = 0
        self.str = 0+4
        self.int = 0+4
        self.defense = 0
        clas_img = pygame.image.load('img\HeroKnight_Idle_2.png')
        image_to_load = pygame.transform.scale(clas_img, (tilesize, tilesize))
        self.clas_img = pygame.Surface([self.width, self.heigth])
        self.clas_img.set_colorkey(black)
    def armour_add(self, armour_pos, armour_nam):
        armour_nam = armour_items[armour_nam]['item']
        armour_def = armour_items[armour_nam]['def']
        armour_stat = armour_items[armour_nam]['add']
        if armour_nam != plr.armour[armour_pos]['name']:
            self.defense = 0
            self.armour[armour_pos]['name']=armour_nam
            self.armour[armour_pos]['defense']=armour_def
            if self.armour[armour_pos]['stat'] == 'int':
                self.int += armour_stat
                self.armour[armour_pos]['intelligence']=armour_stat
            elif self.armour[armour_pos]['stat'] == 'hp':
                self.tot_hp += armour_stat
                self.armour[armour_pos]['health']=armour_stat
            elif self.armour[armour_pos]['stat'] == 'str':
                self.str += armour_stat
                self.armour[armour_pos]['strength']=armour_stat
            elif self.armour[armour_pos]['stat'] == 'mana':
                self.max_mana += armour_stat
                self.armour[armour_pos]['mana']=armour_stat
            elif self.armour[armour_pos]['stat'] == 'stamina':
                self.stamina += armour_stat
                self.armour[armour_pos]['stamina']=armour_stat
            for i in possible_armour:
                self.defense += self.armour[i]['defense']
                plr.armour_list.append(self.armour[i]['name'])
        else:
            print("alredy there")
def class_name_maker():
    plr.n = input("whats your name:")
    print(plr.n)
    class_list = ['barbarian', 'rogue', 'warrior', 'wizard']
    print("you can be a {0}, {1}, {2}, {3}".format(*class_list))
    cl = 'w'
    while cl not in class_list: 
        cl = input("what class are you: ")
        cl.lower           
        if cl in class_list:
            plr.clas = cl
            if cl == 'rogue':
                plr.clas_img = pygame.image.load('img\HeroKnight_Idle_2.png')
            elif cl == 'warrior':
                plr.clas_img = pygame.image.load('img\HeroKnight_Idle_2.png')
            elif cl == 'barbarian':
                plr.clas_img = pygame.image.load('img\HeroKnight_Idle_2.png')
            elif cl == 'wizard':
                plr.clas_img = pygame.image.load('img\HeroKnight_Idle_2.png')
                
def stre_inte_maker():
    if plr.clas == 'barbarian':
        x = 3
        y = -2
        z = 1
        plr.mana = 20
    if plr.clas == 'rogue':
        x = 0
        y = 1
        z = 3
        plr.man = 40
    if plr.clas == 'warrior':
        x = 1
        y = 0
        z = 2
        plr.mana = 40
    if plr.clas == 'wizard':
        x = -2
        y = 3
        z = 0
        plr.mana = 80

    d = random.randint(1, 17)+6
    b = random.randint(1, 17)+3
    c = random.randint(1, 4)+5
    plr.str = d+x
    plr.int = b+y
    plr.mana += plr.int*5
    plr.max_mana = plr.mana
    plr.stamina = c+z
def weapon_armour_maker():
    for i in possible_armour:
        plr.armour_add(plr, i, f'leather {i}')
        plr.items.append(f'leather {i}')

    for key, value in starter_weapons.items():
            print(key, ":", value)
    x = 'e'
    while x not in starter_weapons:       
        x = input("what weapon do you choose: ")
        if x in starter_weapons:
            plr.item_img.append(starter_weapons[x]['img'])
            plr.weap = starter_weapons[x]['weapon']
            plr.items.append(starter_weapons[x]['weapon'])
            plr.plwd = starter_weapons[plr.weap]['damage']

def hp_maker():
    c = random.randint(1, 20)+5
    c = round(c + (plr.str/4))
    plr.hp = c
    plr.tot_hp = c
def monster_maker():
    f = plr.hp / 6
    x = round(f)
    r = random.randint(1, 2)
    if r == 1:
        plr.mon_dam = random.randint(1, 3)+1
        plr.mon_hp=random.randint(3, 4)+x
    elif r == 2:
        plr.mon_dam = random.randint(1, 2)+2
        plr.mon_hp=random.randint(2, 5)+x
def stat_show():
    x = plr.n, plr.str, plr.int, plr.stamina, plr.hp, plr.potions
    b = ("hello {} stats: str = {} int = {} stam = {} hp = {} potions = {}".format(*x))
    plr.cls_tot = b
    print(b)    

def start_game():
    plr.__init__(plr)
    class_name_maker()
    stre_inte_maker()
    hp_maker()
    weapon_armour_maker()
    monster_maker()
    stat_show()

