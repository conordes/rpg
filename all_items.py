import random
import pygame
bul_dam = random.randint(1, 2)+1
peir_dam = random.randint(1, 3)
mg_pn = random.randint(1, 3)
poss_ar = ['helmet', 'chestplate', 'leggings', 'gauntlets', 'boots']
starter_weapons = {
        "dagger" : {'weapon' : 'dagger', 'damage' : 6, 'img':"img\items\Weapons\dagger.png"},
        "sword" : {'weapon' : 'sword', 'damage' : 5+bul_dam, 'img':"img\items\Weapons\Sword.png"},
        "bow" : {'weapon' : 'bow', 'damage' : 4+peir_dam, 'img':"img\items\Weapons\Bow.png"},
        "staff" : {'weapon' : 'staff', 'damage': 2+mg_pn, 'img':"img\items\Weapons\wizard_staff_img.png"}}
x = random.randint(1, 20)/4
s = round(x, 1)
rare_weapons = {
            'flame sword' : {'weapon':'flame sword', 'damage':10+s, 'img':"img\items\Weapons\Flame_sword.png"},
            'electric bow' : {'weapon':'electric bow', 'damage':11+s, 'img':"img\items\Weapons\Electro_bow.png"},
            'dagger o death' : {'weapon':'dagger o death', 'damage':8+s, 'img':"img\items\Weapons\dagger_odeath.png"}}


entire_items = {
            "dagger" : {'item' : 'dagger', 'damage' : 6, 'img':"img\items\Weapons\dagger.png"},
            "sword" : {'item' : 'sword', 'damage' : 5+bul_dam, 'img':"img\items\Weapons\Sword.png"},
            "bow" : {'item' : 'bow', 'damage' : 4+peir_dam, 'img':"img\items\Weapons\Bow.png"},
            'flame sword' : {'item':'flame sword', 'damage':10+s, 'img':"img\items\Weapons\Flame_sword.png"},
            'electric bow' : {'item':'electric bow', 'damage':11+s, 'img':"img\items\Weapons\Electro_bow.png"},
            'dagger o death' : {'item':'dagger o death', 'damage':8+s, 'img':"img\items\Weapons\dagger_odeath.png"},
            'gold key': {'item':'gold key', 'damage':0, 'img':"img\items\gold_key_image.jpg"},
            "staff": {'item' : 'staff', 'damage': 2+mg_pn, 'img':"img\items\Weapons\wizard_staff_img.png"}
            }
consumablse = {
    'bread': {'item' : 'bread', 'hp': 3, 'img':"img\items\Food\Bread_img.png", 'food':5, 'amount':0, 'damage':0},
    'rum': {'item' : 'rum', 'hp': 5, 'img':"img\items\Food\Rum_img.png", 'food':2, 'amount':0, 'damage':0},
    'apple': {'item' : 'apple', 'hp': 1, 'img':"img\items\Food\Apple_img.png", 'food':4, 'amount':0, 'damage':0},
    'carrot': {'item' : 'carrot', 'hp': 2, 'img':"img\items\Food\Carrot_img.png", 'food':3, 'amount':0, 'damage':0},
    'cookie': {'item' : 'rum', 'hp': 6, 'img':"img\items\Food\Cookie_img.png", 'food':1, 'amount':0, 'damage':0},
    'fish': {'item' : 'fish', 'hp': 4, 'img':"img\items\Food\Fish_img.png", 'food':3, 'amount':0, 'damage':0},
    'magic mellon': {'item' : 'magic mellon', 'hp': 19, 'img':"img\items\Food\Melon_img.png", 'food':6, 'amount':0, 'damage':0}}
entire_items.update(consumablse)

#            :ARMOUR ADDONS:
#common armour = 1-5, uncomon armour = 5-10,
#rare armour = 10-15, very rare armour = 15-20,
#epic armour = 20-25, lej armour = 25-30,
#spec armour = 30-35, ultra armour = 35-40
#for stat addons = def addon/10
armour_items = {
    #leather
    'leather helmet':{'item':'leather helmet', 'def':1.5, 'add':0.1, 'img':"img\items\Armour\Helmet_leather.png", 'type':'helmet'},
    'leather chestplate':{'item':'leather chestplate', 'def':2, 'add':0.25, 'img':"img\items\Armour\Chestplate_leather.png", 'type':'chestplate'},
    'leather leggings':{'item':'leather leggings', 'def':2, 'add':0.2, 'img':"img\items\Armour\Leather_leggings.png", 'type':'leggings'},
    'leather boots':{'item':'leather boots', 'def':1 , 'add':0.1, 'img':"img\items\Armour\Boots_leather.png", 'type':'boots'},
    'leather gauntlets':{'item':'leather gauntlets', 'def':1.5 , 'add':0.15, 'img':"img\items\Armour\Helmet_gauntlets.png", 'type':'gauntlets'},
    #chainmail
    'chainmail helmet':{'item':'chainmail helmet', 'def':4, 'add':0.2, 'img':"img\items\Armour\Helmet_chainmail.png", 'type':'helmet'},
    'chainmail chestplate':{'item':'chainmail chestplate', 'def':3.5, 'add':0.35, 'img':"img\items\Armour\Chestplate_chainmail.png", 'type':'chestplate'},
    'chainmail leggings':{'item':'chainmail leggings', 'def':3.5, 'add':0.3, 'img':"img\items\Armour\Leggings_chainmail.png", 'type':'leggings'},
    'chainmail boots':{'item':'chainmail boots', 'def':4 , 'add':0.1, 'img':"img\items\Armour\Boots_chainmail.png", 'type':'boots'},
    'chainmail gauntlets':{'item':'chainmail gauntlets', 'def':3.5 , 'add':0.35, 'img':"img\items\Armour\Gauntlets_chainmail.png", 'type':'gauntlets'},
    #iron armour
    'iron helmet':{'item':'iron helmet', 'def':4.5, 'add':0.3, 'img':"img\items\Armour\Helmet_iron.png", 'type':'helmet'},
    'iron chestplate':{'item':'iron chestplate', 'def':5, 'add':0.45, 'img':"img\items\Armour\Chestplate_iron.png", 'type':'chestplate'},
    'iron leggings':{'item':'iron leggings', 'def':5.5, 'add':0.5, 'img':"img\items\Armour\Leggings_iron.png", 'type':'leggings'},
    'iron boots':{'item':'iron boots', 'def':3.5 , 'add':0.3, 'img':"img\items\Armour\Boots_iron.png", 'type':'boots'},
    'iron gauntlets':{'item':'iron gauntlets', 'def':4.5 , 'add':0.45, 'img':"img\items\Armour\Gauntlets_iron.png", 'type':'gauntlets'}}
    
armour_name = []
for  i in armour_items:
    armour_name.append(i)
entire_items.update(armour_items)
possible_armour = ['helmet', 'chestplate', 'leggings', 'gauntlets','boots']
consumable_list = ['bread', 'rum', 'apple']
quest_list = ['gold key', 'kill bandits']
quests = {
    'gold key' : {'quest':'gold key', 'money reward':50, 'item reward':'dagger'},
    'kill bandits' : {'quest':'kill bandits', 'money reward':80, 'item reward':'electric bow'}
    }
