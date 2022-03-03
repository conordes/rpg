from player import *
from pygame_battle import*
from tavern import*
import random
plr.__init__(plr)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (0, 0, 0)
class r:
    def __init__(self):
        self.g = start_battle(page)
class f:
    def __init__(self):
        self.b = start_bar(page)
class doorz:
    def __init__(self):
        self.unlocked = False
        self.locked = True
        self.room = 0 # 0 = starter room 1 = town 2 = tavern 3 = forest
           
window_width = 840
window_height = 700
enemy_speed = random.randint(2, 4)

inventory_layer = 5
player_layer = 4
enemy_layer =  3
block_layer = 2
ground_layer = -1
hidden_layer = 0
items_layer = 6
text_layer = 7

tilesize = 42
fps = 30

