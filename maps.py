import pygame
from player_sprite import*
import random
import math
from maps_helper import*
from pygame_battle import*
from battle_button import Button
import sys
from all_items import*
from npc_sprite import*
from tavern import*
from equipped_items import equip_screen
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
orange = (200, 125, 0)
plr.hp = 9
plr.tot_hp = 10
fps = 30
doorz.__init__(doorz)
doorz.room = 0
pygame.time.Clock().tick(fps)
class game:
    def __init__(self):
        self.tilemap_b = [
            'bbbbbbbbjjjjjbbbbbbb',
            'b........jjj....bbbb',
            'b.........h......bbb',
            'b..v......h.q.....bb',
            'b.........h........b',
            'b.........hhhh.....b',
            'b.hhhhhhhhh........bbbbbbbbb',
            'b.........h................b',
            'b.......0.h.........3......b',
            'b........ hp...............b',
            'b..x.....hhhhhhhhh.........b',
            'b.h.......h......h.........b',
            'b.h.......h......hhhhhhhhh.b',
            'b.hhhhhhhhh...x....bbbbbbbbb',
            'b.........h........b',
            'b.........h........b',
            'b...n.....hhhhhhh..b',
            'b.........h........b',
            'b.........h..i.....b',
            'b.....hhhhh........b',
            'b.........h........b',
            'b...n.....h........b',
            'b.........h........b',
            'b.........hhhhhh...b',
            'b..hhhhhhhh...n....b',
            'b..................b',
            'bbbbbbbbbbbbbbbbbbbb',
]
        self.tilemap_a = [
            'bbbbbbbbbbbbbbbbbbbb',
            'b89......../..../.4b',
            'b..e.........!....cb',
            'b..................b',
            'b[[[[[[b..b[[b[[b[[b',
            'b..y...........y...b',
            'b.e......n.........b',
            'b........p........db',
            'b.>t.<.............b',
            'b4.......bw..e.....b',
            'b........b.........b',
            'b..e!....bw........b',
            'b........b.:s..!...b',
            'b...c....b.4.......b',
            'bbbbbbbbbbbbbbbbbbbb',
]

        self.tilemap_c = [
            'bbbbbbbbbbbb',
            'b4444444444bbbbbbbbb',
            'b....7.....5.......b',
            'b6.................b',
            'b2.2.2.2.2.2.......b',
            'b..................b',
            'b....2.......2.....b',
            'b....1.......1n....b',
            'b...2.2.....2.2....b',
            'b..................b',
            'b....2.......2.....b',
            'b.n..1.......1.....b',
            'b...2.2..p..2.2....b',
            'b....2...d...2.....b',
            'bbbbbbbbbbbbbbbbbbbb',
]
        self.tilemap_d =[
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
            'b..t.....q...........j....[...........s...j.b',
            'b.....j.......[..j...........j..e...........b',
            'b.j.................]................s.j....b',
            'b.........j...j..........j....s.............b',
            'b.......p.......t..bbbbbbbbbbbbbbbbbbbbbbbbbb',
            'b....j..t......j...b',
            'b.s................b',
            'b.[..j....e.....s..b',
            'bj............j....b',
            'b.......s..........b',
            'b..j............j..b',
            'b........j...t.....b',
            'b...s..............b',
            'b.j........j....t..b',
            'b......j....[......b',
            'b[.......s......j..b',
            'b....j.............bbbbbbbbbbbbbbbbbbbbbbbbbbb',
            'b.......j...j..s.....e....s....j....t........b',
            'b.j.s.........j.....t..]................j....b',
            'b..........................e......j..........b',
            'b.j......t.....j......j.....s.....t......t...b',
            'b......j.............j.........[.......j.....b',
            'b........[.........bbbbbbbbbbbbbbbbbbbbbbbbbbb',
            'b..j..........e....b',
            'b.....t............b',
            'b..j.......j.......b',
            'b.............tt...b',
            'b.....j....[.......b',
            'b..t...............b',
            'bbbbbbbbbbbbbbbbbbbb',
]
    

        screen = pygame.display.set_mode((window_width, window_height))
        self.screen = screen
        self.running = True
        level_ladder = {1:100, 2:200, 3:400, 4:600, 5:900, 6:1200, 7:1400, 8:1700, 9:2000, 10:2400, 11:2700, 12:3000, 13:3300, 14:3600,
                        15:4000,
                        16:4500,
                        17:5000}
        self.amount_item = 0
        back_img = pygame.image.load('img\panel.png')
        self.back_img = pygame.transform.scale(back_img, (840, 1000))
        self.screen.blit(self.back_img, (0, 0))
        plr.nxt_lvl_xp = level_ladder[plr.level+1]
        self.werty = False
        self.armour_show = False

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.text_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.inventory = pygame.sprite.LayeredUpdates()
        self.potion = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        self.chest = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.npc = pygame.sprite.LayeredUpdates()
        self.door = pygame.sprite.LayeredUpdates()
        self.text = pygame.sprite.LayeredUpdates() 
        self.furniture = pygame.sprite.LayeredUpdates()
        self.house_a = pygame.sprite.LayeredUpdates()
        self.house_b = pygame.sprite.LayeredUpdates()
        self.tavern = pygame.sprite.LayeredUpdates()
        self.market = pygame.sprite.LayeredUpdates()
        self.tavern_door = pygame.sprite.LayeredUpdates()
        self.UI = pygame.sprite.LayeredUpdates()
        self.bar_counter = pygame.sprite.LayeredUpdates()
        self.wizard_tower = pygame.sprite.LayeredUpdates()
        self.forest_gate = pygame.sprite.LayeredUpdates()
        self.tree = pygame.sprite.LayeredUpdates()
        self.gate = pygame.sprite.LayeredUpdates()
        self.speech_bubble = pygame.sprite.LayeredUpdates()
        
        
        words_a = ('item amount:{}'.format(str(self.amount_item)))
        words_e = ('potions: {}'.format(str(plr.potions)))
        words_f = ('money: {}'.format(str(plr.money)))
        words_g = ('level: {}'.format(str(plr.level)))
        words_h = ('mana: {}/{}'.format(str(plr.mana), str(plr.max_mana)))
        words_t = ('quest: {}'.format(plr.quest))
        words_d = ('weapon damage: {}'.format(str(plr.plwd)))
        words_o = ('total defense: {}'.format(str(plr.defense)))

        wep_img = entire_items[plr.weap]['img']
        equip_img = pygame.image.load("img\Equip_ton.jpg")
        
        self.t1 = text(words_a, 40, 590, self.screen, orange, self)
        self.t2 = text(words_e, 240, 610, self.screen, orange, self)
        self.t3 = text(words_f, 240, 630, self.screen, red, self)
        self.t4 = text(words_g, 240, 650, self.screen, blue, self)
        self.t5 = text(words_h, 40, 610, self.screen, orange, self)
        self.t6 = text(words_t, 40, 630, self.screen, orange, self)
        self.t7 = text(words_d, 230, 590, self.screen, green, self)
        self.t8 = text(words_o, 40, 650, self.screen, orange, self)

    #addons
        self.health_bar = healthbar(550, 580, plr.hp, plr.tot_hp, self.screen, self)
        self.armour_screen = equip_screen(self, 250, 250, self.screen)
        self.equip_button = Button(self.screen, 400, 600, equip_img, 90, 40, self)
        self.num = 0
    def events(self):
        # makes sure theres no duplicates in plr.items:
        plr.items = list(dict.fromkeys(plr.items))
        
        if doorz.room == 0 and doorz.unlocked == True:
            #starter room
            doorz.room = 1
            start_map_town()
            plr.mana += 40
            if plr.mana> plr.max_mana:
                plr.mana = plr.max_mana
        if doorz.room == 1 and doorz.unlocked == True:
            #town
            start_map_game()
        if doorz.room == 2 and doorz.unlocked == True:
            #tavern
            tilemaps(self.tilemap_c, False, 2)
        if doorz.room == 3 and doorz.unlocked == True:
            #forest
            tilemaps(self.tilemap_d, True, 3)

        self.screen.fill((0, 0, 0))
        change_colour = (0, 255, 0)
    # text

        words_a = ('item amount:{}'.format(str(self.amount_item)))
        if 'gold key' in plr.items:
            words_b = 'you found the key!'
            colour_change = (255, 255, 0)
        words_e = ('potions: {}'.format(str(plr.potions)))
        words_f = ('money: {}'.format(str(plr.money)))
        words_g = ('level: {}'.format(str(plr.level)))
        words_h = ('mana: {}/{}'.format(str(plr.mana), str(plr.max_mana)))
        words_t = ('quest: {}'.format(plr.quest))
        words_d = ('weapon damage: {}'.format(str(plr.plwd)))
        words_o = ('total defense: {}'.format(str(plr.defense)))

        wep_img = entire_items[plr.weap]['img']

        self.t1.ptr(words_a)
        self.t2.ptr(words_e)
        self.t3.ptr(words_f)
        self.t4.ptr(words_g)
        self.t5.ptr(words_h)
        self.t6.ptr(words_t)
        self.t7.ptr(words_d)
        self.t8.ptr(words_o)


    #functions for items
        self.health_bar.draw(plr.hp)
        def potion_use():
            potion_effect = 2
            if plr.potions > 0:                      
                if (plr.tot_hp - plr.hp) > potion_effect:
                    heal_amount = potion_effect
                else:
                    heal_amount = plr.tot_hp - plr.hp
                plr.hp += heal_amount
                plr.potions -= 1

        def go(x, on, sub):
                pos = pygame.mouse.get_pos()
                x.clicked = False

                #check mouseover and clicked conditions
                if x.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and x.clicked == False:
                                x.action = True
                                x.clicked = True

                if pygame.mouse.get_pressed()[0] == 0:
                        x.clicked = False
                if on:
                    x.draw()
                if x.clicked:
                    sub()
                    clicked = True
                else:
                    clicked = False

        def weapon_change(item):
            if item in consumable_list:
                self.amount_item = consumablse[item]['amount']
                img = consumablse[item]['img']
                if consumablse[item]['amount'] <= 0:
                    plr.items.remove(item)
                    plr.item_img.remove(img)
                else:
                    plr.hp += consumablse[item]['hp']
                    consumablse[item]['amount'] -= 1
            elif item in armour_items:
                plr.armour_add(plr, armour_items[item]['type'],item)
            else:
                plr.weap = item
                dam = entire_items[item]['damage']
                plr.plwd = dam
        def item_go(x, on, sub, item):
            pos = pygame.mouse.get_pos()
            x.clicked = False
        #check mouseover and clicked conditions
            if x.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and x.clicked == False:
                            x.action = True
                            x.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                    x.clicked = False
            if on:
                x.draw()
            if x.clicked:
                sub(item)
                clicked = True
            else:
                clicked = False
        #........................................................................
        intro = 'press the weapon you want to equip'
        get_current_time = pygame.time.get_ticks()
        start_time = get_current_time
        coin_img = pygame.image.load("img\items\coin_image.jpg")  
        potion_img = pygame.image.load("img\items\Potions\Hp_potion.png")
        #open armour
        if self.equip_button.draw():
            if self.num == 0:
                self.armour_show = True
                self.num = 1
            elif self.num == 1:
                self.armour_show = False
                self.num = 0
        #open armour
        #levels
        if plr.xp >= plr.nxt_lvl_xp:
            plr.level += 1
            plr.xp = 0
            plr.str += 0.5*plr.level
            plr.hp += 3*plr.level
            plr.int += 1*plr.level
            f = plr.max_mana/10
            p = f*5 +plr.int
            plr.max_mana += p
        #levels
        #quests
        if plr.quest == 'gold key':
            if 'gold key' in plr.items:
                plr.money += 50+(random.randint(1, 15)*10)
                plr.xp += 100
                plr.items.append('flame sword')
                plr.weap = plr.items[0]
                quest_list.remove('gold key')
                plr.quest = 'done'
                plr.items.remove('gold key')
                plr.weap = plr.items[0]

        if plr.quest == 'kill bandits':
            if plr.bandits_killed >= 8:
                plr.money += 80+(random.randint(1, 20)*10)
                plr.xp += 150+random.randint(1, 100)
                plr.items.append('dagger o death')
                quest_list.remove('kill bandits')
                plr.quest = 'done'
        #quest
        #show items in inventory
        plr.armour_list = [plr.armour[x]['name'] for x in possible_armour]
        if self.werty:
            for i in plr.items:
                s = entire_items[i]['img']
                if i not in armour_items:
                    dam = entire_items[i]['damage']
                name = entire_items[i]['item']
                im = pygame.image.load(s)
                l = plr.items.index(i)+1
                li = l*50
                x_o = 840
                if plr.items.index(i)>11:
                    x_o = 890
                    l = plr.items.index(i)-11
                    li = l*50
                nam = Button(self.screen, x_o, li, im, 50, 50, self)
                potion_button = Button(self.screen, 840, 0, potion_img, 50, 50, self)
                item_go(nam, True, weapon_change, name)
                go(potion_button, True, potion_use)
        #show items in inventory
        #armour view

        if self.armour_show:
            self.armour_screen.draw(300, 400, True)
        else:
            self.armour_screen.on = False
            self.armour_screen.draw(300, 400, False)
        #armour view
        #event manager
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    pygame.mouse.set_visible(True)
                    screen = pygame.display.set_mode((1030, window_height))
                    inventory(self, 840, 0, True, screen)
                    plr.inventory_not_open = False
                    self.werty = True
                    self.armour_screen.on = True
                if event.key == pygame.K_c:
                    inventory(self, 840, 0, False, self.screen)
                    screen = pygame.display.set_mode((window_width, window_height))
                    self.all_sprites.update()
                    plr.inventory_not_open = True
                    self.werty = False
        #event manager            
                    
    def update(self):
        self.all_sprites.update()
        self.text_sprites.update()
            
    def draw(self):
        self.all_sprites.draw(self.screen)
        self.text_sprites.draw(self.screen)
        pygame.display.update()
    def main(self):
        black = (0, 0, 0)
        while self.playing:
            self.draw()
            self.events()
            self.update()
        self.running = False

    def gameover(self):
        pass
    def intro_screen(self):
        pass

class enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, ter):
        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 0
        self.movement_loop = 0
        self.frame = {
            'right':0,
            'left':0}
        self.max_travel = random.randint(10, 30)
        self.image = self.mon_image()


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        self.animate()
        self.image.set_colorkey((0, 0, 0))
            
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
           
        self.x_change = 0
        self.y_change = 0
    def mon_image(self):
        mon = random.randint(1, 2)
        if mon == 1:
            self.name = 'Light Bandit'
            self.name_b = 'LightBandit'
            image = pygame.image.load('img\Sprites\Idle\LightBandit_Idle_0.png').convert()
            image = pygame.transform.scale(image, (tilesize+20, tilesize+20))

        elif mon == 2:
            self.name = 'Heavy Bandit'
            self.name_b = 'HeavyBandit'
            image = pygame.image.load('img\HeavyBandit_Idle_0.png').convert()
            image = pygame.transform.scale(image, (tilesize+20, tilesize+20))
        self.mon = mon
        return image
    def animate(self):
        if self.frame[self.facing]>=8 and self.facing == 'right':
            self.frame[self.facing] = 0
        if self.frame[self.facing]>=8 and self.facing == 'left':
            self.frame[self.facing] = 0
        self.lb_right = []
        self.lb_left = []
        self.hb_right = []
        self.hb_left = []
        for i in range(8):
            fe = pygame.image.load(f"img\Sprites\{self.name}\Run_right\{self.name_b}_Run_{i}.png").convert()
            f = pygame.transform.scale(fe, (tilesize, tilesize*2))
            if self.mon == 1:
                self.lb_right.append(f)
            else:
                self.hb_right.append(f)
        for i in range(8):
            fe = pygame.image.load(f"img\Sprites\{self.name}\Run\{self.name_b}_Run_{i}.png").convert()
            f = pygame.transform.scale(fe, (tilesize, tilesize*2))
            if self.mon == 1:
                self.lb_left.append(f)
            else:
                self.hb_left.append(f)
        if self.mon == 1:
            if self.facing == 'right':
                self.image = self.lb_right[self.frame[self.facing]]
                self.frame[self.facing] +=1
            elif self.facing == 'left':
                self.image = self.lb_left[self.frame[self.facing]]
                self.frame[self.facing] +=1               
        if self.mon == 2:
            if self.facing == 'right':
                self.image = self.hb_right[self.frame[self.facing]]
                self.frame[self.facing] +=1
            elif self.facing == 'left':
                self.image = self.hb_left[self.frame[self.facing]]
                self.frame[self.facing] +=1   
    def movement(self):
        if self.facing == 'left':
            self.x_change -= enemy_speed
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
                    
        if self.facing == 'right':
            self.x_change += enemy_speed
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.facing = 'left'
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.facing = 'right'
                    


class block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, imge, sx, sy, ler, kinda):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, {kinda}
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y*tilesize
        size_x = sx*tilesize
        size_y = sy*tilesize
        self.width = size_x
        self.height = size_y
        white = (255, 255, 255)

        self.weird_colorkey = ler

        image = pygame.image.load(imge).convert_alpha()
        self.img = pygame.transform.scale(image, (size_x, size_y))
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        if self.weird_colorkey == False:
            print("wy")
            self.image.set_colorkey(black)

        self.image.blit(self.img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class furniture(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image, sx, sy, search, has):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.furniture
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y*tilesize
        size_x = sx*tilesize
        size_y = sy*tilesize
        self.width = size_x
        self.height = size_y
        white = (255, 255, 255)

        self.image = pygame.Surface([self.width, self.height])
        image = pygame.image.load(image).convert_alpha()
        self.img = pygame.transform.scale(image, (size_x, size_y))
        self.image.set_colorkey(black)
        if has:
            self.image.blit(self.img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.image.blit(self.img, (0,0))


class door(pygame.sprite.Sprite):
    def __init__(self, game, x, y, ger, door):
        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, {door} 
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y*tilesize
        size_x = 2*tilesize
        size_y = 1*tilesize
        self.width = size_x
        self.height = size_y
        white = (255, 255, 255)

        image = pygame.image.load("img\items\door.jpg")
        self.img = pygame.transform.scale(image, (size_x, size_y)).convert_alpha()
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        if doorz.room == 3:
            self.image.set_colorkey(black)
        if ger:
            self.image.blit(self.img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.image.blit(self.img, (0,0))

class ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img, der):
        self.game = game
        self._layer = 1
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*tilesize
        self.y = y*tilesize
        self.width = tilesize
        self.height = tilesize

        image = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(image, (tilesize, tilesize))
        self.image = pygame.Surface([self.width, self.height])
        if der:
            self.image.blit(self.img, (0,0))
            self._layer = block_layer

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.image.blit(self.img, (0,0))
class inventory(pygame.sprite.Sprite):
    def __init__(self, game, x, y, on, screen):
        black = (0, 0, 0)
        self.game = game
        self.groups = self.game.text_sprites, self.game.inventory
        pygame.sprite.Sprite.__init__(self, self.groups)
        self._layer = 9

        self.x = x
        self.y = y
        self.width = 170
        self.height = 700
        image = pygame.image.load("img\Inventory_image.png").convert()
        self.img = pygame.transform.scale(image, (170, 700))
        self.image = pygame.Surface([self.width, self.height])
        if on:
            self.image.blit(self.img, (0,0))
        else:
            self._layer = 0
           
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Button(pygame.sprite.Sprite):
        def __init__(self, surface, x, y, image, size_x, size_y, game):
                self.game = game
                self.groups = self.game.text_sprites, self.game.items
                pygame.sprite.Sprite.__init__(self, self.groups)
                self._layer = 10
                white = (255, 255, 255)
                self.img = pygame.transform.scale(image, (size_x, size_y)).convert()
                self.img.set_colorkey(white)
                self.width = self.img.get_width()
                self.height = self.img.get_height()
                self.image = pygame.Surface([self.width, self.height])
                self.image.set_colorkey((0, 0, 0))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False
        def draw(self):
                white = (255, 255, 255)
                self.action = False

                #get mouse position
            
                pos = pygame.mouse.get_pos()


                #check mouseover and clicked conditions
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                self.action = True
                                self.clicked = True

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                #draw button
                self.image.blit(self.img, (0, 0))
                return self.action

class healthbar(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, max_hp, screen, game):
        self.game = game
        self.screen = screen
        self.groups = self.game.text_sprites, self.game.healthbar
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y+30
        self.hp = hp
        self.max_hp = max_hp
        self._layer = 11

        self.width = tilesize*4
        self.height = tilesize*2


        self.draws()
    def draw(self, hp):
        self.hp = hp
        self.draws()
    def draws(self):
        self.user_hp = round(self.hp/self.max_hp, 1)
        self.chooser = 0
        if self.user_hp == 0.9 or self.user_hp == 0.8:
            self.chooser = 1
        elif self.user_hp == 0.7:
            self.chooser = 2
        elif self.user_hp == 0.6:
            self.chooser = 3
        elif self.user_hp == 0.5:
            self.chooser = 4
        elif self.user_hp == 0.4:
            self.chooser = 5
        elif self.user_hp == 0.3:
            self.chooser = 6
        elif self.user_hp == 0.2:
            self.chooser = 7
        elif self.user_hp == 0.1:
            self.chooser = 8
        elif self.user_hp == 0:
            self.chooser = 9

        self.img = pygame.image.load(f"img\items\Potions\health\sprite_{self.chooser}.png").convert()
        self.imgz = pygame.transform.scale(self.img, (self.width, self.height))
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.imgz, (0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
class chest(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image, fer):
        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.chest
        pygame.sprite.Sprite.__init__(self, self.groups)

        white = (255, 255, 255)

        self.x = x*tilesize
        self.y = y*tilesize
        self.width = tilesize
        self.height = tilesize
        
        self.img = pygame.transform.scale(image, (tilesize, tilesize)).convert()
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        if fer:
            self.image.blit(self.img, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.image.blit(self.img, (0,0))

class text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, screen, col, game):
        terz = 1
        self.game = game
        self._layer = 10
        self.groups = self.game.text_sprites, self.game.text
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.text = text
        self.col =col
        self.x = x
        self.y = y
        self.rerun()
    def ptr(self, text):
        self.text = text
        self.rerun()
        
    def rerun(self):
        self.font = pygame.font.SysFont('SH Pinscher Regular', 30)
        self.textSurf = self.font.render(self.text, 4, self.col)
        self.width = self.textSurf.get_width()
        self.height = self.textSurf.get_height()
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.textSurf, (0, 0))
        
class house(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image, sx, sy, inside, dark):
        self.game = game
        self._layer = 7
        self.groups = self.game.all_sprites, {inside}
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        sx += 1
        sy += 1
        dec = image

        self.x = x * tilesize
        self.y = y*tilesize
        size_x = sx*tilesize
        size_y = sy*tilesize
        self.width = size_x
        self.height = size_y
        white = (255, 255, 255)

        image = pygame.image.load(image).convert()
        self.img = pygame.transform.scale(image, (size_x, size_y))
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        
        self.image.blit(self.img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class tree(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image, sx, sy, place):
        self.game = game
        self._layer = text_layer
        self.groups = self.game.all_sprites, {place}
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y*tilesize
        size_x = sx*tilesize
        size_y = sy*tilesize
        self.width = size_x
        self.height = size_y
        white = (255, 255, 255)

        image = pygame.image.load(image).convert()
        self.img = pygame.transform.scale(image, (size_x, size_y)).convert_alpha()
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(black)
        self.image.blit(image, (0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.image.blit(self.img, (0,0))

class eq_weap(pygame.sprite.Sprite):
    def __init__(self, x, y, img, game):
        self.game = game
        self._layer = 11
        self.groups = self.game.text_sprites, self.game.text
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.size_x = 50
        self.size_y = 50
        self.width = self.size_x
        self.height = self.size_y
        white = (255, 255, 255)
        self.imgz = img
        self.draw()

    def ptr(self, img):
        self.imgz = img
        self.draw()

    def draw(self):
        image = pygame.image.load(self.imgz)
        self.image = pygame.Surface([self.width, self.height])
        self.img = pygame.transform.scale(image, (self.size_x, self.size_y))
        self.image.set_colorkey(white)
        self.img.set_colorkey(white)
        self.image.blit(self.img, (0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class createtilemap:
    def __init__(self, game, screen, chang, maps, outside, room):
        self.screen = screen
        self.game = game
        groupz = self.game.door
        size_a = 2
        size_b = 1
        boor = room
        if boor == 2:
            groupz = self.game.tavern_door
            size_a = 12
            size_b = 1
            gurber = self.game.bar_counter
        elif boor == 3:
            groupz = self.game.forest_gate
        else:
            groupz = self.game.door
            gurber = self.game.blocks
        wardroab_img = "img\items\Wardroab_image.png"
        table_img = "img\items\Table_image.png"
        bed_img = "img\items\Bed_image.png"
        side_chair_img = "img\items\Side_chair_image.png"
        bed_side_table_img = "img\items\Bedside_table_image.png" 
        couch_img = "img\items\Couch_image.png"
        front_chair_img = "img\items\Front_chair_image.png"
        bedside_table_img = "img\items\Bedside_table_image.png"
        table_top_img = "img\items\Table_top_image.png"
        grass_img = "img\items\Forest\Rock_plant_img.png"
        bookshelf_img = "img\items\Bookshelve_image.jpg"
        wall_img = "img\wall.png"
        npc_img = pygame.image.load("img\Talker_img.png").convert_alpha()
        market_img = "img\items\Town\Market.png"
        ground_img = "img\Wooden_floor.png"
        path_img = "img\Path_img.png"
        house_a_img = "img\items\Town\House_1.png"
        house_b_img = "img\items\Town\House_2.png"
        tavern_img = "img\items\Town\Tavern_img.png"
        wizard_tower_img = "img\items\Town\Wizard_tower.gif"
        bar_table_img = "img\items\Bar_table.png"
        bar_stool_img = "img\items\Bar_stool.png"
        tavern_drinks = "img\items\Tavern_furniture.jpg"
        mat_img = "img\items\Mat_img.png"
        stove_img = "img\items\Stove_img.png"
        sink_img = "img\items\Sink_img.png"
        wheelbarough_img = "img\items\Town\Wheelbarough_img.png"
        book_x = 1
        book_y = 1
        bed_x = 3
        bed_y = 2
        tab_x = 1
        tab_y = 2
        tavx = 1
        tavy = 1
        house_choose = self.game.house_a
        if outside == True:
            ground_img = "img\items\Town\Grass.png"
            wall_img = "img\items\Town\Tree_img.png"
            bookshelf_img = "img\items\Forest\Log_img.png"
            bed_img = "img\items\Forest\Bush_img.png"
            table_img = "img\items\Forest\Rock_img.png"
            book_x = 2
            book_y = 2
            bed_x = 1.5
            bed_y = 1
            book_y = 0.5
            tab_x = 2.5
            tab_y = 2
        if doorz.room == 3:
            house_choose = self.game.gate
            house_a_img = "img\items\Forest\Gate_img.png"
            ground_img = "img\items\Forest\Forest_floor_img.png"
            wall_img = "img\items\Forest\Forest_tree.png"
            tavern_drinks = grass_img
            tavx = 0.5
            tavy = 0.5
        elif doorz.room == 0:
            tavern_drinks = "img\items\Plant_img.png"
            tavx = 0.5
            tavy = 0.5
        self.change_srn = chang
        if chang:
            for i, row in enumerate(maps):
                for j, column in enumerate(row):
                    ground(self.game, j, i, ground_img, self.change_srn)
                    if column == '.':
                        ground(self.game, j, i, ground_img, self.change_srn)
                        if doorz.room == 3:
                            x = random.randint(1, 3)
                            if x == 3:
                               f = furniture(self.game, j, i, tavern_drinks, 0.5, 0.5, True, self.change_srn)
                               f._layer = 1
                                
                    if column == 'b':
                        x = block(self.game, j, i, wall_img, 1, 1, self.change_srn, self.game.blocks)
                        if doorz.room == 1:
                            print("we")
                            x.weird_colorkey = False
                    if column == 'e':
                        enemy(self.game, j, i, self.change_srn)
                    if self.change_srn:
                        if column == 'p':
                            self.player = player(self.game, j, i, self.screen)
                    if column == 'c':
                        image = pygame.image.load("img\items\chest.jpg").convert()
                        chest(self.game, j, i, image, self.change_srn)
                    if column == 'n':
                        if doorz.room == 1:
                            npc_img = random.choice([
                                pygame.image.load("img\Sprites\Characters\Villager_b_img.png").convert(),
                                pygame.image.load("img\Sprites\Characters\Villager_img.png").convert()])
                        chosen_text = random.choice(['thankyou for freeing that house!', 'go to the tavern to get a mission!'])
                        imgz = npc_img
                        npc_a = npc(self.game, j, i, imgz.convert_alpha(), self.screen, self.change_srn, True, chosen_text)
                    if column == 'B':
                        furniture(self.game, j, i, bed_side_table_img, 1, 1, True, self.change_srn)
                    if column == 'y':
                        img = "img\items\cuboard_image.png"
                        furniture(self.game, j, i, img, 2, 1, True, self.change_srn)
                    if column == 'w':
                        furniture(self.game, j, i, wardroab_img, 1, 2, True, self.change_srn)
                    if column == 't':
                        furniture(self.game, j, i, table_img, tab_x, tab_y, True, self.change_srn)
                    if column == 's':
                        furniture(self.game, j, i, bed_img, bed_x, bed_y, True, self.change_srn)
                    if column == '<':
                        furniture(self.game, j, i, side_chair_img, 1, 1, True, self.change_srn)
                    if column == '>':
                        furniture(self.game, j, i, front_chair_img, 1, 1, True, self.change_srn)
                    if column == '/':
                        furniture(self.game, j, i, couch_img, 2, 1, True, self.change_srn)
                    if column == '@':
                        furniture(self.game, j, i, table_top_img, 2, 1, True, self.change_srn)
                    if column == '6':
                        block(self.game, j, i, table_top_img, size_a, size_b, self.change_srn, gurber)
                    if column == '[':
                        block(self.game, j, i, bookshelf_img, book_x, book_y, False, self.game.blocks)
                    if column == ':':
                        furniture(self.game, j, i, side_chair_img, 1, 1, True, self.change_srn)
                    if column == 'd':
                        door(self.game, j, i, self.change_srn, groupz)
                    if column == '8':
                        furniture(self.game, j, i, stove_img, 1, 1, True, self.change_srn)
                    if column == '9':
                        furniture(self.game, j, i, sink_img, 1, 1, True, self.change_srn)
                    if column == 'm':
                        furniture(self.game, j, i, market_img, 2, 1, True)
                    if column == 'h':
                        ground(self.game, j, i, path_img, self.change_srn)
                    if column == '!':
                        furniture(self.game, j, i, mat_img, 2, 2, True, self.change_srn)
                    if column == 'q':
                        house(self.game, j, i, house_a_img, 3, 3, house_choose, False)
                        block(self.game, j, i, house_a_img, 4-0.1, 4-0.1, self.change_srn, self.game.blocks)
                    if column == 'x':
                        house(self.game, j, i, house_b_img, 3, 3, self.game.house_b, False)
                        block(self.game, j, i, house_b_img, 4-0.1, 4-0.1, self.change_srn, self.game.blocks)
                    if column == 'v':
                        house(self.game, j, i, tavern_img, 3, 3, self.game.tavern, False)
                        block(self.game, j, i, tavern_img, 4-0.1, 4-0.1, self.change_srn, self.game.blocks)
                    if column == '3':
                        house(self.game, j, i, market_img, 4, 4, self.game.market, False)
                        block(self.game, j, i, market_img, 5-0.1, 5-0.1, self.change_srn, self.game.blocks)
                    if column == 'i':
                        house(self.game, j, i, wizard_tower_img, 2, 4, self.game.wizard_tower, False)
                        block(self.game, j, i, wizard_tower_img, 3-0.1, 5-0.1, self.change_srn, self.game.blocks)
                    if column == '1':
                        furniture(self.game, j, i, bar_table_img, 1, 2, True, self.change_srn)
                    if column == '2':
                        furniture(self.game, j, i, bar_stool_img, 1, 1, True, self.change_srn)
                    if column == '4':
                        block(self.game, j, i, tavern_drinks, tavx, tavy, self.change_srn, self.game.blocks)
                    if column == '5':
                        block(self.game, j, i, ground_img, 1, 1, self.change_srn, self.game.blocks)
                    if column == '7':
                        img = pygame.image.load("img\items\Town\Bartender_img.png")
                        npc(self.game, j, i, img, self.screen, self.change_srn, False, 'welcome to the bar')
                    if column == 'j':
                        img = "img\items\Forest\Forest_tree.png"
                        if boor == 1:
                            tr = self.game.forest_gate
                        else:
                            tr = self.game.tree
                        tree(self.game, j, i, img, 1, 2, tr)
                    if column == '0':
                        furniture(self.game, j, i, wheelbarough_img, 2, 1.5, True, self.change_srn)
                        
class tilemaps:
    def __init__(self, name_tilemap, outside, t):
        g = game()
        g.intro_screen()
        g.new()
        doorz.unlocked = False
        doorz.locked = False
        while g.running :
            if page == True:
                screen = pygame.display.set_mode((window_width, window_height))
                start_map_game()
            createtilemap(g, g.screen, True, name_tilemap, outside, t)
            g.main()
            g.gameover()
        pygame.quit()
        quit()

def start_map_game():  
    g = game()
    g.intro_screen()
    g.new()
    doorz.unlocked = False
    doorz.locked = False
    while g.running :
        if page == True:
            screen = pygame.display.set_mode((window_width, window_height))
            start_map_game()
        createtilemap(g, g.screen, True, g.tilemap_a, False, 0)
        g.main()
        g.gameover()
    pygame.quit()
    quit()

def start_map_town():
    plr.level = 4
    doorz.unlocked = False
    doorz.locked = True
    g = game()
    g.intro_screen()
    g.new()
    while g.running:
        if page == True:
            screen = pygame.display.set_mode((window_width, window_height))
            start_map_town()
        createtilemap(g, g.screen, True, g.tilemap_b, True, 1)
        g.main()
        g.gameover()
    pygame.quit()
    quit()
